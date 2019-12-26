__all__ = [
    "home",
    "cdn",
    "media",
    "api",
    "gateway",
    "wss",
    "gg",
    "invite",
    "devs",
    "oauth2",
    "webhooks",
    "emoji",
    "guild_icon",
    "guild_splash",
    "guild_banner",
    "default_pfp",
    "user_pfp",
    "app_icon",
    "app_asset",
    "chat",
    "webhook",
    "team_pfp",
    "achievement"
]

global home, cdn, media, api, gateway, wss
global gg, invite, devs, oauth2, webhooks
home = "https://discordapp.com"
cdn = "https://cdn.discordapp.com"
media = "https"
api = f"{home}/api/v7"
gateway = f"{home}/api/gateway"
wss = "wss://gateway.discord.gg/?v=6&encoding=json"
gg = "https://discord.gg"
invite = f"{home}/invite"
devs = f"{home}/developers"
oauth2 = f"{home}/api/oauth2"
webhooks = f"{home}/api/webhooks"

def emoji(id, fmt = 'png'):
    global cdn
    return f"{cdn}/emojis/{id}.{fmt}"

def guild_icon(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/icons/{id}/{hash}.{fmt}"

def guild_splash(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/splashes/{id}/{hash}.{fmt}"

def guild_banner(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/banners/{id}/{hash}.{fmt}"

def default_pfp(discrim):
    global cdn
    return f"{cdn}/embed/avatars/{int(discrim) % 5}.png"

def user_pfp(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/avatars/{id}/{hash}.{fmt}"

def app_icon(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/app-icons/{id}/{hash}.{fmt}"

def app_asset(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/app-assets/{id}/{hash}.{fmt}"

def achievement(id, hash, other, fmt = 'png'):
    global cdn
    return f"{cdn}/app-assets/{id}/achievements/{other}/icons/{hash}.{fmt}"

def team_pfp(id, hash, fmt = 'png'):
    global cdn
    return f"{cdn}/team-icons/{id}/{hash}.{fmt}"

def webhook(id, token):
    global webhooks
    return f"{webhooks}/{id}/{token}"

def chat(gID = "@me", cID = None, tID = None):
    global home
    url = f"{home}/{gID}"
    if cID and gID != "@me":
        url = f"{url}/{cID}"
        if tID:
            url = f"{url}/{tID}"
    return url
