#from .Channel import Channel
from .VC import VC
from .DM import DM
from .StoreChannel import StoreChannel
from .Catagory import Catagory
from .NewsChannel import NewsChannel
from .GroupDM import GroupDM

def AnyChannel(**kw):
    channels = {
        0: RawObj(Channel, **kw),
        1: RawObj(DM, **kw),
        2: RawObj(VC, **kw),
        3: RawObj(GroupDM, **kw),
        4: RawObj(Catagory, **kw),
        5: RawObj(NewsChannel, **kw),
        6: RawObj(StoreChannel, **kw)
    }
    return channels[kw["type"]].make()
