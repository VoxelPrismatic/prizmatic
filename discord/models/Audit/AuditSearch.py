import re
from ..Error import ClassError
from ..Member import User

__all__ = ["AuditSearch"]

class AuditSearch:
    """
    {{loc}} discord.models.Audit
    {{cls}} instance = AuditSearch(events)

    {{desc}} Represents an audit log search

    {{noinit}}

    {{param}} events [List[~.AuditEvent]]
        List of events

    {{prop}} events [List[~.AuditEvent]]
    """
    def __init__(self, events):
        self.events = events

    def __getitem__(self, key):
        """
        {{bltin}} instance.__getitem__(key)
        {{usage}} instance[key]

        {{desc}} Either returns a ~.AuditEvent or a ~.AuditSearch object

        {{param}} key [int, str, discord.models.Member.User]
            If `int`, then it will return that index in `instance.events` or it
            will filter by user ID if it is a user ID
            If `str`, then it will filter the events to that event type or by
            user ID if it is a user ID
            If `User`, then it will filter by that user

        {{rtn}} [~.AuditSearch] The filtered events if `key`
        is a User, user ID, or str
        {{rtn}} [~.AuditEvent] The event if `key` is an index
        """
        if type(key) == int:
            if len(str(key)) < 15:
                return self.events[key]
        elif type(key) == str:
            if not re.search(r"^\d{20}$", str(key)):
                ls = []
                for evt in self.events:
                    if evt.action == key:
                        ls.append(evt)
                return AuditSearch(ls)
        elif type(key) == User:
            key = int(key)
        else:
            raise ClassError(key, str, [int, str, User])
        ls = []
        for evt in self.events:
            if evt.user_id == key:
                ls.append(evt)
        return self.__class__(ls)
