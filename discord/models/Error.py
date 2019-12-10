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
    DESCRIPTION ---
        Base class for all exceptions, shows attempts taken, args, and kwargs
    """
    def __init__(self, name = "UnknownError", attempts = "None",
                 typ = "PrizmaticError", *args, **kwargs):
        self.name = name.strip()
        self.attempts = attempts.strip()
        self.other_info = args
        self.specific_info = kwargs
        self.typ = typ.strip() + " "

    def __str__(self):
        return f"""\
{self.typ} ---
{self.name}

ATTEMPTS TAKEN ---
{self.attempts}

OTHER INFO ---
{fmt(self.other_info)}

SPECIFIC INFO ---
{fmt(self.specific_info)}
"""

class ClassError(Error):
    """
    DESCRIPTION ---
        A much more specific TypeError
    """
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
    """
    DESCRIPTION ---
        Warns about a bad URL
    """
    def __init__(self, url):
        super.__init__(
            name = "Bad url given",
            typ = "URLError",
            url = url
        )

class SnowDecodeError(Error):
    """
    DESCRIPTION ---
        Warns about a malformed snowflake
    """
    def __init__(self, snowflake):
        super.__init__(
            name = "Bad snowflake given",
            typ = "SnowDecodeError",
            attempts = "Tried converting from str, hex, and binary",
            snowflake = snowflake
        )

class LoginError(Error):
    """
    DESCRIPTION ---
        Is thrown upon login failure
    """
    def __init__(self, code, j):
        super.__init__(
            name = "Bad login info given",
            typ = "LoginError",
            attempts = "Stripped space characters from token",
            reponse = j,
            status_code = code
        )

class InputError(Error):
    """
    DESCRIPTION ---
        Is thrown when a command gets bad input
    """
    def __init__(self, obj, reqd):
        super.__init__(
            name = "Bad argument or input",
            given = obj,
            allowed = reqd
        )

class ForbiddenError(Error):
    """
    DESCRIPTION ---
        Is thrown upon a 403 response
    """
    def __init__(self, code, j):
        super.__init__(
            name = "Client is forbidden to do an action",
            typ = "ForbiddenError",
            response = j,
            status_code = code
        )
