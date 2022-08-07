class Color:
    red: float
    green: float
    blue: float

    def __init__(self, red: float, green: float, blue: float):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_255(cls, red: int, green: int, blue: int):
        return Color(red / 255, green / 255, blue / 255)
