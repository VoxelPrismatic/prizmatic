from ..PrizmCls import PrizmList, PrizmDict
global permissions

__all__ = ["permissions", "decode_perms", "encode_perms", "Perms"]

permissions = {
    "MANAGE_EMOJIS":         0x40000000,
    "MANAGE_WEBHOOKS":       0x20000000,
    "MANAGE_ROLES":          0x10000000,
    "MANAGE_NICKNAMES":      0x08000000,
    "CHANGE_NICKNAME":       0x04000000,
    "USE_VAD":               0x02000000,
    "MOVE_MEMBERS":          0x01000000,
    "DEAFEN_MEMBERS":        0x00800000,
    "MUTE_MEMBERS":          0x00400000,
    "SPEAK":                 0x00200000,
    "CONNECT":               0x00100000,
    "USE_EXTERNAL_EMOJIS":   0x00040000,
    "MENTION_EVERYONE":      0x00020000,
    "READ_MESSAGE_HISTORY":  0x00010000,
    "ATTACH_FILES":          0x00008000,
    "EMBED_LINKS":           0x00004000,
    "MANAGE_MESSAGES":       0x00002000,
    "SEND_TTS_MESSAGES":     0x00001000,
    "SEND_MESSAGES":         0x00000800,
    "VIEW_CHANNEL":          0x00000400,
    "STREAM":                0x00000200,
    "PRIORITY_SPEAKER":      0x00000100,
    "VIEW_AUDIT_LOG":        0x00000080,
    "ADD_REACTIONS":         0x00000040,
    "MANAGE_GUILD":          0x00000020,
    "MANAGE_CHANNELS":       0x00000010,
    "ADMINISTRATOR":         0x00000008,
    "BAN_MEMBERS":           0x00000004,
    "KICK_MEMBERS":          0x00000002,
    "CREATE_INSTANT_INVITE": 0x00000001,
}

def decode_perms(num: int):
    ls = PrizmList([])
    global permissions
    for perm in permissions:
        val = permissions[perm]
        if (val & num) == val:
            ls << perm
    return list(ls)

def encode_perms(ls: list):
    perms = 0
    global permissions
    for perm in ls:
        perms |= permissions[perm.replace(" ", "_").upper()]
    return perms

class Perms:
    """
    {{cls}} instance = Perms(*, allow, deny, none)

    {{desc}} Represents the permissions of a member, user, or overwrite

    {{param}} allow [int]
        The allowed things, as an int

    {{param}} deny [int]
        The denied things, as an int

    {{note}} Use the encode method to create an int from a list of perms

    {{note}} The documentation for this class is not complete yet
    """
    def __init__(self, allow = 0, deny = 0):
        self.override_type = type
        self.allow_int = allow
        self.deny_int = deny

    @property
    def allow(self):
        return decode_perms(self.allow_int)

    @property
    def deny(self):
        return decode_perms(self.deny_int)

    @property
    def inherit_int(self):
        return abs(~self.allow_int + 1) & abs(~self.deny_int + 1)

    @property
    def inherit(self):
        return decode_perms(self.inherit_int)

    def __dict__(self):
        dic = {}
        for perm in self.allow:
            dic[perm] = True
        for perm in self.deny:
            dic[perm] = False
        for perm in self.inherit:
            dic[perm] = None
        return dic

    def __int__(self):
        return self.allow_int

    def update(self, other: dict):
        deny = self.deny
        allow = self.allow
        for key in other:
            key2 = key.upper().replace(" ", "_")
            if other[key] == True:
                if key2 in deny:
                    deny >> key2
                if key2 not in allow:
                    allow << key2
            elif other[key] == None:
                if key2 in deny:
                    deny >> key2
                if key2 in allow:
                    allow >> key2
            elif other[key] == False:
                if key2 not in deny:
                    deny << key2
                if key2 in allow:
                    allow >> key2
        self.allow_int = encode_perms(allow)
        self.deny_int = encode_perms(deny)

    def update_int(self, allow = None, deny = None):
        self.allow_int = allow if allow is not None else self.allow_int
        self.deny_int = deny if deny is not None else self.deny_int
        self.deny = decode_perms(deny)
        self.allow = decode_perms(allow)

    @property
    def empty(self) -> bool:
        return self.allow_int == 0 and self.deny_int == 0

    def __getitem__(self, key) -> bool:
        return dict(self)[key.upper().replace(" ", "_")]

    def __setitem__(self, key, val):
        self.set({key: val})
