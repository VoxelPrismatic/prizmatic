from ..Member import User
from ..Role import Role
from ..Error import ClassError

__all__ = ["Status"]

class Status:
    """
    {{cls}} instance = Status(*, too_many_args_to_list_here)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a presence, or "status" as referred to in the UI

    {{param}} user [dict, discord.models.User]
        The user that has this status

    {{param}} roles [List[dict], List[dicord.models.Role]]
        A list of roles that the user has

    {{param}} guild_id [str, discord.models.Snow]
        The guild ID

    {{param}} status [str]
        Their "online" status, eg "Online" or "Do not Disturb"

    {{param}} activites [List[dict], List[discord.models.Status.Actitivites

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, user, roles, game, guild_id, status, activities,
                 client_status, bot_obj):
        if type(user) == dict:
            self.user = bot_obj.raw("users", user, bot_obj = bot_obj)
        elif type(user) == User:
            self.user = user
        else:
            raise ClassError(user, ["discord.models.User", "dict"])
        self.user = User(**user)
        self.roles = bot_obj.find_list(
            "roles",
            roles,
            f"/guilds/{guild_id}/roles/",
            bot_obj = bot_obj
        )
        self.status = status
        self.text = activities
