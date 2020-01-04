from ..Semi import SemiUser
from ..ClsUtil import extra_kw

__all__ = ["Invite"]

class Invite:
    """
    {{cls}} instance = Invite(*, too_many_args_to_list_here)

    {{desc}} Represents an invite

    {{noinit}}

    {{param}} code [str]
        Invite code, eg `ZM84Nm6n`

    {{param}} guild [dict]
        The guild object

    {{param}} channel [dict]
        The channel object

    {{param}} target_user [dict]
        The targeted user

    {{param}} target_user_type [int]
        I honestly do not know

    {{param}} approximate_presence_count [int]
        Rough number of statuses

    {{param}} approximate_member_count [int]
        Rough number of players

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} code [str]
        Invite code, eg `ZM84Nm6n`

    {{prop}} guild_id [int]
        The guild ID

    {{prop}} guild [~/Guild]
        The guild object

    {{prop}} channel_id [int]
        The channel ID

    {{prop}} channel [~/Channel.AnyChannel]
        The channel object

    {{prop}} target [~/Semi.SemiUser]
        The target user

    {{prop}} target_type [int]
        I honestly do not know

    {{prop}} rough_status_count [int]
        Rough number of statuses

    {{prop}} rough_player_count [int]
        Rough number of players

    {{prop}} bot_obj [~/Bot]
        The bot object
    """
    def __init__(self, *, code, guild, channel, target_user, target_user_type,
                 approximate_presence_count, approximate_member_count,
                 bot_obj = None, **kw):
        extra_kw(kw, "Invite")
        self.code = code
        self.url = "https://discord.gg/" + code
        self.target = SemiUser(**self.target_user)
        self.target_type = self.target_user_type
        self.rough_status_count = approximate_presence_count
        self.rough_player_count = approximate_member_count
        self.bot_obj = bot_obj
        self.guild_id = guild["id"]
        self.channel_id = channel["id"]
        bot_obj.listener.invites[code] = self

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    @property
    def channel(self):
        return self.bot_obj.all_channels(self.channel_id)

    async def delete(self):
        """
        {{fn}} await instance.delete()

        {{desc}} Deletes this object and the invite

        {{note}} This does NOT return a ~/NonExistentObj after deletion because
        Discord creates a random invite code
        """
        await self.bot_obj.http.req(m = "-", u = f"/invites/{self.code}")
        del self.bot_obj.listener.invites[self.code]
        del self

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "code": self.code,
            "guild": dict(self.guild),
            "channel": dict(self.channel),
            "target_user": dict(self.target),
            "target_user_type": self.target_type,
            "approximate_member_count": self.rough_player_count,
            "approximate_presence_count": self.rough_status_count
        }
