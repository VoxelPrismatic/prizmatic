from ..Semi import SemiUser

class Invite:
    """
    DESCRIPTION ---
        Represents an invite
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
    
    FUNCTIONS ---
        invite = Invite(code, guild, channel, user, type, presences, members)
        - Create a new Invite object
        
        await invite.update()
        - Updates the invite data
        
        await invite.delete()
        - Deletes the invite, and the object
    """
    def __init__(self, code, guild, channel, target_user, target_user_type,
                 approximate_presence_count, approximate_member_count, bot_obj):
        self.code = code
        self.url = "https://discord.gg/"+code
        self.target = SemiUser(**self.target_user)
        self.rough_status_count = approximate_presence_count
        self.rough_player_count = approximate_member_count
        self.bot_obj = bot_obj
        self.guild = bot_obj.listener.guilds[guild["id"]]
        self.channel = bot_obj.listener.channels[channel["id"]]
        bot_obj.listener.invites[code] = self
   
   async def update(self):
       d = await self.bot_obj.http.req(u = f"/invites/{self.code}")
       self.__init__(**d)
       
   async def delete(self):
       await self.bot_obj.http.req(m = "-", u = f"/invites/{self.code}")
       del self.bot_obj.listener.invites[self.code]
       del self