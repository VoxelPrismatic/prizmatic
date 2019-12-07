__all__ = ["SemiChannel"]

class SemiChannel:
    """
    DESCRIPTION ---
        Represents a partial channel object

    PARAMS ---
        Only initialize SemiObjects when the full version shouldn't be
        initialized by hand.

        name [str]
        - The name of the channel

        type [int]
        - The channel type
        - 0: Channel
          1: DM
          2: VC
          3: GroupDM
          4: Catagory
          5: NewsChannel
          6: StoreChannel

    FUNCTIONS ---
        semi = SemiChannel(name, type)
        - Creates a new SemiChannel object

        dict(semi)
        - Used internally for sending to Discord
    """
    pass
