__all__ = ["SemiChannel"]
from ..Channel import Category, Channel, DM, GroupDM, NewsChannel, VC,\
    StoreChannel

class SemiChannel:
    """
    {{cls}} instance = SemiChannel(*, name, typ)

    {{desc}} Represents a partial channel object

    {{param} name [str]
        Name of the channel

    {{param}} typ [int, str, class]
        Type of channel
        0, "text", Channel -------> text channel
        1, "dm", DM --------------> direct message
        2, "vc", VC --------------> voice channel
        3, "group", GroupDM ------> group direct message
        4, "category", Category --> category channel
        5, "news", NewsChannel ---> news channel
        6, "store", StoreChannel -> store channel

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} name [str]
        Name of the channel

    {{prop}} type [int]
        Type of the channel
    """
    def __init__(self, *, name, typ):
        if type(typ) == str:
            typ = typ.lower()
        if typ in ["text", 0, Channel]:
            self.type = 0
        elif typ in ["dm", 1, DM]:
            self.type = 1
        elif typ in ["vc", 2, VC]:
            self.type = 2
        elif typ in ["group", 3, GroupDM]:
            self.type = 3
        elif typ in ["category", 4, Category]:
            self.type = 4
        elif typ in ["news", 5, NewsChannel]:
            self.type = 5
        elif typ in ["store", 6, StoreChannel]:
            self.type = 6
        else:
            raise TypeError("`" + str(typ) + "` is not a valid channel type")
        self.name = name

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {"name": self.name, "type": self.type}
