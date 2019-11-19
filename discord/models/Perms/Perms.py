from .PrizmCls import PrizmList, PrizmDict
global permissions
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
    "CREATE_INSTANT_INVITE": 0x00000001
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
    DESCRIPTION ---
        Represents the permissions of a member, user, or overwrite
    
    PARAMS ---
        allow [int]
        - The allowed things, as an int
        
        deny [int]
        - The denied things, as an int
        
        none [int]
        - The inherited things, as an int
        
        *Use the encode method to create an int from a list of perms
        
    FUNCTIONS ---
        perms = Perms(allow, deny, none)
        - Creates a Perms object
        
        dict(perms)
        - Creates a dict object and returns it
        
        perms.update(other_dict)
        - Updates `perms' with the values of other_dict
        
        perms.update_int(?allow, ?deny, ?none)
        - Updates `perms' with the specified ints
        
        perms.is_empty()
        - Returns `True' if the perms do absolutely nothing
        
        perms[perm]
        - Returns the value of that perm
        
        perms[perm] = val
        - Updates perm to be True [allow], False [deny], or None [none]
    """
    def __init__(self, allow = 0, deny = 0, none = 0):
        self.override_type = type
        self.allow = decode_perms(allow)
        self.allow_int = allow
        self.deny = decode_perms(deny)
        self.deny_int = deny
        self.none = PrizmList([])
        for perm in decode_perms(int(0xffffffff)):
            if perm not in self.allow and perm not in self.deny:
                self.none <= perm
        self.none_int = encode_perms(self.none)

    def __dict__(self):
        dic = {}
        for perm in self.allow:
            dic[perm] = True
        for perm in self.deny:
            dic[perm] = False
        for perm in self.none:
            dic[perm] = None
        return dic

    def update(self, other: dict):
        for key in other:
            key2 = key.upper().replace(" ", "_")
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
        self.none_int = encode_perms(self.none)
        self.allow_int = encode_perms(self.allow)
        self.deny_int = encode_perms(self.deny)

    def update_int(self, allow = None, deny = None, none = None):
        self.allow_int = allow if allow is not None else self.allow_int
        self.deny_int = deny if deny is not None else self.deny_int
        self.none_int = none if none is not None else self.none_int
        self.none = decode(none)
        self.deny = decode(deny)
        self.allow = decode(allow)

    def is_empty(self):
        if all(i == None for i in self.none) \
           and all(i == None for i in self.deny) \
           and all(i == None for i in self.allow):
               return True
        return False
    
    def __getitem__(self, key):
        return dict(self)[key.upper().replace(" ", "_")]
        
    def __setitem__(self, key, val):
        self.set({key: val})
    
    def decode(num: int):
        return decode_perms(num)

    def encode(ls: list):
        return encode_perms(ls)