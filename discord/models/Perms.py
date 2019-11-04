from .PrizmCls import *

def decode(num: int):
    st = [int(h, 16) for h in hex(num)[2:].zfill(8)]
    ls = PrizmList([])
    dic = {
        "MANAGE_EMOJIS":         (lambda a: [a[0] - 4] + a[1:] if a[0] - 4 >= 0 else a),
        "MANAGE_WEBHOOKS":       (lambda a: [a[0] - 2] + a[1:] if a[0] - 2 >= 0 else a),
        "MANAGE_ROLES":          (lambda a: [a[0] - 1] + a[1:] if a[0] - 1 >= 0 else a),
        "MANAGE_NICKNAMES":      (lambda a: a[:1]+[a[1] - 8]+a[2:] if a[1]-8 >= 0 else a),
        "CHANGE_NICKNAME":       (lambda a: a[:1]+[a[1] - 4]+a[2:] if a[1]-4 >= 0 else a),
        "USE_VAD":               (lambda a: a[:1]+[a[1] - 2]+a[2:] if a[1]-2 >= 0 else a),
        "MOVE_MEMBERS":          (lambda a: a[:1]+[a[1] - 1]+a[2:] if a[1]-1 >= 0 else a),
        "DEAFEN_MEMBERS":        (lambda a: a[:2]+[a[2] - 8]+a[3:] if a[2]-8 >= 0 else a),
        "MUTE_MEMBERS":          (lambda a: a[:2]+[a[2] - 4]+a[3:] if a[2]-4 >= 0 else a),
        "SPEAK":                 (lambda a: a[:2]+[a[2] - 2]+a[3:] if a[2]-2 >= 0 else a),
        "CONNECT":               (lambda a: a[:2]+[a[2] - 1]+a[3:] if a[2]-1 >= 0 else a),
        "USE_EXTERNAL_EMOJIS":   (lambda a: a[:3]+[a[3] - 4]+a[4:] if a[3]-4 >= 0 else a),
        "MENTION_EVERYONE":      (lambda a: a[:3]+[a[3] - 2]+a[4:] if a[3]-2 >= 0 else a),
        "READ_MESSAGE_HISTORY":  (lambda a: a[:3]+[a[3] - 1]+a[4:] if a[3]-1 >= 0 else a),
        "ATTACH_FILES":          (lambda a: a[:4]+[a[4] - 8]+a[5:] if a[4]-8 >= 0 else a),
        "EMBED_LINKS":           (lambda a: a[:4]+[a[4] - 4]+a[5:] if a[4]-4 >= 0 else a),
        "MANAGE_MESSAGES":       (lambda a: a[:4]+[a[4] - 2]+a[5:] if a[4]-2 >= 0 else a),
        "SEND_TTS_MESSAGES":     (lambda a: a[:4]+[a[4] - 1]+a[5:] if a[4]-1 >= 0 else a),
        "SEND_MESSAGES":         (lambda a: a[:5]+[a[5] - 8]+a[6:] if a[5]-8 >= 0 else a),
        "VIEW_CHANNEL":          (lambda a: a[:5]+[a[5] - 4]+a[6:] if a[5]-4 >= 0 else a),
        "STREAM":                (lambda a: a[:5]+[a[5] - 2]+a[6:] if a[5]-2 >= 0 else a),
        "PRIORITY_SPEAKER":      (lambda a: a[:5]+[a[5] - 1]+a[6:] if a[5]-1 >= 0 else a),
        "VIEW_AUDIT_LOG":        (lambda a: a[:6]+[a[6] - 8]+a[7:] if a[6]-8 >= 0 else a),
        "ADD_REACTIONS":         (lambda a: a[:6]+[a[6] - 4]+a[7:] if a[6]-4 >= 0 else a),
        "MANAGE_GUILD":          (lambda a: a[:6]+[a[6] - 2]+a[7:] if a[6]-2 >= 0 else a),
        "MANAGE_CHANNELS":       (lambda a: a[:6]+[a[6] - 1]+a[7:] if a[6]-1 >= 0 else a),
        "ADMINISTRATOR":         (lambda a: a[:7] + [a[7] - 8] if a[7] - 8 >= 0 else a),
        "BAN_MEMBERS":           (lambda a: a[:7] + [a[7] - 4] if a[7] - 4 >= 0 else a),
        "KICK_MEMBERS":          (lambda a: a[:7] + [a[7] - 2] if a[7] - 2 >= 0 else a),
        "CREATE_INSTANT_INVITE": (lambda a: a[:7] + [a[7] - 1] if a[7] - 1 >= 0 else a)
    }
    for perm in dic:
        sta = dic[perm](st)
        if sta != st:
            ls << perm
            st = sta
    return ls

def encode(ls: list):
    st = [0, 0, 0, 0, 0, 0, 0, 0]
    dic = {
        "MANAGE_EMOJIS":         (lambda a: [a[0] + 4] + a[1:]),
        "MANAGE_WEBHOOKS":       (lambda a: [a[0] + 2] + a[1:]),
        "MANAGE_ROLES":          (lambda a: [a[0] + 1] + a[1:]),
        "MANAGE_NICKNAMES":      (lambda a: a[:1]+[a[1] + 8]+a[2:]),
        "CHANGE_NICKNAME":       (lambda a: a[:1]+[a[1] + 4]+a[2:]),
        "USE_VAD":               (lambda a: a[:1]+[a[1] + 2]+a[2:]),
        "MOVE_MEMBERS":          (lambda a: a[:1]+[a[1] + 1]+a[2:]),
        "DEAFEN_MEMBERS":        (lambda a: a[:2]+[a[2] + 8]+a[3:]),
        "MUTE_MEMBERS":          (lambda a: a[:2]+[a[2] + 4]+a[3:]),
        "SPEAK":                 (lambda a: a[:2]+[a[2] + 2]+a[3:]),
        "CONNECT":               (lambda a: a[:2]+[a[2] + 1]+a[3:]),
        "USE_EXTERNAL_EMOJIS":   (lambda a: a[:3]+[a[3] + 4]+a[4:]),
        "MENTION_EVERYONE":      (lambda a: a[:3]+[a[3] + 2]+a[4:]),
        "READ_MESSAGE_HISTORY":  (lambda a: a[:3]+[a[3] + 1]+a[4:]),
        "ATTACH_FILES":          (lambda a: a[:4]+[a[4] + 8]+a[5:]),
        "EMBED_LINKS":           (lambda a: a[:4]+[a[4] + 4]+a[5:]),
        "MANAGE_MESSAGES":       (lambda a: a[:4]+[a[4] + 2]+a[5:]),
        "SEND_TTS_MESSAGES":     (lambda a: a[:4]+[a[4] + 1]+a[5:]),
        "SEND_MESSAGES":         (lambda a: a[:5]+[a[5] + 8]+a[6:]),
        "VIEW_CHANNEL":          (lambda a: a[:5]+[a[5] + 4]+a[6:]),
        "STREAM":                (lambda a: a[:5]+[a[5] + 2]+a[6:]),
        "PRIORITY_SPEAKER":      (lambda a: a[:5]+[a[5] + 1]+a[6:]),
        "VIEW_AUDIT_LOG":        (lambda a: a[:6]+[a[6] + 8]+a[7:]),
        "ADD_REACTIONS":         (lambda a: a[:6]+[a[6] + 4]+a[7:]),
        "MANAGE_GUILD":          (lambda a: a[:6]+[a[6] + 2]+a[7:]),
        "MANAGE_CHANNELS":       (lambda a: a[:6]+[a[6] + 1]+a[7:]),
        "ADMINISTRATOR":         (lambda a: a[:7] + [a[7] + 8]),
        "BAN_MEMBERS":           (lambda a: a[:7] + [a[7] + 4]),
        "KICK_MEMBERS":          (lambda a: a[:7] + [a[7] + 2]),
        "CREATE_INSTANT_INVITE": (lambda a: a[:7] + [a[7] + 1])
    }
    for perm in dic:
        if perm in ls:
            st = dic[perm](st)
    return int("".join(hex(num) for num in st).replace("0x", ""), 16)

class Perms:
    """
    Represents the permission overwrites of a channel
    **You shouldn't have to initialize this class, so no documentation for
      initializing this class will be given
    """
    def __init__(self, allow = 0, deny = 0, none = 0):
        self.override_type = type
        self.allow = decode(allow)
        self.allow_int = allow
        self.deny = decode(deny)
        self.deny_int = deny
        self.none = PrizmList([])
        for perm in decode(int(0xffffffff)):
            if perm not in self.allow and perm not in self.deny:
                self.none <= perm
        self.none_int = encode(self.none)

    def __dict__(self):
        dic = {}
        for perm in self.allow:
            dic[perm] = True
        for perm in self.deny:
            dic[perm] = False
        for perm in self.none:
            dic[perm] = None

    def update(self, other: dict):
        for key in other:
            key2 = key.upper.replace(" ", "_") #because humans are humans, they will most likely
            if other[key] == True:
                if key2 in self.deny:
                    self.deny >> key2
                if key2 in self.none:
                    self.none >> key2
                if key2 not in self.allow:
                    self.allow << key2
            elif other[key] == None:
                if key2 in self.deny:
                    self.deny >> key2
                if key2 not in self.none:
                    self.none << key2
                if key2 in self.allow:
                    self.allow >> key2
            elif other[key] == False:
                if key2 not in self.deny:
                    self.deny << key2
                if key2 in self.none:
                    self.none >> key2
                if key2 in self.allow:
                    self.allow >> key2
        self.none_int = encode(self.none)
        self.allow_int = encode(self.allow)
        self.deny_int = encode(self.deny)

    def update_int(self, allow = self.allow_int deny = self.deny_int, none = self.none_int):
        self.allow_int = allow
        self.deny_int = deny
        self.none_int = none
        self.none = decode(none)
        self.deny = decode(deny)
        self.allow = decode(allow)

    def is_empty(self):
        if all(i == None for i in self.none) \
           and all(i == None for i in self.deny) \
           and all(i == None for i in self.allow):
               return True
        return False
