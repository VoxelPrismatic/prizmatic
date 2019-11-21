import re
from .Error import SnowDecodeError
import datetime
import time

class Snow:
    """
    DESCRIPTION ---
        Represents a snowflake... wonderfully named btw
        000000000000000000000000000000000000000000 00000 00000 000000000000
        ----------------TIME STAMP---------------- -wID- -PID- --INCREMENT--
        
    PARAMS ---
        snowflake [int, str]
        - Represents a Discord snowflake
        - Can be encoded in hex, binary, or an int all as strings
        - Can also be a raw int
        
    FUNCTIONS ---
        snow = Snow(snowflake)
        - Creates a Snow object
        
        str(snow)
        - Prepares the snowflake to send
    """
    def __init__(self, snowflake):
        if type(snowflake) == str:
            #Make sure it is correct
            if re.search(r"^[10]{64}$", snowflake):
                snowflake = int(snowflake, 2)
            elif re.search(r"^\d{20}$", snowflake):
                snowflake = int(snowflake)
            elif re.search(r"^[A-Fa-f0-9]{16}$", snowflake):
                snowflake = int(snowflake, 16)
            else:
                raise SnowDecodeError(snowflake)
        if type(snowflake) != int or len(str(snowflake)) != 20:
            #If the snowflake is broken
            raise SnowDecodeError(snowflake)
        self.timestamp = (snowflake >> 22) + 1420070400000
        self.worker = (snowflake & 0x3e0000) >> 17
        self.process = (snowflake & 0x1f000) >> 12
        self.increment = snowflake & 0xfff
        self.id = snowflake
        self.raw = f"{self.id:b}".zfill(64)
        self.hex = f"{self.id:h}".upper().zfill(16)
        self.dt = datetime.datetime.fromisoformat(time.gmtime(self.timestamp).strftime("%Y-%m-%dT%H:%M:%S%z"))
    
    def __str__(self):
        return str(self.id)