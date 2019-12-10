from .Channel import Channel
from .VC import VC
from .DM import DM
from .StoreChannel import StoreChannel
from .Catagory import Catagory
from .NewsChannel import NewsChannel
from .GroupDM import GroupDM

__all__ = ["AnyChannel"]

def AnyChannel(**kw):
    """
    DESCRIPTION ---
        Creates a channel given its JSON object version.

    PARAMS ---
        **kw
        - The JSON data that allows the object to be built

    RETURNS ---
        The respective channel object
    """
    if "bot_obj" not in kw:
        raise TypeError("Could not find bot object as 'bot_obj' in kw")
    bot = kw["bot_obj"]
    channels = {
        0: (lambda kw: Channel(**kw)),
        1: (lambda kw: DM(**kw)),
        2: (lambda kw: VC(**kw)),
        3: (lambda kw: GroupDM(**kw)),
        4: (lambda kw: Catagory(**kw)),
        5: (lambda kw: NewsChannel(**kw)),
        6: (lambda kw: StoreChannel(**kw))
    }

    return channels[kw["type"]](kw)
