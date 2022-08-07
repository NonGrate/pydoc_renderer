from doc_renderer.color import Color
from doc_renderer.paragraph_text_style import ParagraphTextStyle


class Cell:
    text: str
    merge_right: int
    merge_down: int
    text_style: ParagraphTextStyle
    background_color: Color

    def __init__(
            self,
            text: str,
            merge_right: int = 1,
            merge_down: int = 1,
            background_color: Color = None,
            text_style: ParagraphTextStyle = ParagraphTextStyle(),
    ):
        self.text = text
        self.merge_right = merge_right
        self.merge_down = merge_down
        self.background_color = background_color
        self.text_style = text_style


class Row:
    cells: list[Cell]

    def __init__(
            self,
            cells: list[Cell]
    ):
        self.cells = cells
