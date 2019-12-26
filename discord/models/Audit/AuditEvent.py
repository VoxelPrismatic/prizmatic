from .AuditChange import AuditChange

__all__ = ["AuditEvent", "audit_actions"]

audit_actions = {
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
    81: "integration_edit"
}

class AuditEvent:
    """
    {{cls}} instance = AuditEvent(*, too_many_args_to_list_here)

    {{desc}} Represents an audit log event

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{param}} target_id [str, discord.models.Snow, int]
        The target ID, eg a role ID or a channel ID

    {{param}} changes [list]
        A list of applied changes

    {{param}} user_id [str, discord.models.Snow, int]
        The user ID that made the change

    """
    def __init__(self, target_id, changes = [], user_id = 0, id = 0,
                 action_type = 0, options = {}, reason = ""):
        self.target_id = int(target_id)
        self.event_id = int(id)
        self.changes = [AuditChange(**d) for d in changes]
        self.user_id = int(user_id)
        self.action = audit_actions[action_type]
        self.other_info = options
        self.reason = reason
