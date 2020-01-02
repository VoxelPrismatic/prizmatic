from .Overwrite import Overwrite

__all__ = ["Overwrites"]

class Overwrites:
    """
    {{loc}} discord.models.Perms

    {{cls}} instance = Overwrites(overwrites)

    {{desc}} Represents a list of overwrites with some extra features

    {{param}} overwrites [List[dict, ~.Overwrite]]
        The list of overwrites
        {{norm}} []

    {{prop}} overwrites [List[~.Overwrite]]
        The list of overwrites
    """
    def __init__(self, overwrites = []):
        self.overwrites = []
        for ovw in overwrites:
            if type(ovw) == dict:
                self.overwrites.append(Overwrite(**ovw))
            elif type(ovw) == Overwrite:
                self.overwrites.append(ovw)

    @property
    def empty(self) -> bool:
        for ovw in self.overwrites:
            if ovw.empty:
                return False
        return True

    def __list__(self):
        """
        {{bltin}} instance.__list__()
        {{usage}} list(instance)

        {{desc}} Returns the overwrites

        {{rtn}} [List[~.Overwrite]]
        """
        return self.overwrites

    def __getitem__(self, index: int):
        """
        {{bltin}} instance.__getitem__(index)
        {{usage}} instance[index]

        {{desc}} Treats this class as if it were a dict

        {{param}} index [int]
            The index into the list of overwrites

        {{rtn}} [~.Overwrite] The overwrite object
        """
        return self.overwrites[index]

    def __iter__(self):
        """
        {{bltin}} instance.__iter__()
        {{usage}} iter(instance)

        {{desc}} Creates a generator of channels

        {{rtn}} [generator]
        """
        self.___iter_index___ = -1
        return self

    def __next__(self):
        """
        {{bltin}} instance.__next__()
        {{usage}} for overwrite in instance: #... code

        {{desc}} Allows you to iterate through these overwrites

        {{rtn}} [~.Overwrite]
        """
        self.___iter_index___ += 1
        if self.___iter_index___ < len(self.sub_channels):
            return self.sub_channels[self.___iter_index___]
        else:
            raise StopIteration("No more overwrites")
