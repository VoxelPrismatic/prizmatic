import re
import typing

__all__ = [
    "Color",
    "Colour"
    "get_color",
    "grab_color",
    "get_colour",
    "grab_colour"
]

class Color:
    """
    {{cls}} instance = Color(int_color, rgb_color, hex_color)

    {{desc}} Represents a color... yes thats it

    {{note}} An alias for this class exists under `Colour`

    {{param}} int_color [Optional[int]]
        The integer representation of the number

    {{param}} rgb_color [Optional[tuple]]
        R, G, and B color values in a tuple

    {{param}} hex_color [Optional[str]]
        The hexadecimal color. Must start with a #

    {{prop}} hex [str]
        The hex color

    {{prop}} num [int]
        The actual int color

    {{prop}} rgb [tuple]
        The RGB tuple
    """
    def __init__(self, int_color: typing.Optional[int] = -1,
                 rgb_color: typing.Optional[tuple] = (-1, -1, -1),
                 hex_color: typing.Optional[str] = "#"):
        if int_color != -1:
            if int_color > 0xffffff or int_color < 0:
                raise ValueError("Invalid color value for `int_color`")
            self.color = int_color
        elif rgb_color != (-1, -1, -1):
            if any(color < 0 or color > 255 for color in rgb_color):
                raise ValueError("Invalid color value for `rgb_color`")
            r, g, b = rgb_color
            self.color = r << 16 | g << 8 | b
        elif hex_color != "#":
            if re.search(r"^\#[A-Fa-f0-9]{6}$", hex_color):
                self.color = int(hex_color[1:], 16)
            elif re.search(r"^\#[A-Fa-f0-9]{3}$", hex_color):
                hex_color = re.sub(r"\#(.)(.)(.)", r"#\1\1\2\2\3\3", hex_color)
                self.color = int(hex_color[1:], 16)
            else:
                raise ValueError("Invalid color value for `hex_color`")
        else:
            self.color = 0

    def __str__(self):
        """
        {{fn}} str(instance)

        {{desc}} Return the hex color of the class

        {{rtn}} [str] The color
        """
        return f"#{self.color:06x}"

    def __int__(self):
        """
        {{fn}} int(instance)

        {{desc}} Return the int color of the class

        {{rtn}} [int] The int color
        """
        return self.color

    def __tuple__(self):
        """
        {{fn}} tuple(instance)

        {{desc}} Return the RGB tuple of the color

        {{rtn}} [tuple] The RGB tuple
        """
        return (self.color & 0xff0000, self.color & 0xff00, self.color & 0xff)

    @property
    def hex(self):
        return str(self)

    @property
    def rgb(self):
        return tuple(self)

    @property
    def num(self):
        return self.color


def get_color(obj) -> int:
    """
    {{sepfn}} get_color(obj)

    {{desc}} Returns the color value of an object}

    {{note}} Aliases for this function lie under `grab_color()`. `get_colour()`,
    and `grab_colour()` for my non-fellow brittish m8s

    {{param}} obj [tuple, int, str, Color]
        A color object or color compatible object

    {{rtn}} [int] The int color value
    """
    if type(obj) == Color:
        return int(obj)
    elif type(obj) == int:
        if obj < 0 or obj > 0xffffff:
            raise ValueError("Invalid int color")
        return int
    elif type(obj) == list and len(obj) == 3:
        if any(color < 0 or color > 255 for color in obj):
            raise ValueError("Invalid rgb tuple")
        return int("".join(f"{c:02x}" for c in obj), 16)
    elif type(obj) == str:
        if re.search(r"^\#[A-Fa-f0-9]{6}$", obj):
            return int(obj[1:], 16)
        if re.search(r"^\#[A-Fa-f0-9]{3}$", obj):
            return int(re.sub(r"\#(.)(.)(.)", r"\1\1\2\2\3\3", obj), 16)
        raise ValueError("Invalid color value for `hex_color`")
    raise ValueError("Invalid color")

grab_color = get_color
get_colour = get_color
grab_colour = get_color
Colour = Color
