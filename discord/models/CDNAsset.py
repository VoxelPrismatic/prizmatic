__all__ = ["CDNAsset"]

class CDNAsset:
    """
    {{cls}} instance = CDNAsset(url, **fmt)

    {{desc}} Represents a CDN Asset for emojis and things

    {{param}} url [str]
        The URL of the asset, with formatting

    {{param}} **fmt [kwargs]
        How to format the URL
        {{note}} All of these keys will automatically become attributes

    {{prop}} url [str]
        The formatted URL
    """
    def __init__(self, url, **fmt):
        self.url = url.format(**fmt)
        self.fmt = fmt
        for key in fmt:
            self.__setattr__(key, fmt[key])
