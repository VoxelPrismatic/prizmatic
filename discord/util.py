import re

__all__ = ["escape"]

def escape(st):
    """
    {{sepfn}} escape(st)

    {{desc}} Escapes markdown

    {{param}} st [str]
        The string to escape

    {{note}} This function also escapes mentions/pings

    {{rtn}} [str] The escaped string
    """
    st = re.sub(r"([\_\*\~\|\>\`])", r"\\1", st)
    st = re.sub(r"<([\@\#]\&?)(\d+)>", r"<\u200b\1\2>", st)
    st = re.sub(r"<\:([\d\w_]+)\:(\d+)>", r"<\u200b:\1:\2>", st)
    return st
