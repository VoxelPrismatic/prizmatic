from .AuditChange import AuditChange
from ..ClsUtil import extra_kw

__all__ = [
    "AuditEvent",
    "audit_actions"
]

#According to Discord Docs
audit_actions = {
    0: "nothing_changed",
    1: "guild_edit",

    10: "channel_make",
    11: "channel_edit",
    12: "channel_delete",
    13: "channel_perms_make",
    14: "channel_perms_edit",
    15: "channel_perms_delete",

    20: "player_kick",
    21: "player_prune",
    22: "player_ban",
    23: "player_unban",
    24: "player_edit",
    25: "player_roles_edit",
    26: "player_move",
    27: "player_disconnect",
    28: "bot_add",

    30: "role_make",
    31: "role_edit",
    32: "role_delete",

    40: "invite_make",
    41: "invite_edit",
    42: "invite_delete",

    50: "webhook_make",
    51: "webhook_edit",
    52: "webhook_delete",

    60: "emoji_make",
    61: "emoji_edit",
    62: "emoji_delete",

    72: "text_delete",
    73: "text_bulk_delete",
    74: "text_pin",
    75: "text_unpin",

    80: "integration_make",
    81: "integration_edit",
}

class AuditEvent:
    """
    {{cls}} instance = AuditEvent(*, too_many_args_to_list_here)

    {{desc}} Represents an audit log event

    {{noinit}}

    {{param}} target_id [str, ~/Snow, int]
        The target ID, eg a role ID or a channel ID
        {{reqd}}

    {{param}} changes [List[dict]]
        A list of applied changes

    {{param}} user_id [str, ~/Snow, int]
        The user ID that made the change

    {{param}} id [str, dis.mod.Snow, int]
        The ID of the audit event

    {{param}} action_type [int]
        Type of action, which somehow has more types than the gateway which is
        mildly infuriating

    {{param}} options [dict]
        Other things

    {{param}} reason [str]
        Reason for those changes

    {{param}} bot_obj [~/Bot]
        The bot object, so you can access it anywhere

    {{prop}} target_id [int]
        The target ID, eg a role ID or a channel ID

    {{prop}} changes [List[~.AuditChange]]
        A list of applied changes

    {{prop}} user_id [int]
        The user ID that made the change

    {{prop}} user [dis.mod.Member.User]

    {{prop}} id [int]
        The ID of the audit event

    {{prop}} action_type [int]
        Type of action, which somehow has more types than the gateway which is
        mildly infuriating

    {{prop}} action [str]
        Type of action, but human readable

    {{prop}} options [dict]
        Other things

    {{prop}} reason [str]
        The reason for those changes

    {{prop}} bot_obj [~/Bot]
        The bot object, so you can access it anywhere
    """
    def __init__(self, *, target_id, changes = [], user_id = 0, id = 0,
                 action_type = 0, options = {}, reason = "", bot_obj = None,
                 **kw):
        extra_kw(kw, "AuditEvent")
        self.target_id = int(target_id)
        self.id = int(id)
        self.changes = [AuditChange(**d) for d in changes]
        self.user_id = int(user_id)
        self.action = audit_actions[action_type]
        self.action_type = action_type
        self.options = options
        self.reason = reason
        self.bot_obj = bot_obj

    @property
    def user(self):
        return self.bot_obj.users(self.user_id)

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        return "<AuditEvent by user ID " + str(self.user_id) + ">"

    def __getitem__(self, index: int):
        """
        {{bltin}} instance.__getitem__(index)
        {{usage}} instance[index]

        {{pydesc}} __getitemL__

        {{param}} index [int]
            That specific change

        {{rtn}} [~.AuditChange] That specific change
        """
        return self.changes[index]

    def __list__(self):
        """
        {{bltin}} instance.__list__()
        {{usage}} list(instance)

        {{desc}} Returns the list of changes

        {{rtn}} [List[~.AuditChange]]
        """
        return self.changes

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "target_id": str(self.target_id),
            "id": str(self.id),
            "changes": [dict(change) for change in self.changes],
            "user_id": str(self.user_id),
            "action_type": self.action_type,
            "options": self.options,
            "reason": self.reason
        }

    def __iter__(self):
        """
        {{bltin}} instance.__iter__()
        {{usage}} iter(instance)

        {{pydesc}} __iter__

        {{rtn}} [generator]
        """
        self.___iter_index___ = -1
        return self

    def __next__(self):
        """
        {{bltin}} instance.__next__()
        {{usage}} for change in instance: #code...

        {{pydesc}} __next__

        {{rtn}} [~.AuditChange] The next event
        """
        self.___iter_index___ += 1
        if self.___iter_index___ < len(self.changes):
            return self.changes[self.___iter_index___]
        raise StopIteration("No more changes")
