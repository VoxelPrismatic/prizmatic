__all__ = ["Assets"]

class Assets:
    """
    {{cls}} instance = Assets(*, too_many_args_to_list_here)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents assets

    {{param}} large_image [str]
        Large image hash

    {{param}} large_text [str]
        Long description

    {{param}} small_image [str]
        Thumbnail hash

    {{param}} small_text [str]
        Short description

    {{prop}} big_img [str]
        Large image hash

    {{prop}} big_txt [str]
        Long description

    {{prop}} lil_img [str]
        Thumbnail hash

    {{prop}} lil_txt [str]
        Short description
    """
    def __init__(self, *, large_image, large_text, small_image, small_text):
        self.big_img = large_image
        self.big_txt = large_text
        self.lil_img = small_image
        self.lil_txt = small_text
    def __dict__(self):
        """
        {{fn}} instance.__dict__()

        {{note}} This function is actually meant to be used as `dict(instance)`

        {{desc}} Returns the send-ready object

        {{rtn}} [dict] The send-ready object
        """
        return {
            "large_image": self.big_img,
            "small_image": self.lil_img,
            "large_text": self.big_txt,
            "small_text": self.lil_txt
        }
