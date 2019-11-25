import re

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
    """

    def __init__(self, num: int = 0):
        self.color = num

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.color = int(hexx(r) + hexx(g) + hexx(b), 16)

    def __init__(self, hx: str = "0x000000"):
        if not re.search(r"^(0x|\#)?[0-9a-fA-F]{6}$"):
            raise ValueError
        self.color = int(hx.replace("0x", "").replace("#", ""), 16)

    def __init__(self, rgb: tuple = (0, 0, 0)):
        r, g, b = rgb
        self.color = int(hexx(r) + hexx(g) + hexx(b), 16)

    def __str__(self):
        return hex(self.color).replace("0x", "#")
    
    def __int__(self):
        return self.color

def grab_color(obj):
    if type(obj) == Color:
        return int(color)
    else:
        return int(Color(color))
