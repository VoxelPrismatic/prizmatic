import datetime
from ..Perms import Perms
from ..Guild import Guild
from ..User import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from ..Overwrite import Overwrite

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