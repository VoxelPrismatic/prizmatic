import re

__all__ = ["hexx", "Color", "get_color", "grab_color"]

def hexx(num, fill = 2):
    return hex(num)[2:].zfill(fill)

class Color:
    """
    DESCRIPTION ---
        Represents a color... yes thats it

    PARAMS---
        ?num [int]
        - The integer representation of the hexadecimal color

        ?rgb [tuple]
        - The (r, g, b) values of the color

        ?r [int]
        - The r value of the color

        ?g [int]
        - The g value of the color

        ?b [int]
        - The b value of the color

        ?hx [str]
        - The hexadecimal representation of the color
        **You should only pass one type of param [(r, g, b), rgb, num, hex] or
          you may not get the desired output

    FUNCTIONS ---
        color = Color(some_color)
        - Creates a Color object

        str(color)
        - Returns the hex representation of the color

        int(color)
        - Alias for color.color, except this is compatible
          with ints as well
    """

    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == int:
            self.color = args[0]
        elif len(args) == 3 and all(type(arg) == int for arg in args):
            r, g, b = args
            self.color = int(hexx(r) + hexx(g) + hexx(b), 16)
        elif len(args) == 1 and len(args[0]) == 3 and all(type(arg) == int for arg in args[0]):
            r, g, b = args[0]
            self.color = int(hexx(r) + hexx(g) + hexx(b), 16)
        elif len(args) == 1 and re.search(r"^(0x|\#)?[0-9a-fA-F]{6}$", str(args[0])):
            self.color = int(args[0].replace("0x", "").replace("#", ""), 16)
        else:
            raise ValueError("Unknown color type")

    def __str__(self):
        return hex(self.color).replace("0x", "#")

    def __int__(self):
        return self.color

def get_color(obj):
    if type(obj) == Color:
        return int(obj)
    else:
        return int(Color(obj))

grab_color = get_color
