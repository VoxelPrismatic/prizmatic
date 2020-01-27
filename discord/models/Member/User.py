import io
import re
from base64 import b64encode as b64e
from .. import Url
from ..Raw import RawFile
from ..Error import InputError
from ..ClsUtil import extra_kw
from ..PrizmCls import PrizmList
from ..Bitset import Bitset

__all__ = ["User"]

class User:
    """
    {{cls}} instance = User()

    {{desc}} Represents a non-guild player

    {{param}} id [int]
        ID of the user

    {{param}} username [str]
        Name of the user, eg `PRIZ ;]`

    {{param}} discriminator [int]
        The user discriminator eg `9244`

    {{param}} avatar [str]
        The hash of the avatar, this is not a URL

    {{param}} bot [bool]
        Whether or not this user is a bot

    {{param}} mfa_enabled [bool]
        Whether or not the user has 2FA enabled, this will be `False` %N3%

    {{param}} locale [str]
        The language, this will be `None` %N3%

    {{param}} verified [bool]
        Whether or not the user has been verified, this will be `False` %N3%

    {{param}} email [str]
        The user's email, this will be `None` %N3%

    {{param}} flags [int]
        A bitset of flags that the user has

    {{param}} premium_type [int]
        The type of nitro the user has

    {{param}} bot_obj [~/Bot]
        The bot object

    %n3% unless the client has scopes other than "bot"

    {{prop}} id [int]
        The ID of the user

    {{prop}} name [str]
        The name of the user

    {{prop}} discrim [int]
        The user's discriminator
        {{alias}} discriminator

    {{prop}} pfp_hash [str]
        The hash of the PFP

    {{prop}} pfp [str]
        The actual URL of the pfp

    {{prop}} bot [bool]
        Whether or not the user is a bot

    {{prop}} mfa [bool]
        Whether or not the user has 2FA enabled

    {{prop}} locale [str]
        The user's language

    {{prop}} email [str]
        The user's email

    {{prop}} flags [~/Bitset]
        A proper bitset of flags

    {{prop}} nitro [str]
        The nitro name, `"Nitro"` or `"Nitro Classic"`

    {{prop}} nitro_type [int]
        The type of nitro

    {{prop}} bot_obj [~/Bot]
        The bot object
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
        self.locale = locale
        self.email = email
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
        self.flags = Bitset(flags, all_flags)
        self.bot_obj = bot_obj
        self.nitro = ""
        if premium_type == 1:
            self.nitro = "Nitro Classic"
        elif premium_type == 2:
            self.nitro = "Nitro"
        self.nitro_type = premium_type

    @property
    def pfp(self):
        return Url.user_pfp(id, self.pfp_hash)

    @property
    def discriminator(self):
        return self.discrim

    async def edit(self, name = None, pfp = None):
        """
        {{fn}} await instance.edit(name, pfp)

        {{desc}} Edits the user and refreshes the class

        {{note}} All parameters are optional

        {{param}} name [str]
            The new name of the user

        {{param}} pfp [str, file, ~/Raw.RawFile, bytes, io.BytesIO]
        """
        if type(pfp) == str:
            if re.search(r"^https?\://.*\.(png|jpeg|jpg|gif)$", pfp):
                pfp = await (RawFile(pfp)).get()
            else:
                try:
                    pfp = open(pfp, "rb")
                except FileNotFoundError:
                    raise InputError(
                        pfp, [
                            "<url>", RawFile, bytes, io.BytesIO,
                            "<name of file>"
                        ]
                    )
        elif type(pfp) == RawFile:
            pfp = pfp.get()
        elif type(pfp) not in [bytes, io.BytesIO]:
            raise InputError(
                pfp, ["<url>", RawFile, bytes, io.BytesIO, "<name of file>"]
            )
        d = {}
        if name:
            d["username"] = str(name)
        if pfp:
            d["avatar"] = b64e(bytes(pfp))
        if d:
            user = await self.bot_obj._http(
                m = "/",
                d = d
            )
            self.__init__(**user, bot_obj = self.bot_obj)
        return self

    def __str__(self):
        """
        {{bltin}} instance.__str__()
        {{usage}} str(instance)

        {{desc}} Returns the username and discriminator eg `PRIZ ;]#9244`

        {{rtn}} [str]
        """
        return f"{self.name}#{self.discrim:0>4}"

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "id": str(self.id),
            "username": self.name,
            "discriminator": self.discrim,
            "avatar": self.pfp_hash,
            "bot": self.bot,
            "mfa_enabled": self.mfa,
            "locale": self.locale,
            "verified": self.verified,
            "email": self.email,
            "flags": int(self.flags),
            "premium_type": self.nitro_type
        }
