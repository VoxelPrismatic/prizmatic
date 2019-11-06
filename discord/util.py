import re
def escape(st):
    st = re.sub(r"([\_\*\~\|\>\`])", r"\\1", st)
    st = re.sub(r"<([\@\#])(\d+)>", r"<\u200b\1\2>", st)
    st = re.sub(r"<\:([\d\w_]+)\:(\d+)>", r"<\u200b:\1:\2>", st)
    return st
