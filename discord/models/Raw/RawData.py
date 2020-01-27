__all__ = ["RawData"]

class RawData:
    """
    {{cls}} instance = RawData(data)

    {{note}} This class is 99% useless in your own code, do not use this class

    {{desc}} A container for bytes and things to be interacted similarly to the
    other Raw classes

    {{param}} data [bytes]
        The bytes object

    {{prop}} data [bytes]
        The bytes object
    """
    def __init__(self, data: bytes):
        self.data = data

    async def get(self):
        """
        {{fn}} await instance.get()

        {{rtn}} [bytes] The bytes object
        """
        return self.data

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.data` for lazy people like me

        {{rtn}} [bytes] The bytes object
        """
        return self.data
