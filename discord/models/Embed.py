import re
import datetime
from .Color import Color
from .PrizmCls import PrizmList, PrizmDict
from .ClsUtil import from_ts, https

__all__ = ["typed", "Embed"]

def typed(thing):
    ls = []
    for th in thing:
        ls.append(type(th))
    return ls

class Embed:
    """
    {{cls}} instance = Embed(*, too_many_args_to_list_here)

    {{desc}} Represents a Discord Embed

    {{param}} title [str]
        The Embed Title, 256 chars max, %N0%

    {{param}} type [str]
        Type of embed
        {{norm}} "rich"

    {{param}} desc [str]
        The Embed Description, 2048 chars max, %N0%
        {{alias}} description

    {{param}} fields [List[str, str, bool], List[str, str]]
        The fields, in [name, value, inline?] format
        Alternatively, you can use [name, value], where inline is False
        - name is 256 chars max, %N0%
        - value is 1024 chars max, %N0%
        - inline is False by default
        Any more than 25 fields will be discarded
        Any invalid fields will silently be discarded

    {{param}} foot [str]
        The footer, 2048 chars max, %N0%
        {{alias}} footer

    {{param}} foot_icon [str]
        The http[s] url of the footer icon, %N1%
        {{alias}} footer_icon

    {{param}} foot_proxy_icon [str]
        The proxied url of the footer icon
        {{alias}} footer_proxy_icon

    {{param}} url [str]
        The url of the embed, http[s] only, %N1%

    {{param}} time [datetime.datetime, str]
        The Datetime object of the time you wish to put
        Placing "now" will give you the current time in UTC
        Placing a VALID ISO 8601 timestamp will also work
        {{alias}} timestamp

    {{param}} color [discord.models.Color, int, str, tuple]
        The color of the embed
        - if str, must be in hex eg #004466, in that format
        - if tuple, then it must be 3 ints with max value 255, RGB
        - if int, then no problem
        - if Color, then it must be a Color object from this library

    {{param}} image [str]
        The http[s] url of the image, %N1%

    {{param}} image_proxy [str]
        The proxied url of the image

    {{param}} image_height [int]
        How tall the image should be

    {{param}} image_width [int]
        How wide the image should be

    {{param}} thumb [str]
        The http[s] url of the thumbnail, %N1%
        {{alias}} thumbnail

    {{param}} thumb_proxy [str]
        The proxied url of the thumbnail
        {{alias}} thumbnail_proxy

    {{param}} thumb_height [int]
        How tall the thumbnail should be
        {{alias}} thumbnail_height

    {{param}} thumb_width [int]
        How wide the thumbnail should be
        {{alias}} thumbnail_width

    {{param}} video [str]
        The http[s] url of the video %N1%

    {{param}} video_height [int]
        How tall the video should be

    {{param}} video_width [int]
        How wide the video should be

    {{param}} provider [str]
        Name of the provider

    {{param}} provider_url [str]
        The url of the provider

    {{param}} author [str]
        Name of the author, 256 chars max, %N0%

    {{param}} author_url [str]
        The url of the author

    {{param}} author_icon [str]
        The http[s] url of the author's pfp, %N1%

    {{param}} author_proxy_icon [str]
        The proxied url of the author's pfp

    %n0% All text will automatically be stripped to meet length requirements

    %n1% All non http[s] or urls [not including proxied ones] will be silently
    discarded, but Discord does allow the `attachment://<file_name>.<type>`
    scheme, and is supported here too.

    {{note}} This is the default formatting of an Embed ---
     ______________
    /
    | Author things
    | Title
    | -------------
    | desc...       [thumb]
    |
    | Field name
    | field content
    |
    | [   image   ]
    | [           ]
    | -------------
    | Footer things | Timestamp
    |______________
    *not to scale ofc but this is the general layout

    {{prop}} title [str]
        The title of the embed

    {{prop}} type [str]
        The type of embed

    {{prop}} desc [str]
        Description
        {{alias}} description

    {{prop}} foot [str]
        Footer text
        {{alias}} footer

    {{prop}} foot_icon [str]
        Footer icon URL
        {{alias}} footer_icon

    {{prop}} foot_proxy_icon [str]
        Footer proxy icon URL
        {{alias}} footer_proxy_icon

    {{prop}} url [str]
        The embed URL

    {{prop}} time [None, datetime.datetime]
        The timestamp of the embed
        {{alias}} timestamp

    {{prop}} color [None, Color]
        The color of the embed, on the left

    {{prop}} image [str]
        Image URL
        {{alias}} img

    {{prop}} image_proxy [str]
        Image proxy URL
        {{alias}} img_proxy

    {{prop}} image_width [int]
        Width of the image in pixels
        {{alias}} img_w

    {{prop}} image_height [int]
        Height of the image in pixels
        {{alias}} img_h

    {{prop}} thumb [str]
        The thumbnail URL
        {{alias}} thumbnail

    {{prop}} thumb_proxy [str]
        The thumbnail proxy URL
        {{alias}} thumbnail_proxy

    {{prop}} thumb_width [int]
        The width of the thumbnail in pixels
        {{alias}} thumbnail_width
        {{alias}} thumb_w

    {{prop}} thumb_height [int]
        Height of the thumbail in pixels
        {{alias}} thumbnail_height
        {{alias}} thumb_w

    {{prop}} video [str]
        The video URL
        {{alias}} vid

    {{prop}} video_proxy [str]
        The video proxy URL
        {{alias}} vid_proxy

    {{prop}} video_width [int]
        The video width in pixels
        {{alias}} vid_w

    {{prop}} video_height [int]
        The height of the video in pixels
        {{alias}} vid_h

    {{prop}} provider [str]
        Name of the provider, eg "YouTube"

    {{prop}} provider_url [str]
        The URL of the provider, eg "https://youtu.be/"

    {{prop}} author [str]
        Name of the author
        {{alias}} auth

    {{prop}} author_url [str]
        The URL of where to locate the author
        {{alias}} auth_url

    {{prop}} author_icon [str]
        The URL of the author icon
        {{alias}} auth_icon

    {{prop}} author_proxy_icon [str]
        URL of the author proxy icon
        {{alias}} auth_proxy_icon

    {{prop}} fields [List[List[str, str, bool]]]
        A list of fields in the [name, val, ?inline] format

    {{prop}} valid [bool]
        Whether or not this embed is valid according to the Discord docs
    """

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        return f"<Embed object - '{self.title or '[no title]'}'>"

    def __init__(self, *, title = "", type = "rich", desc = "",
                 description = "", fields = [], foot = "", footer = "",
                 foot_icon = "", timestamp = None, footer_icon = "",
                 foot_proxy_icon = "", footer_proxy_icon = "", url = "",
                 time = None, color = None, image = "", image_proxy = "",
                 image_width = 0, image_height = 0, thumb = "", thumbnail = "",
                 thumb_proxy = "", thumbnail_proxy = "", thumb_width = 0,
                 thumbnail_width = 0, thumb_height = 0, thumbnail_height = 0,
                 video = "", video_height = 0, video_width = 0, provider = "",
                 provider_url = "", author = "", author_url = "",
                 author_icon = "", author_proxy_icon = ""):
        self.title = str(title)[:257]
        self.type = str(type)
        self.desc = str(desc or description)[:2049]
        self.foot = str(foot or footer)[:2049]
        self.foot_icon = https(str(foot_icon or footer_icon))
        self.foot_proxy_icon = str(foot_proxy_icon or footer_proxy_icon)
        self.url = https(str(url))
        self.time = None
        self.color = None
        if time is not None:
            self.time = from_ts(time)
        if type(color) == Color:
            self.color = Color
        elif color:
            self.color = Color(color)
        self.image = https(str(image))
        self.image_proxy = str(image_proxy)
        self.image_width = int(image_width)
        self.image_height = int(image_height)
        self.thumb = https(str(thumb or thumbnail))
        self.thumb_proxy = str(thumb_proxy or thumbnail_proxy)
        self.thumb_width = int(thumb_width or thumbnail_width)
        self.thumb_height = int(thumb_height or thumbnail_height)
        self.video = https(str(video))
        self.video_width = int(video_width)
        self.video_height = int(video_height)
        self.provider = str(provider)
        self.provider_url = str(provider_url)
        self.author = str(author)[:257]
        self.author_url = str(author_url)
        self.author_icon = https(str(author_icon))
        self.author_proxy_icon = str(author_proxy_icon)
        self.fields = PrizmList([])
        for field in fields:
            if len(self.fields) >= 25:
                break
            if typed(field) == [str, str, bool]:
                self.fields << field
            elif typed(field) == [str, str, int]:
                self.fields << field[:-1] + [bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            else:
                pass
                #Invalid fields will silently be discarded

    def __dict__(self):
        """
        {{fn}} instance.__dict__()

        {{note}} This function is actually meant to be used as `dict(instance)`

        {{desc}} Returns a discord-compatible dict object ready for sending

        {{rtn}} [dict] The send-ready object

        {{err}} [ValueError] If the embed is invalid, this saves time and data
        usage by checking locally instead of remotely
        """
        if not self.valid:
            raise ValueError("This embed is malformed, " + self.why_invalid)
        emb = {"type": self.type}
        if self.title:
            emb["title"] = self.title
        if self.desc:
            emb["description"] = self.desc
        if self.foot:
            emb["footer"] = {}
            emb["footer"]["text"] = self.foot
            if self.foot_icon:
                emb["footer"]["icon_url"] = self.foot_icon
            if self.foot_proxy_icon:
                emb["footer"]["proxy_icon_url"] = self.foot_proxy_icon
        if self.url:
            emb["url"] = self.url
        if self.time:
            emb["timestamp"] = self.time.isoformat()
        if self.color:
            emb["color"] = self.color.color
        if self.image or self.image_proxy or self.image_width or\
                self.image_height:
            emb["image"] = {}
            if self.image:
                emb["image"]["url"] = self.image
            if self.image_proxy:
                emb["image"]["proxy_url"] = self.image_proxy
            if self.image_width:
                emb["image"]["width"] = self.image_width
            if self.image_height:
                emb["image"]["height"] = self.image_height
        if self.thumb or self.thumb_proxy or self.thumb_width or\
                self.thumb_height:
            emb["thumbnail"] = {}
            if self.thumb:
                emb["thumbnail"]["url"] = self.thumb
            if self.thumb_proxy:
                emb["thumbnail"]["proxy_url"] = self.thumb_proxy
            if self.thumb_width:
                emb["thumbnail"]["width"] = self.thumb_width
            if self.thumb_height:
                emb["thumbnail"]["height"] = self.thumb_height
        if self.video or self.video_width or self.video_height:
            emb["video"] = {}
            if self.video:
                emb["video"]["url"] = self.video
            if self.video_height:
                emb["video"]["height"] = self.video_height
            if self.video_width:
                emb["video"]["width"] = self.video_width
        if self.provider or self.provider_url:
            emb["provider"] = {}
            if self.provider:
                emb["provider"]["name"] = self.provider
            if self.provider_url:
                emb["provider"]["url"] = self.provider_url
        if self.author or self.author_url or self.author_icon or\
                self.author_proxy_icon:
            emb["author"] = {}
            if self.author:
                emb["author"]["name"] = self.author
            if self.author_url:
                emb["author"]["url"] = self.author_url
            if self.author_icon:
                emb["author"]["icon_url"] = self.author_icon
            if self.author_proxy_url:
                emb["author"]["proxy_icon_url"] = self.author_proxy_icon
        if self.fields:
            emb["fields"] = []
            for field in self.fields:
                emb["fields"].append({
                    "name": field[0],
                    "value": field[1],
                    "inline": field[2]
                })
        return emb

    def clear(self, *args):
        """
        {{fn}} instance.clear(*args)

        {{desc}} Clears values

        {{param}} *args [str]
            What attributes to clear, eg ['title', 'desc']

        {{rtn}} [discord.models.Embed] Itself
        """
        for arg in args:
            self.__setattr__(arg, None)
        return self

    def set(self, *, title = "", type = "rich", desc = "",
            description = "", fields = [], foot = "", footer = "",
            foot_icon = "", timestamp = None, footer_icon = "",
            foot_proxy_icon = "", footer_proxy_icon = "", url = "",
            time = None, color = None, image = "", image_proxy = "",
            image_width = 0, image_height = 0, thumb = "", thumbnail = "",
            thumb_proxy = "", thumbnail_proxy = "", thumb_width = 0,
            thumbnail_width = 0, thumb_height = 0, thumbnail_height = 0,
            video = "", video_height = 0, video_width = 0, provider = "",
            provider_url = "", author = "", author_url = "",
            author_icon = "", author_proxy_icon = ""):
        """
        {{fn}} instance.set(*, too_many_args_to_list_here)

        {{desc}} Similar to creation, but only overrides given params

        {{note}} All parameters are the ones from initialization. That way you
        can edit all the params in one command

        {{rtn}} [discord.models.Embed] Itself
        """
        self.title = str(title)[:257] or self.title
        self.type = str(type) or self.type
        self.desc = str(desc or description)[:2049] or self.desc
        self.foot = str(foot or footer)[:2049] or self.foot
        self.foot_icon = https(str(foot_icon or footer_icon)) or self.foot_icon
        self.foot_proxy_icon =\
            str(foot_proxy_icon or footer_proxy_icon) or self.foot_proxy_icon
        self.url = https(str(url)) or self.url
        if time is not None:
            self.time = from_ts(time)
        if type(color) == Color:
            self.color = Color
        elif color:
            self.color = Color(color)
        self.image = https(str(image)) or self.image
        self.image_proxy = str(image_proxy) or self.image_proxy
        self.image_width = int(image_width) or self.image_width
        self.image_height = int(image_height) or self.image_height
        self.thumb = https(str(thumb or thumbnail)) or self.thumb
        self.thumb_proxy = str(thumb_proxy or thumbnail_proxy) or\
            self.thumb_proxy
        self.thumb_width = int(thumb_width or thumbnail_width) or\
            self.thumb_width
        self.thumb_height = int(thumb_height or thumbnail_height) or\
            self.thumb_height
        self.video = https(str(video)) or self.video
        self.video_width = int(video_width) or self.video_width
        self.video_height = int(video_height) or self.video_height
        self.provider = str(provider) or self.provider
        self.provider_url = str(provider_url) or self.provider_url
        self.author = str(author)[:257] or self.author
        self.author_url = str(author_url) or self.author_url
        self.author_icon = https(str(author_icon)) or self.author_icon
        self.author_proxy_icon = str(author_proxy_icon) or\
            self.author_proxy_icon
        if fields:
            self.fields = PrizmList([])
        for field in fields:
            if len(self.fields) >= 25:
                break
            if typed(field) == [str, str, bool]:
                self.fields << field
            elif typed(field) == [str, str, int]:
                self.fields << field[:-1] + [bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            else:
                pass
                #Invalid fields will silently be discarded
        return self

    def append_fields(self, fields):
        """
        {{fn}} instance.append_fields(fields)

        {{desc}} Adds fields to the embed

        {{param}} fields [List[List[str, str, bool]], List[str, str, bool]]
            Either a single field or a list of fields

        {{rtn}} [discord.models.Embed] Itself
        """
        if type(fields[0]) != list:
            fields = [fields]
        for field in fields:
            if len(self.fields) >= 25:
                break
            if typed(field) == [str, str, bool]:
                self.fields << field
            elif typed(field) == [str, str, int]:
                self.fields << field[:-1] + [bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            #Invalid fields will silently be discarded
        return self

    def swap_fields(self, fields: dict):
        """
        {{fn}} instance.swap_fields(fields)

        {{desc}} Swaps a set of fields

        {{param}} fields [Dict[int: int]]
            A dict of key-value pairs where the key is the field you want to
            swap and the value is the new location of the field. This also
            swaps the field currently occupying that location.

        {{rtn}} [discord.models.Embed] Itself
        """
        ls = self.fields
        for key in fields:
            val = fields[key]
            ls[key], ls[val] = ls[val], ls[key]
        self.fields = ls
        return self

    def edit_field(self, index: int, field):
        """
        {{fn}} instance.edit_field(index, field)

        {{desc}} Edits a field at index

        {{param}} index [int]
            The field number to edit, starts from 0

        {{param}} field [List[str, str, bool], List[str, str]]
            The fields, in [name, value, inline?] format
            Alternatively, you can use [name, value], where inline is False
            - name is 256 chars max, %N0%
            - value is 1024 chars max, %N0%
            - inline is False by default
            Any more than 25 fields will be discarded
            Any invalid fields will silently be discarded
        """
        if typed(field) == [str, str, bool]:
            self.fields[index - 1] = field
        elif typed(field) == [str, str, int]:
            self.fields[index - 1] = field[:-1] + [bool(field[-1])]
        elif typed(field) == [str, str]:
            self.fields[index - 1] = field + [False]
        #Invalid fields will silently be discarded

    def remove_fields(self, indexes):
        """
        {{fn}} instance.remove_fields(indexes)

        {{desc}} Removes fields, starting from 0

        {{param}} indexes [int, str, List[int]]
            The indexes to remove. This is 0 based

        {{rtn}} [discord.models.Embed] Itself
        """
        if type(indexes) == int:
            indexes = [indexes]
        for index in indexes:
            del self.fields[int(index)]
        return self

    def from_dict(self, emb):
        """
        {{fn}} instance.from_dict(emb)

        {{desc}} Converts a dict embed to an actual embed

        {{param}} emb [dict]
            A dict compatible object

        {{rtn}} The new embed
        """
        if "footer" in emb:
            if "text" in emb["footer"]:
                emb["foot"] = emb["footer"]["text"]
            if "icon_url" in emb["footer"]:
                emb["foot_icon"] = emb["footer"]["icon_url"]
            if "proxy_icon_url" in emb["footer"]:
                emb["foot_proxy_icon"] = emb["footer"]["proxy_icon_url"]
            del emb["footer"]
        if "image" in emb:
            emb["img"] = emb["image"]
            if "url" in emb["img"]:
                emb["image"] = emb["img"]["url"]
            if "proxy_url" in emb["img"]:
                emb["image_proxy"] = emb["img"]["proxy_url"]
            if "width" in emb["img"]:
                emb["image_width"] = emb["img"]["width"]
            if "height" in emb["img"]:
                emb["image_height"] = emb["img"]["height"]
            del emb["img"]
        if "thumbnail" in emb:
            if "url" in emb["thumbnail"]:
                emb["thumb"] = emb["thumbnail"]["url"]
            if "proxy" in emb["thumbnial"]:
                emb["thumb_proxy"] = emb["thumbnail"]["proxy_url"]
            if "width" in emb["thumbnail"]:
                emb["thumb_width"] = emb["thumbnail"]["width"]
            if "height" in emb["thumbnail"]:
                emb["thumb_height"] = emb["thumbnail"]["height"]
            del emb["thumbnail"]
        if "video" in emb:
            emb["vid"] = emb["video"]
            if "url" in emb["vid"]:
                emb["video"] = emb["vid"]["url"]
            if "height" in emb["vid"]:
                emb["video_height"] = emb["vid"]["height"]
            if "width" in emb["vid"]:
                emb["video_width"] = emb["video"]["width"]
            del emb["vid"]
        if "provider" in emb:
            if "url" in emb["provider"]:
                emb["provider_url"] = emb["provider"]["name"]
            if "name" in emb["provider"]:
                emb["provider"] = emb["provider"]["name"]
        if "author" in emb:
            emb["auth"] = emb["author"]
            if "name" in emb["auth"]:
                emb["author"] = emb["auth"]["name"]
            if "url" in emb["auth"]:
                emb["author_url"] = emb["auth"]["url"]
            if "icon_url" in emb["auth"]:
                emb["author_icon"] = emb["auth"]["icon_url"]
            if "proxy_icon_url" in emb["auth"]:
                emb["author_proxy_icon"] = emb["auth"]["proxy_icon_url"]
        if self.fields:
            emb["fields"] = [
                (d["name"], d["value"], d["inline"]) for d in emb["fields"]
            ]
        self.set(**emb) #Provides checks too :D
        return self

    def __getitem__(self, key):
        """
        {{fn}} instance.__getitem__(key)

        {{note}} This function is meant to be used as `instance[key]`

        {{desc}} Returns an attribute, so you can interact with this class as if
        it were a dict

        {{param}} key [str]
            The attribute you want

        {{rtn}} [Any] The attribute
        """
        return self.__getattribute__(key)

    def __setitem__(self, key, val):
        """
        {{fn}} instance.__setitem__(key) = val

        {{note}} This function is meant to be used as `instance[key] = val`

        {{desc}} Returns an attribute, so you can interact with this class as if
        it were a dict

        {{param}} key [str]
            The attribute to set

        {{param}} val [Any]
            The value to set the attribute to
        """
        self.set(**{key: val})

    #Named Aliases
    @property
    def thumbnail(self):
        return self.thumb

    @property
    def thumbnail_proxy(self):
        return self.thumb_proxy

    @property
    def thumbnail_height(self):
        return self.thumb_height

    @property
    def thumbnail_width(self):
        return self.thumbwidth

    @property
    def footer(self):
        return self.foot

    @property
    def footer_icon(self):
        return self.foot_icon

    @property
    def footer_proxy_icon(self):
        return self.foot_proxy_icon

    @property
    def description(self):
        return self.desc

    @property
    def timestamp(self):
        return self.time

    @property
    def img(self):
        return self.image

    @property
    def img_proxy(self):
        return self.image_proxy

    @property
    def img_w(self):
        return self.image_width

    @property
    def img_h(self):
        return self.image_height

    @property
    def thumb_w(self):
        return self.thumb_width

    @property
    def thumb_h(self):
        return self.thumb_height

    @property
    def vid(self):
        return self.video

    @property
    def vid_proxy(self):
        return self.video_proxy

    @property
    def vid_w(self):
        return self.video_width

    @property
    def vid_h(self):
        return self.video_height

    @property
    def auth(self):
        return self.author

    @property
    def auth_url(self):
        return self.author_url

    @property
    def auth_icon(self):
        return self.author_icon

    @property
    def auth_proxy_icon(self):
        return self.author_proxy_icon

    @property
    def valid(self):
        self.why_invalid = "Is valid"
        chars = 0
        field_n = 0
        for field in self.fields:
            name, val, inline = field
            chars += len(name) + len(val)
            if len(name) > 256:
                self.why_invalid = f"title in field {field_n} is too long"
                return False
            if len(val) > 1024:
                self.why_invalid = f"value in field {field_n} is too long"
                return False
            if inline not in [True, False]:
                self.why_invalid = f"inline in field {field_n} is not a bool"
                return False
            field_n += 1
        if len(self.fields) > 25:
            self.why_invalid = f"too many fields"
            return False
        chars += len(self.title)
        chars += len(self.desc)
        chars += len(self.foot)
        chars += len(self.author)
        if len(self.title) > 256:
            self.why_invalid = f"title is too long"
            return False
        if len(self.desc) > 2048:
            self.why_invalid = f"description is too long"
            return False
        if len(self.foot) > 2048:
            self.why_invalid = f"footer is too long"
            return False
        if len(self.author) > 256:
            self.why_invalid = f"author is too long"
            return False
        if chars > 6000:
            self.why_invalid = f"too many chars"
            return False
        return True
