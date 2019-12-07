__all__ = ["RawData"]

class RawData:
    """
    DESCRIPTION ---
        A container for bytes and things to be interacted
        similarly to the other Raw classes

    PARAMS ---
        data [bytes]
        - Raw data

    FUNCTIONS ---
        raw_data = RawData(bytes_obj)
        - Create a new RawData object

        await raw_data.get()
        - Return the bytes data

        raw_data()
        - Return the bytes data
    """
    def __init__(self, data: bytes):
        self.data = data

    async def get(self):
        return self.data

    def __call__(self):
        return self.data
