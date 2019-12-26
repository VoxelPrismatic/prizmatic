from pprint import pformat as fmt

__all__ = [
    "typed",
    "Error",
    "ClassError",
    "LoginError",
    "URLError",
    "SnowDecodeError",
    "InputError"
]

def typed(thing):
    if type(thing) == type:
        return str(thing).split("'")[1]
    return str(type(thing)).split("'")[1]

class Error(Exception):
    """
    {{cls}} error = Error(name, attempts, typ, *args, **kwargs)

    {{desc}} Represents the base error class

    {{param}} name [Any]
        Name of the error, `TypeError: Type 'thing' cannot be converted into
        type 'thing'`

    {{param}} attempts [Any]
        Attempted fixes or ways to prevent the error

    {{param}} typ [Any]
        The type of error eg TypeError or PrizmaticError

    {{param}} *args [args]
        A list of other info

    {{param}} **kwargs [kwargs]
        A dict of slightly more specific info
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
{self.typ} ---
{self.name}

ATTEMPTED FIXES ---
{self.attempts}

OTHER INFO ---
{fmt(self.other_info)}

SPECIFIC INFO ---
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

class LoginError(Error):
    def __init__(self, code, j):
        super.__init__(
            name = "Bad login info given",
            typ = "LoginError",
            attempts = "Stripped space characters from token",
            reponse = j,
            status_code = code
        )

class InputError(Error):
    def __init__(self, obj, reqd):
        super.__init__(
            name = "Bad argument or input",
            typ = "InputError",
            given = obj,
            allowed = reqd
        )

class ObjNotFoundError(Error):
    def __init__(attempts, looking_for):
        super.__init__(
            name = "Object not found",
            typ = "ObjNotFoundError",
            attempts = attempts,
            looking_for = looking_for
        )
