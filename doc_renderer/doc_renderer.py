from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from doc_renderer.paragraph_text_style import ParagraphTextStyle, ParagraphTextStyleEnum, ParagraphTextDecorationEnum
from doc_renderer.table_renderer import Row

import functools


class DocRenderer:
    title: str = ""

    location = 1
    objects: dict[str, tuple[int, int]] = {}
    # unprocessed_requests: list[docs.Request] = []
    # requests: list[docs.Request] = []
    unprocessed_requests = []
    requests = []

    # service: docs.DocsApi
    # document: docs.Document
    service = None
    document = None

    def __init__(self, title):
        self.title = title

    def create(self, credentials: Credentials):
        self.service = build('docs', 'v1', credentials=credentials)

        print("Creating a new document")
        self.document = self.service.documents().create(body={'title': self.title}).execute()
        print("New document created")

        print(self.document)

    def add_text_line(self, text: str, text_style: ParagraphTextStyle = None, new_line: bool = True):
        """Add text line"""
        self.unprocessed_requests.append({
            'insertText': {
                'location': {
                    'index': self.location,
                },
                'text': text + ("\n" if new_line else "")
            }
        })
        print(f"[{self.current_request()}] Adding a [{text}] text at location: {self.location}")
        print(f"[{self.current_request()}] Text has new line at the end: {new_line}")

        new_location = self.location + len(text) + (1 if new_line else 0)
        self.objects[text] = (self.location, new_location)
        print(f"[{self.current_request()}] Adding an object with indices: {self.location} - {new_location}")
        self.location = new_location
        print(f"[{self.current_request()}] Updating location to: {self.location}")

        if text_style is not None and text_style.style is not None:
            self.set_paragraph_style(text_style=text_style.style, tag=text)

        if text_style is not None:
            self.set_text_style(text_style=text_style, tag=text)

    def add_list(self, lines: list[str], text_style: ParagraphTextStyle = None):
        """Add unordered list """
        print(f"[{self.current_request()}] Adding {lines} to the document")
        for line in lines:
            self.add_text_line(line, text_style)
            self.unprocessed_requests.append({
                'createParagraphBullets': {
                    'range': {
                        'startIndex': self.objects[line][0],
                        'endIndex': self.objects[line][1],
                    },
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                }
            })
        print(f"[{self.current_request()}] Setting a bullet style to the {lines}")

    def set_text_style(self, text_style: ParagraphTextStyle, tag: str):
        """Set the text style"""
        fields = [
            "bold",
            "italic",
            "underline",
        ]

        print(f"[{self.current_request()}] Setting the {text_style.decorations} decorations to the [{tag}] text")
        style = {
            "bold": ParagraphTextDecorationEnum.BOLD in text_style.decorations,
            "italic": ParagraphTextDecorationEnum.ITALIC in text_style.decorations,
            "underline": ParagraphTextDecorationEnum.UNDERLINED in text_style.decorations,
        }

        if text_style.font_size is not None:
            print(f"[{self.current_request()}] Setting the [{text_style.font_size}] font size to the [{tag}] text")
            fields.append("fontSize")
            style["fontSize"] = {
                "magnitude": text_style.font_size,
                "unit": "PT"
            }

        if text_style.font_color is not None:
            print(f"[{self.current_request()}] Setting the [{text_style.font_color}] color to the [{tag}] text")
            fields.append("foregroundColor")
            style["foregroundColor"] = {
                "color": {
                    "rgbColor": {
                        "red": text_style.font_color.red,
                        "green": text_style.font_color.green,
                        "blue": text_style.font_color.blue,
                    }
                }
            }

        if text_style.background_color is not None:
            print(f"[{self.current_request()}] Setting the [{text_style.background_color}] color to the [{tag}] text")
            fields.append("backgroundColor")
            style["backgroundColor"] = {
                "color": {
                    "rgbColor": {
                        "red": text_style.background_color.red,
                        "green": text_style.background_color.green,
                        "blue": text_style.background_color.blue,
                    }
                }
            }

        self.unprocessed_requests.append({
            "updateTextStyle": {
                "range": {
                    "startIndex": self.objects[tag][0],
                    "endIndex": self.objects[tag][1],
                },
                "fields": ",".join(fields),
                "textStyle": style,
            }
        })
        print(f"[{self.current_request()}] Setting text style {text_style} to locations: "
              f"{self.objects[tag][0]} - {self.objects[tag][1]}")

    def set_paragraph_style(self, text_style: ParagraphTextStyleEnum, tag: str):
        """Set the paragraph style"""
        paragraph_style = text_style.value

        self.unprocessed_requests.append({
            "updateParagraphStyle": {
                "range": {
                    "startIndex": self.objects[tag][0],
                    "endIndex": self.objects[tag][1],
                },
                "fields": 'namedStyleType',
                "paragraphStyle": {
                    "namedStyleType": paragraph_style,
                },
            }
        })
        print(f"[{self.current_request()}] Setting style {paragraph_style} to locations: "
              f"{self.objects[tag][0]} - {self.objects[tag][1]}")

    def add_image(self, uri: str, height: float, width: float, new_line: bool = True):
        """Add an image from Google Drive into the Google Doc"""
        print(f"[{self.current_request()}] Adding an image {uri} to the document at {self.location} location")

        self.unprocessed_requests.append({
            "insertInlineImage": {
                "location": {
                    "index": self.location
                },
                "uri": uri,
                "objectSize": {
                    "height": {
                        "magnitude": height,
                        "unit": "PT"
                    },
                    "width": {
                        "magnitude": width,
                        "unit": "PT"
                    }
                }
            }
        })

        new_location = self.location + 1
        self.objects[uri] = (self.location, new_location)
        self.location = new_location

        print(f"[{self.current_request()}] Updating location to: {self.location}")
        if new_line:
            print(f"[{self.current_request()}] Adding an additional new line")
            self.add_text_line(text="")

    def add_table(self, rows: list[Row]):
        """Renders a table"""
        rows_count = len(rows)
        columns_count = max(map(lambda row: len(row.cells), rows))
        print(f"[{self.current_request()}] Adding a new table to the document at {self.location} location")
        print(f"[{self.current_request()}] Table has {rows_count} rows and {columns_count} columns")
        self.unprocessed_requests.append({
            "insertTable": {
                "rows": rows_count,
                "columns": columns_count,
                "endOfSegmentLocation": {
                    "segmentId": None
                }
            }
        })

        table_start_location = self.location + 1
        self.location += 4

        for row in rows:
            # If len(row.cells) > columns_count => range(0) => row.cells += []
            row.cells += [None for _ in range(columns_count - len(row.cells))]

            for cell in row.cells:
                if cell is not None:
                    print(f"AAAAAAAAAAAAAAAAA: {cell.text}")
                    self.add_text_line(text=cell.text, new_line=False, text_style=cell.text_style)
                    row_index = rows.index(row)
                    column_index = row.cells.index(cell)

                    if cell.background_color is not None:
                        print(f"[{self.current_request()}] Setting the [{cell.background_color}] "
                              f"color to the [{cell.text}] cell")
                        self.unprocessed_requests.append({
                            "updateTableCellStyle": {
                                "tableRange": {
                                    "rowSpan": 1,
                                    "columnSpan": 1,
                                    "tableCellLocation": {
                                        "rowIndex": row_index,
                                        "columnIndex": column_index,
                                        "tableStartLocation": {
                                            "index": table_start_location,
                                        }
                                    },
                                },
                                "tableCellStyle": {
                                    "backgroundColor": {
                                        "color": {
                                            "rgbColor": {
                                                "red": cell.background_color.red,
                                                "green": cell.background_color.green,
                                                "blue": cell.background_color.blue,
                                            }
                                        }
                                    }
                                },
                                "fields": "backgroundColor",
                            }
                        })

                    if cell.merge_right > 1 or cell.merge_down > 1:
                        self.unprocessed_requests.append({
                            "mergeTableCells": {
                                "tableRange": {
                                    "rowSpan": min(cell.merge_down, rows_count - row_index),
                                    "columnSpan": min(cell.merge_right, columns_count - column_index),
                                    "tableCellLocation": {
                                        "rowIndex": row_index,
                                        "columnIndex": column_index,
                                        "tableStartLocation": {
                                            "index": table_start_location,
                                        }
                                    },
                                },
                            }
                        })

                self.location += 2
            self.location += 1
        print(f"[{self.current_request()}] Current location is: {self.location}")
        self.location -= 1
        print(f"[{self.current_request()}] Updating location to: {self.location}")

    def current_request(self):
        """Get the index of the current request"""
        return len(self.unprocessed_requests) - 1

    def save(self):
        """Submit all the requests"""
        print(f"Unprocessed requests count: {len(self.unprocessed_requests)}")

        response = self.service.documents() \
            .batchUpdate(documentId=self.document['documentId'], body={'requests': self.unprocessed_requests}) \
            .execute()

        print(f"processed requests: {self.unprocessed_requests}")
        self.requests += self.unprocessed_requests
        self.unprocessed_requests.clear()

        print(response)
