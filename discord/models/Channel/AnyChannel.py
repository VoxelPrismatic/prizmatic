from ..ClsUtil import from_ts
from ..Perms import Perms
from ..Guild import Guild
from ..User import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from ..Overwrite import Overwrite
from .Channel import Channel
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