from .Semi import SemiIntegration
from .ClsUtil import from_ts

__all__ = ["Integration"]

class Integration:
    """
    {{cls}} instance = Integration(*, too_many_args_to_list_here)

    {{desc}} Represents an integration, or partial integration if only some
    params are passed

    {{noinit}}

    {{note}} The documentation for this class is not complete yet

    {{param}} id [int, discord.models.Snow, str]
        ID of this integration

    {{param}} name [str]
        Name of this integration

    {{param}} account [dict]
        Account containing name and id

    {{param}} enabled [bool]
        Whether or not this integration is enabled

    {{param}} syncing [bool]
        Whether or not this integration is being synced

    {{param}} role_id [int, discord.models.Snow, str]
        The role ID

    {{param}} expire_behavior [int]
        The behaviour of expiring subscribers

    {{param}} expire_grace_period [int]
        The grace period before expiring subscribers

    {{param}} user [dict]
        User for this object

    {{param}} synced_at [str, datetime.datetime]
        When this integration was last synced

    {{}}
    """
    def __init__(self, *, id, name, type, account, enabled = None,
                 syncing = None, role_id = None, expire_behavior = None,
                 expire_grace_period = None, user = None, synced_at = None,
                 bot_obj = None):
        semi_obj = True
        for attr in [
            enabled, syncing, role_id, expire_behavior, expire_grace_period,
            user, synced_at
        ]:
            if attr is not None:
                semi_obj = False
        if semi_obj:
            return SemiIntegration(
                id = id, name = name, type = type, account = account,
                bot_obj = bot_obj
            )
        self.id = int(id)
        self.name = name
        self.type = type
        self.account = account
        self.enabled = enabled
        self.syncing = syncing
        self.role_id = int(role_id)
        self.expire_behavior = expire_behavior
        self.expire_grace_period = expire_grace_period
        self.user = user
        self.synced_at = from_ts(synced_at)
        if bot_obj:
            self.user = bot_obj.raw("users", user, bot_obj = bot_obj)
        self.bot_obj = bot_obj

    @property
    def expire_behaviour(self):
        return self.expire_behavior

    @property
    def role(self):
        return self.bot_obj.roles(self.role_id)
