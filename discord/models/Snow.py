import re
from .Error import SnowDecodeError
from .ClsUtil import from_ts
import time

__all__ = ["Snow"]

class Snow:
    """
    {{cls}} instance = Snow(snowflake)

    {{desc}}
        Represents a snowflake... wonderfully named btw
        000000000000000000000000000000000000000000 00000 00000 000000000000
        ----------------TIME STAMP---------------- -wID- -pID- --INCREMENT--

    {{param}} snowflake [int, str, bytes]
        Represents a Discord snowflake
        - If str, then it must be a hex, number, or binary encoded string
        - If bytes, then it must be able to be utf-8 decoded
        - If int, then it must be correctly formatted

    {{prop}} timestamp [int]
        Creation date of the ID

    {{prop}} worker [int]
        Worker ID, the `wID` shown above.

    {{prop}} process [int]
        Process ID, the `pID` shown above.

    {{prop}} increment [int]
        Increment, idk

    {{prop}} id [int]
        The entire ID, like a guild id, channel id, or a message id

    {{prop}} hex [str]
        The hex formatted ID, if you need it

    {{prop}} bin [str]
        The binary formatted ID, if you need it

    {{prop}} dt [datetime.datetime]
        When the ID was made, as a datetime object
    """
    def __init__(self, snowflake):
        if not re.search(r"^[A-Fa-f0-9]+$", str(snowflake)):
            raise TypeError("Invalid snowflake format")
        if type(snowflake) == bytes:
            snowflake = snowflake.decode()
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

    #Named Aliases
    @property
    def timestamp(self):
        return (self.snowflake >> 22) + 1420070400000

    @property
    def worker(self):
        return (self.snowflake & 0x3e0000) >> 17

    @property
    def process(self):
        return (self.snowflake & 0x1f000) >> 12

    @property
    def increment(self):
        return self.snowflake & 0xfff

    @property
    def id(self):
        return self.snowflake

    @property
    def bin(self):
        return f"{self.id:064b}"

    @property
    def hex(self):
        return f"{self.id:016x}".upper()

    @property
    def dt(self):
        return from_ts(
            time.gmtime(self.timestamp).strftime("%Y-%m-%dT%H:%M:%S%z")
        )

    def __str__(self):
        """
        {{fn}} instance.__str__()

        {{note}} This function should actually be used as `str(instance)`

        {{desc}} Turns the snowflake into an str

        {{rtn}} [str] The str of the actual ID
        """
        return str(self.id)

    def __int__(self):
        """
        {{fn}} instance.__int__()

        {{note}} This function should actually be used as `int(instance)`

        {{desc}} Turns the snowflake into an int

        {{rtn}} [int] The actual ID
        """
        return self.id
