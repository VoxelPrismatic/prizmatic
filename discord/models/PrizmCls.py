import re

__all__ = [
    "PrizmDict",
    "PrizmList"
]

class PrizmList(list):
    """
    {{cls}} instance = PrizmList(*args)

    {{desc}} A list, but with more useful stuff

    {{note}} There are some differences when managing your lists when using this
    class. Be sure to read the docs.

    {{param}} *args [args]
        Your list, can be left blank
    """
    def __init__(self, *args):
        self = list(args)
    def __lshift__(self, item):
        """
        {{fn}} instance.__lshift__(item)

        {{note}} This function is actually meant to be used as `instance << item`

        {{desc}} Short for `instance.append(item)`

        {{param}} item [Any]
            The item to append to the list
        """
        self.append(item)
    def __rshift__(self, item):
        """
        {{fn}} instance.__rshift__(item)

        {{note}} This function is actually meant to be used as `instance >> item`

        {{desc}} Short for `instance.remove(item)`

        {{param}} item [Any]
            The item to remove from the list
        """
        self.remove(item)
    def __invert__(self):
        """
        {{fn}} instance.__invert__()

        {{note}} This function is actually meant to be used as `~instance`

        {{desc}} Reverses the list
        """
        self = self[::-1]
    def __isub__(self, data):
        """
        {{fn}} instance.__isub__(data)

        {{note}} This function is actually meant to be used as `instance -= data`

        {{desc}} Removes all items in data from the list

        {{param}} data [List[Any]]
            The list of things to remove
        """
        for item in data:
            self >= item
        return self
    def __iadd__(self, data):
        """
        {{fn}} instance.__iadd__(data)

        {{note}} This function is actually meant to be used as `instance += data`

        {{desc}} Short for `instance.extend(data)`

        {{param}} data [List[Any]]
            The list of things to add to the list
        """
        self.extend(data)
        return self
    def __or__(self, seperator):
        "list | ' '  ||  ' '.join([str(item) for item in list])"
        ls = [str(item) for item in self]
        return seperator.join(ls)
    def __and__(self, item):
        "list & item  ||  list.index(item)"
        return self.index(item)
    def __matmul__(self, index: int = 1):
        "list @ index  ||  list.pop(index)"
        return self.pop(index)

class PrizmDict:
    """
    {{cls}} instance = PrizmDictList(**pairs)

    {{desc}} Allows you to use a dict as a list, and vice versa

    """
    def __init__(self, **pairs):
        self.pairs = pairs

    def __str__(self):
        return str(self.pairs)

    def __getitem__(self, key):
        if type(key) == int and key not in self.pairs:
            return self.pairs[list(self.pairs)[key]]
        elif key in self.pairs:
            return self.pairs[key]
        raise KeyError(key)

    def __setitem__(self, key, val):
        self.pairs[key] = val

    def __delitem__(self, key):
        if type(key) == int and key not in self.pairs:
            del self.pairs[list(self.pairs)[key]]
        elif key in self.pairs:
            del self.pairs[key]
        raise KeyError(key)

    def __dict__(self):
        return self.pairs

    def __list__(self):
        return self.pairs.values()

    def pop(self, key):
        if type(key) == int and key not in self.pairs:
            val = self.pairs[list(self.pairs)[key]]
            del self.pairs[list(self.pairs)[key]]
            return val
        elif key in self.pairs:
            val = self.pairs[key]
            del self.pairs[key]
            return val
        raise KeyError(key)

    def __call__(self, mesh):
        if mesh in self.pairs:
            return self.pairs[mesh]
        try:
            if int(mesh) in self.pairs:
                return self.pairs[int(mesh)]
        except Exception:
            pass
        try:
            if str(mesh) in self.pairs:
                return self.pairs[int(mesh)]
        except Exception:
            pass
        raise KeyError(mesh)

    def __contains__(self, key):
        try:
            self(key)
            return True
        except KeyError:
            return False

    def __getslice__(self, start, end, step = 1):
        return self.pairs.values()[start:end:step]

    def __delslice__(self, start, end, step = 1):
        for index in range(start, end, step):
            del self.pairs[index]

    def __add__(self, other):
        if type(other) == dict:
            self.pairs.update(other)
        else:
            try:
                for key, val in other:
                    self.pairs[key] = val
            except TypeError:
                if len(other) == 2:
                    self.pairs[other[0]] = other[1]
                else:
                    raise TypeError("Cannot add `" + str(other) + "` to dict")
        return self

    def __iadd__(self, other):
        return self + other

    def __len__(self):
        return len(self.pairs)

    def __tuple__(self):
        return ((key, self.pairs[key]) for key in self.pairs)

    def __invert__(self):
        return {self.pairs[key]: key for key in self.pairs}

    def __iter__(self):
        self.___iter_index___ = -1
        return self

    def __next__(self):
        self.___iter_index___ += 1
        if self.___iter_index___ < len(self.pairs):
            return self.pairs[list(self.pairs)[self.___iter_index___]]
        raise StopIteration

    def keys(self):
        return self.pairs.keys()

    def values(self):
        return self.pairs.values()

    def update(self, other):
        self.pairs.update(other)

    def clear(self):
        self.pairs = {}

    def get(self, key, default = None):
        return self.pairs.get(key, default)

    def items(self):
        return self.pairs.items()
