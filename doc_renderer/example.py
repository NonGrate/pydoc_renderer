from google.oauth2.credentials import Credentials

from doc_renderer.color import Color
from doc_renderer.doc_renderer import DocRenderer
from doc_renderer.paragraph_text_style import ParagraphTextStyle, ParagraphTextStyleEnum, ParagraphTextDecorationEnum
from doc_renderer.table_renderer import Row, Cell


def example_doc_renderer(credentials: Credentials):
    renderer = DocRenderer("Pydoc renderer")
    renderer.create(credentials)

    renderer.add_text_line(text="PlainText0")

    renderer.add_text_line(
        text="FontFamily",
        text_style=ParagraphTextStyle(font_family="Roboto"),
    )
    renderer.add_text_line(
        text="FontFamily",
        text_style=ParagraphTextStyle(font_family="Arial"),
    )
    renderer.add_text_line(
        text="FontFamily",
        text_style=ParagraphTextStyle(font_family="Times New Roman"),
    )
    renderer.add_text_line(
        text="FontFamily",
        text_style=ParagraphTextStyle(font_family="Sans"),
    )

    renderer.add_text_line(
        text="StyledPlainText",
        text_style=ParagraphTextStyle(
            font_size=8,
            font_color=Color.from_255(255, 102, 0),
            background_color=Color.from_255(0, 255, 0),
            decorations=[
                ParagraphTextDecorationEnum.UNDERLINED,
            ],
        ),
    )

    renderer.add_text_line(
        text="StyledHeaderText",
        text_style=ParagraphTextStyle(
            style=ParagraphTextStyleEnum.HEADER_5,
            font_size=36,
            font_color=Color.from_255(102, 255, 102),
            decorations=[
                ParagraphTextDecorationEnum.ITALIC,
                ParagraphTextDecorationEnum.BOLD,
            ],
        ),
    )

    renderer.add_text_line(
        text="Header1",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(text="PlainText1")

    renderer.add_text_line(
        text="Header2",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_2),
    )

    renderer.add_text_line(
        text="SubHeader2",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_text_line(text="PlainText2")

    renderer.add_list(lines=["aaa", "bbb", "ccc"])

    renderer.add_text_line(
        text="SubHeader3",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_list(lines=["aaa", "bbb", "ccc"])

    renderer.add_image(
        uri="https://picsum.photos/300/200",
        height=300,
        width=200,
    )

    renderer.add_text_line(
        text="SubHeader4",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.add_table(
        rows=[
            Row(
                cells=[
                    Cell(
                        text="111",
                        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
                    ),
                    Cell(
                        text="222",
                        text_style=ParagraphTextStyle(font_size=6, background_color=Color.from_255(255, 0, 255)),
                        background_color=Color.from_255(0, 255, 0),
                    ),
                ],
            ),
            Row(
                cells=[
                    Cell(
                        text="aaa",
                        merge_right=4,
                        merge_down=5,
                    ),
                ],
            ),
            Row(
                cells=[
                    Cell(text="bbb"),
                    Cell(
                        text="ccc",
                        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_5),
                    ),
                ],
            ),
            Row(
                cells=[
                    Cell(text="ddd"),
                    Cell(text="eee"),
                ],
            ),
            Row(
                cells=[
                    None,
                    Cell(text="fff"),
                ],
            ),
        ],
    )

    renderer.add_text_line(text="PlainText111")
    renderer.add_text_line(
        text="SubHeader222",
        text_style=ParagraphTextStyle(style=ParagraphTextStyleEnum.HEADER_3),
    )

    renderer.save()
