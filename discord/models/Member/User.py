import io
import re
from base64 import b64encode as b64e
from .. import Url
from ..Raw import RawFile
from ..Error import InputError
from ..ClsUtil import extra_kw
from ..PrizmCls import PrizmList

__all__ = ["User"]

class User:
    """
    DESCRIPTION ---
        Represents a non-guild player

    PARAMS ---
        This class shouldn't be initalized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, id, username, discriminator, avatar, bot = False,
                 mfa_enabled = False, locale = None, verified = None,
                 email = None, flags = 0, premium_type = 0, bot_obj = None,
                 **kw):
        extra_kw(kw, "User")
        self.id = id
        self.name = username
        self.discrim = discriminator
        self.pfp_hash = avatar
        self.bot = bot
        self.mfa = mfa_enabled
        self.language = locale
        self.email = email
        self.flags_int = flags
        self.flags = []
        bin_flags = f"{flags:011b}"
        self.bot_obj = bot_obj
        all_flags = [
            "Discord Employee",
            "Discord Partner",
            "HypeSquad Events",
            "Bug Hunter",
            "House Bravery",
            "House Brilliance",
            "House Balance",
            "Early Supporter",
            "Team User"
        ]
        for flag in range(len(bin_flags)):
            if bin_flags[flag] == "1":
                self.flags.append(all_flags[flag])

        self.nitro = ""
        if premium_type == 1:
            self.nitro = "Nitro Classic"
        elif premium_type == 2:
            self.nitro = "Nitro"
        self.nitro_type = premium_type

    @property
    def pfp(self):
        self.pfp = Url.user_pfp(id, self.pfp_hash)

    async def edit(self, name = None, pfp = None):
        if type(pfp) == str:
            if re.search(r"^https?\://.*\.(png|jpeg|jpg|gif)$", pfp):
                pfp = await (RawFile(pfp)).get()
            else:
                try:
                    pfp = open(pfp, "rb")
                except FileNotFoundError:
                    raise InputError(
                        pfp, ["URL", RawFile, bytes, io.BytesIO, "name of file"]
                    )
        elif type(pfp) == RawFile:
            pfp = pfp.get()
        elif type(pfp) not in [bytes, io.BytesIO]:
            raise InputError(
                pfp, ["URL", RawFile, bytes, io.BytesIO, "name of file"]
            )
        user = await self.bot_obj._http(
            m = "/",
            d = {
                "username": name,
                "avatar": b64e(bytes(pfp))
            }
        )
        self.__init__(**user, bot_obj = self.bot_obj)
