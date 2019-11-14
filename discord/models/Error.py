class PrizmaticError(Exception):
    def __init__(self, name, attempts = "None", typ = "PrizmaticError", *args, **kwargs):
        self.name = name
        self.attempts = attempts
        self.other_info = args
        self.specific_info = kwargs
        self.typ = typ
        
    def __str__(self):
        return f"""\
{self.typ}: {self.name}
Attempts taken to prevent exception: {self.attempts}
Other info given: {self.other_info}
Specific info: {self.specific_info}
"""