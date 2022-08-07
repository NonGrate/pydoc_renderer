from enum import Enum

from doc_renderer.color import Color


class ParagraphTextStyleEnum(Enum):
    HEADER_1 = "HEADING_1"
    HEADER_2 = "HEADING_2"
    HEADER_3 = "HEADING_3"
    HEADER_4 = "HEADING_4"
    HEADER_5 = "HEADING_5"
    HEADER_6 = "HEADING_6"
    NORMAL_TEXT = "NORMAL_TEXT"


class ParagraphTextDecorationEnum(Enum):
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    UNDERLINED = "UNDERLINED"


class ParagraphTextStyle:
    style: ParagraphTextStyleEnum = None
    decorations: list[ParagraphTextDecorationEnum] = None
    font_size: int = None
    font_color: Color = None
    background_color: Color = None

    def __init__(
            self,
            font_size: int = None,
            font_color: Color = None,
            background_color: Color = None,
            style: ParagraphTextStyleEnum = ParagraphTextStyleEnum.NORMAL_TEXT,
            decorations: list[ParagraphTextDecorationEnum] = None,
    ):
        self.style = style
        self.decorations = decorations or []
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color

    def __str__(self) -> str:
        return f'ParagraphTextStyle(style: {self.style}, decorations: {self.decorations}, ' \
               f'fontSize: {self.font_size}, fontColor: {self.font_color}, backgroundColor: {self.background_color}) '
