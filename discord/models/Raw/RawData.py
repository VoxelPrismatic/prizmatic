__all__ = ["RawData"]

class RawData:
    """
    {{cls}} instance = RawData()

    {{desc}} A container for bytes and things to be interacted similarly to the
    other Raw classes

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, data: bytes):
        self.data = data

    async def get(self):
        return self.data

    def __call__(self):
        return self.data
