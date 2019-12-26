from .Channel import Channel
from .VC import VC
from .DM import DM
from .StoreChannel import StoreChannel
from .Category import Category
from .NewsChannel import NewsChannel
from .GroupDM import GroupDM

__all__ = ["AnyChannel"]

def AnyChannel(**kw):
    """
    {{clsfn}} instance = AnyChannel(**kw)

    {{desc}} Returns the appropriate channel
    """
    if "bot_obj" not in kw:
        raise TypeError("Could not find bot object as 'bot_obj' in kw")
    bot_obj = kw["bot_obj"]
    channels = {
        0: Channel,
        1: DM,
        2: VC,
        3: GroupDM,
        4: Category,
        5: NewsChannel,
        6: StoreChannel
    }
    if int(kw["id"]) in list(bot_obj.listeners.channels):
        return bot_obj.listeners.channels[int(kw["id"])]
    if str(kw["id"]) in list(bot_obj.listeners.channels):
        return bot_obj.listeners.channels[str(kw["id"])]
    return channels[kw["type"]](**kw)
