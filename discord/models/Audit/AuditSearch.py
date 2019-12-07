import re
from ..Error import ClassError
from ..Member import User

__all__ = ["AuditSearch"]

class AuditSearch:
    """
    DESCRIPTION ---
        Represents an audit log search

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        search = AuditSearch(entries)
        - Creates a new AuditSearch object

        search[index]
        - Get that item

        search[event_type]
        - Get a list of events with that type

        search(user_id)
        - Get a list of events with that user
    """
    def __init__(self, events):
        self.events = events

    def __getitem__(self, i):
        if type(i) == int:
            return self.events[i]
        elif type(i) == str:
            ls = []
            for evt in self.events:
                if evt.action == i:
                    ls.append(evt)
            return self.__class__(self.web, self.user, ls, True)
        else:
            raise ClassError(i, str, [int, str])

    def __call__(self, user):
        if type(user) == User:
            id = user.id
        elif type(user) == int:
            id = user
        elif re.search(r"^\d{20}$", str(user)):
            id = int(user)
        else:
            raise ClassError(user, int, [User, int, str])
        ls = []
        for evt in self.events:
            if evt.user_id == id:
                ls.append(evt)
        return self.__class__(self.web, self.user, ls, True)
