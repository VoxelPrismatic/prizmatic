from ..Role import Role
from ..Member import User
from ..PrizmCls import PrizmList
from ..Perms import Perms, Overwrite
from ..ClsUtil import from_ts, extra_kw
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["DM"]

class DM:
    """
    {{cls}} instance = DM(*, last_message_id, type, id, recipients, bot_obj)

    {{desc}} Represents a dm channel

    {{noinit}}

    {{notdone}}

    {{note}} The documentation for this class is not complete yet

    {{param}} last_message_id [int, ~/Snow, str]
        The ID of the latest message

    {{param}} type [int]
        This should always be 1

    {{param}} id [int, ~/Snow, str]
        The ID of the channel

    {{param}} recipients [List[dict]]
        A list of users in this DM, this should be the client, and the person
        the bot is talking to

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} latest_text_id [int]
        The ID of the latest message

    {{prop}} type [int]
        This should always be 1 unless you change it

    {{prop}} id [int]
        The ID of the channel

    {{prop}} users [List[~/Member.User]]
        A list of users in this DM
    """
    def __init__(self, *, last_message_id, type, id, recipients, bot_obj, **kw):
        extra_kw(kw, "DM")
        self.latest_text_id = int(last_message_id)
        self.type = type
        self.id = int(id)
        self.users = bot_obj.raw("users", recipients, bot_obj = bot_obj)
        self.bot_obj = bot_obj
