from .File import File

__all__ = ["Files"]

class Files:
    """
    DESCRIPTION ---
        Represents multiple files

    PARAMS ---
        *file [File, str, bytes, file, RawFile, url, RawData]
        - The files, see the other class for more info

        NOTE: The name param is unsupported here. Please pass
              a `File` object if you want to have a name.

    FUNCTIONS ---
    """
    def __init__(self, *objs):
        self.ls = [File(obj) for obj in objs]

    async def get(self):
        return [await t.get() for t in self.ls]

    def __list__(self):
        return self.ls

    async def send(self):
        self.ls = self.ls[:11] #Discord only allows 10 files at a time iirc
        dic = {}
        for i in range(len(self.ls)):
            dic[f"file{i}"] = {
                "value": await self.ls[i].get(),
                "filename": self.ls[i].name,
                "content_type": "application/octet-stream"
            }
        return dic
