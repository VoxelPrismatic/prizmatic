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
    {{loc}} discord.models.Audit

    {{cls}} instance = AuditLog(*, too_many_args_to_list_here)

    {{desc}} Represents an audit log

    {{noinit}}

    {{param}} webhooks [List[dict]]
        A list of webhooks

    {{param}} users [List[dict]]
        A list of users that are in the audit log

    {{param}} audit_log_entries [List[dict]]
        A list of events

    {{param}} integrations [List[dict]]
        A list of integrations

    {{param}} bot_obj [~/Bot]
        The bot object
        {{optn}}

    {{prop}} webhooks [List[~/Webhook, dict]]
        A list of webhooks if `bot_obj` is not `None`, otherwise a list of
        raw webhooks

    {{prop}} users [List[~/Member.User, dict]]
        A list of users if `bot_obj` is not `None`, otherwise a list of
        raw users

    {{prop}} events [List[~.AuditEvent]]
        A list of events

    {{prop}} integrations [List[~/Semi.SemiIntegration, dict]]
        A list of integrations if `bot_obj` is not `None`, otherwise a list of
        raw integrations

    {{prop}} bot_obj [~/Bot, None]
        The bot object
    """
    def __init__(self, *, webhooks, users, audit_log_entries, integrations,
                 bot_obj = None):
        self.webhooks = webhooks
        self.users = users
        self.events = [AuditEvent(**entry) for entry in audit_log_entries]
        self.integrations = integrations
        if bot_obj:
            self.webhooks = bot_obj.raw("webhooks", webhooks, bot_obj = bot_obj)
            self.users = bot_obj.raw("users", users, bot_obj = bot_obj)
            self.integrations = bot_obj.raw(
                "integrations", integrations, bot_obj = bot_obj
            )
        self.bot_obj = bot_obj

    def __getitem__(self, key):
        """
        {{bltin}} instance.__getitem__(key)
        {{usage}} instance[key]

        {{desc}} Either returns a ~.AuditEvent or a ~.AuditSearch object

        {{param}} key [int, str, ~/Member.User]
            If `int`, then it will return that index in `instance.events` or it
            will filter by user ID if it is a user ID
            If `str`, then it will filter the events to that event type or by
            user ID if it is a user ID
            If `User`, then it will filter by that user

        {{rtn}} [~.AuditSearch] The filtered events if `key` is a User, user ID,
        or str
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
        return AuditSearch(ls)

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "webhooks": [dict(webhook) for webhook in self.webhooks],
            "users": [dict(user) for user in self.users],
            "audit_log_entries": [dict(event) for event in self.events],
            "integrations": [dict(integrate) for integrate in self.integrations]
        }
