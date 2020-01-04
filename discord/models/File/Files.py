from .File import File

__all__ = ["Files"]

class Files:
    """
    {{cls}} instance = Files(*objs)

    {{desc}} Represents multiple files

    {{param}} file [File, str, bytes, file, RawFile, url, RawData]
        The files, see ~.File for more info

    {{note}} The name param is unsupported here. Please pass a `File` object if
    you want to have a name
    """
    def __init__(self, *objs):
        self.ls = [File(obj) for obj in objs]

    async def get(self):
        """
        {{fn}} await instance.get()

        {{desc}} Gets the data if it was from a URL

        {{rtn}} [bytes] The data
        """
        return [await t.get() for t in self.ls]

    def __list__(self):
        return self.ls

    def __getitem__(self, index: int):
        """
        {{bltin}} instance.__getitem__(index)
        {{usage}} instance[index]

        {{desc}} Treats this as if it were a list

        {{rtn}} [~.File] The item at that index
        """

    async def send(self):
        """
        {{fn}} await instance.send()

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        self.ls = self.ls[:11] #Discord only allows 10 files at a time iirc
        i = 0
        for f in self.ls:
            yield await f.send(i)
            i += 1

    def __iter__(self):
        self.___iter_index___ = -1
        return self

    def __next__(self):
        self.___iter_index___ += 1
        if self.___iter_index___ < len(self.ls):
            return self.ls[self.___iter_index___]
        raise StopIteration
