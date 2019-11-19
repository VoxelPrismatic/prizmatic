from pprint import pformat as fmt

def typed(thing):
    if type(thing) == type:
        return str(thing).split("'")[1]
    return str(type(thing)).split("'")[1]

class Error(Exception):
    """
    Base class for all exceptions
    """
    def __init__(self, name = "UnknownError", attempts = "None", typ = "PrizmaticError",
                 *args, **kwargs):
        self.name = name.strip()
        self.attempts = attempts.strip()
        self.other_info = args
        self.specific_info = kwargs
        self.typ = typ.strip() + " "
        
    def __str__(self):
        return f"""\
{self.typ:-<20}-----
{self.name}

ATTEMPTS TAKEN ----------
{self.attempts}

OTHER INFO --------------
{fmt(self.other_info)}

SPECIFIC INFO -----------
{fmt(self.specific_info)}
"""

class ClassError(Error):
    def __init__(self, clsA, clsB, ls):
        tmp = "', '".join(typed(t) for t in ls)
        super.__init__(
            name = f"Type '{typed(clsA)}' cannot be converted into type '{typed(clsB)}'",
            attempts = f"Tried converting from '{tmp}'",
            typ = "ClassError",
            given_class = clsA,
            target_class = clsB,
            allowed_classes = ls
        )

class URLError(Error):
    def __init__(self, url):
        super.__init__(
            name = "Bad url given",
            typ = "URLError",
            url = url
        )

class SnowDecodeError(Error):
    def __init__(self, snowflake):
        super.__init__(
            name = "Bad snowflake given",
            typ = "SnowDecodeError",
            attempts = "Tried converting from str, hex, and binary",
            snowflake = snowflake
        )

