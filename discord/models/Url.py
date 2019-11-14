class Url:
    """
    DESCRIPTION ---
        Provides many URLs for things
        
    PARAMS ---
        None
        
    FUNCTIONS ---
        None
    def init(self):
        home = "https://discordapp.com"
        self.home = home
        self.cdn = "https://cdn.discordapp.com"
        self.media = "https"
        self.api = f"{home}/api/v7"
        self.gateway = f"{home}/api/gateway"
        self.wss = "wss://gateway.discord.gg/?v=6&encoding=json"
        self.gg = "https://discord.gg"
        self.invite = f"{home}/invite"
        self.devs = f"{home}/developers"
        self.oauth2 = f"{home}/api/oauth2"
        self.webhooks = f"{home}/api/webhooks"
        del home
    def emoji(self, id, fmt = 'png'):
        return f"{self.cdn}/emojis/{id}.{fmt}"
    def guild_icon(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/icons/{id}/{hash}.{fmt}"
    def guild_splash(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/splashes/{id}/{hash}.{fmt}"
    def guild_banner(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/banners/{id}/{hash}.{fmt}"
    def default_pfp(self, discrim):
        return f"{self.cdn}/embed/avatars/{discrim}.png"
    def user_pfp(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/avatars/{id}/{hash}.{fmt}"
    def app_icon(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/app-icons/{id}/{hash}.{fmt}"
    def app_asset(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/app-assets/{id}/{hash}.{fmt}"
    def achievement(self, id, hash, other, fmt = 'png'):
        return f"{self.cdn}/app-assets/{id}/achievements/{other}/icons/{hash}.{fmt}"
    def team_pfp(self, id, hash, fmt = 'png'):
        return f"{self.cdn}/team-icons/{id}/{hash}.{fmt}"
    def webhook(self, id, token):
        return f"{self.webhooks}/{id}/{token}"
    def chat(self, gID = "@me", cID = None, tID = None):
        url = f"{self.home}/{gID}"
        if cID and gID != "@me":
            url = f"{url}/{cID}"
            if tID:
                url = f"{url}/{tID}"
        return url