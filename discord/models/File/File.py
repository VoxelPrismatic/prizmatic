import random
from ..Error import ClassError
import re
import io
from ..Raw import RawFile, RawData
import aiohttp
import aiofiles

def rand_name():
    return "".join(random.choice("0123456789ABCDEF") for x in range(16))

class File:
    """
    DESCRIPTION ---
        Represnts a file, used for sending files in messages
    
    PARAMS ---
        loc [str, bytes, file, RawFile, url, RawData]
        - Some way of getting file data
        - str: The file name
        - bytes: Raw Data
        - file: Must have a read() function
        - RawFile: A RawFile object from this module
        - url: A url... duh
        - RawData: A RawData object from this module
        
        ?name [str]
        - Filename, default is random garbage
    
    FUNTIONS ---
        file = File(file_obj, name)
        - Create a new File object
        
        await file.get()
        - Return the data
        
        file()
        - Return the data
        
        await file.send()
        - Prepare the data for sending
    """
    def __init__(self, obj, name = rand_name()):
        self.name = name
        if type(obj) == str:
            if re.search(r"^https?://.+\..+$", obj):
                self.data = RawFile(obj)
            else:
                self.data = RawData(bytes(open(obj, "rb").read()))
        elif type(obj) == bytes:
            self.data = RawData(obj)
        elif type(obj) == io.IOBase:
            self.data = RawData(bytes(obj.read()))
        elif type(obj) == RawData or type(obj) == RawFile:
            self.data = data
        else:
            raise ClassError(obj, RawData, [str, bytes, io.IOBase, RawFile, RawData])
    
    async def get(self):
        return await self.data.get()
    
    def __call__(self):
        return self.data()
    
    async def load(self):
        return {"file": await self.get()}
