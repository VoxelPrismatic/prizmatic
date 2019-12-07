import re
from .AuditSearch import AuditSearch
from .AuditEvent import AuditEvent
from ..Member import User
from ..Webhook import Webhook
from ..Raw import RawObjs
from ..Error import ClassError

__all__ = ["AuditLog"]

class AuditLog:
    """
    DESCRIPTION ---
        Represents an audit log

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        audit_log = AuditLog(webhooks, users, events)
        - Create a new AuditLog object

        audit_log.make()
        - Fully load the audit log, may take a while depending on
          how many entries, webhooks, and users are in this log

        audit_log[index]
        - Get that specific event

        audit_log[event_type]
        - Filter to that event type

        audit_log(user_id)
        - Filter to that user
    """
    def __init__(self, webhooks, users, audit_log_entries):
        self.webhooks = RawObjs(Webhook, webhooks)
        self.users = RawObjs(User, users)
        self.events = RawObjs(AuditEvent, audit_log_entries)

    def __getitem__(self, i):
        if type(i) == int:
            return self.events[i]
        elif type(i) == str:
            ls = []
            for evt in self.events:
                if evt.action == i:
                    ls.append(evt)
            return AuditSearch(ls)
        else:
            raise ClassError(i, str, [int, str])

    def load(self):
        self.events.make()
        self.webhooks.make()
        self.users.make()
        return self.events

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
        return AuditSearch(ls)
