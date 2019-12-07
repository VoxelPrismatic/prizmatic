from .Channel import Channel
from .VC import VC
from .DM import DM
from .StoreChannel import StoreChannel
from .Catagory import Catagory
from .NewsChannel import NewsChannel
from .GroupDM import GroupDM

__all__ = ["AnyChannel"]

def AnyChannel(**kw):
    if "bot_obj" not in kw:
        raise TypeError("Could not find bot object as 'bot_obj' in kw")
    bot = kw["bot_obj"]
    channels = {
        0: (lambda kw: bot.raw(Channel, **kw)),
        1: (lambda kw: bot.raw(DM, **kw)),
        2: (lambda kw: bot.raw(VC, **kw)),
        3: (lambda kw: bot.raw(GroupDM, **kw)),
        4: (lambda kw: bot.raw(Catagory, **kw)),
        5: (lambda kw: bot.raw(NewsChannel, **kw)),
        6: (lambda kw: bot.raw(StoreChannel, **kw))
    }

    return channels[kw["type"]](kw)
