class Assets:
    """
    DESCRIPTION ---
        Represents assets
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, large_image, large_text, small_image, small_text):
        self.big_img = large_image
        self.big_txt = large_text
        self.lil_img = small_image
        self.lil_txt = small_text
    def __dict__(self):
        return {
            "large_image": self.big_img,
            "small_image": self.lil_img,
            "large_text": self.big_txt,
            "small_text": self.lil_txt
        }