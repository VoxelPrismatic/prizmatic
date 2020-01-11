from ..Member import User
from ..Role import Role
from ..Error import ClassError
from ..ClsUtil import extra_kw

__all__ = ["Status"]

class Status:
    """
    {{cls}} instance = Status(*, too_many_args_to_list_here)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a presence, or "status" as referred to in the UI

    {{param}} user [dict]
        The user that has this status

    {{param}} roles [List[dict]]
        A list of roles that the user has

    {{param}} guild_id [str, ~/Snow, int]
        The guild ID

    {{param}} status [str]
        Their "online" status, eg "Online" or "Do not Disturb"

    {{param}} activites [List[dict]]
        A list of activites

    {{param}} client_status

    {{note}} This class has not been finished yet
    """
    def __init__(self, *, user, roles, game, guild_id, status, activities,
                 client_status, bot_obj = None, **kw):
        extra_kw(kw, "Status")
        if type(user) == dict:
            self.user = bot_obj.raw("users", user, bot_obj = bot_obj)
        elif type(user) == User:
            self.user = user
        else:
            raise ClassError(user, ["User", dict])
        self.user = User(**user)
        self.roles = bot_obj.raw(
            "roles",
            roles,
            bot_obj = bot_obj
        )
        self.status = status
        self.text = activities
