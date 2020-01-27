class Bitset:
    """
    {{cls}} instance = Bitset(bits, sets)

    {{desc}} Represents a bitset with extra features

    {{param}} bits [int]
        The actual bitset

    {{param}} sets [List[str]]
        What each bit means, from left to right

    {{prop}} bits [int]
        The actual bitset

    {{prop}} sets [List[str]]
        What each bit means, from left to right
    """
    def __init__(self, bits, sets):
        self.bits = bits
        self.sets = sets

    def __list__(self):
        """
        {{bltin}} instance.__list__()
        {{usage}} list(instance)

        {{desc}} Returns a list of actual flags this bitset has

        {{rtn}} [List[str]]
        """
        ls = []
        st = str(self)
        for bit in range(len(self.sets)):
            if str(self.bits)[bit] == "1":
                ls.append(self.sets[bit])
        return ls

    def __int__(self):
        """
        {{bltin}} instance.__int__()
        {{usage}} int(instance)

        {{desc}} Returns the actual bitset

        {{rtn}} [int]
        """
        return self.bits

    def __str__(self):
        """
        {{bltin}} instance.__str__()
        {{usage}} str(instance)

        {{desc}} Returns the binary bitset

        {{rtn}} [str]
        """
        return str(self.bits).zfill(len(self.sets))

    def __getitem__(self, key):
        """
        {{bltin}} instance.__getitem__(key)
        {{usage}} instance[key]

        {{desc}} Returns the flag at an index if the key is an `int`, or a bool
        if the flag is an str

        {{param}} key [int, str]
            Index or flag name

        {{rtn}} [int] The flag at that index if key is an int, least significant
        flag first [right to left]

        {{rtn}} [bool] Whether or not that flag is set if key is an str

        {{err}} [IndexError] If that flag index doesn't exist

        {{err}} [KeyError] If that flag name doesn't exist

        {{err}} [TypeError] If the key isn't an int or an str
        """
        if type(key) == int:
            return int(str(self)[::-1][key])
        if type(key) == str:
            if key in self.sets:
                return self[self.sets.index[key]]
            raise KeyError(f"Flag name '{key}' doesn't exist")
        raise TypeError(
            f"Type '{type(key)}' cannot be converted into type 'int' or 'str'"
        )

    def __setitem__(self, key, val):
        """
        {{bltin}} instance.__setitem__(key, val)
        {{usage}} instance[key] = val

        {{desc}} Sets a bit

        {{param}} key [int, str]
            Index or flag name

        {{param}} val [int, bool]
            Whether or not the bit is set

        {{rtn}} [int] The new bitset
        """
        exists = self[key]
        ls = list(str(self))[::-1]
        if type(key) == str:
            key = self.sets.index(key)
        if type(key) == int:
            ls[key] = "1" if val else "0"
            self.bits = int("".join(ls[::-1]), 2)
        return self.bits
