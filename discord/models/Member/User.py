from .Url import Url
from .Raw import RawFile
from .PrizmCls import PrizmList
from base64 import b64encode as b64e
import io
import re

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
                 mfa_enabled = False, locale, verified = None, email = None,
                 flags, premium_type, bot_obj):
        url = Url()
        self.id = id
        self.name = username
        self.number = discriminator
        self.pfp_hash = avatar
        self.pfp = url.pfp(id, avatar)
        self.pfp_file = RawFile(self.pfp)
        self.bot = bot
        self.mfa = mfa_enabled
        self.language = locale
        self.email = email
        self.flags_int = flags
        self.flags = PrizmList([])
        bin_flags = bin(flags)[2:].zfill(11)
        self.bot_obj = bot_obj
        if bin_flags[0] == "1":
            self.flags << "Discord Employee"
        if bin_flags[1] == "1":
            self.flags << "Discord Partner"
        if bin_flags[2] == "1":
            self.flags << "HypeSquad Events"
        if bin_flags[3] == "1":
            self.flags << "Bug Hunter"
        if bin_flags[6] == "1":
            self.flags << "HypeSquad house Bravery"
        if bin_flags[7] == "1":
            self.flags << "HypeSquad house Brilliance"
        if bin_flags[8] == "1":
            self.flags << "HypeSquad house Balance"
        if bin_flags[9] == "1":
            self.flags << "Early Supporter"
        if bin_flags[10] == "1":
            self.flags << "Team User"
        
        self.nitro = ""
        if premium_type == 1:
            self.nitro = "Nitro Classic"
        elif premium_type == 2:
            self.nitro = "Nitro"
            
            
    async def edit(self, name = self.name, pfp = self.pfp_):
        if type(pfp) == str:
            if re.search(r"^https?\://.*\.(png|jpeg|jpg|gif)$", pfp):
                pfp = await (RawFile(pfp)).get()
            else:
                try:
                    pfp = open(pfp, "rb")
                except FileNotFoundError:
                    raise TypeError("The PFP param must lead to a bytes like object, either through URL, file, or raw")
        elif type(pfp) == RawFile:
            pfp = pfp.get()
        elif type(pfp) not in [bytes, io.BytesIO]:
            raise TypeError("The PFP param must lead to a bytes like object, either through URL, file, or raw")
        user = await self.bot_obj._http(m = "/", d = {"username": name, "avatar": b64e(bytes(pfp))})
        self.__init__(user)
        