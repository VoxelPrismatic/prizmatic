import re
import datetime
from .Color import Color
from .PrizmCls import *

def https(thing):
    if re.search(r"^(https?|attachment)\:\/\/", thing):
        return thing
    return ""
    
def typed(thing):
    ls = []
    for th in thing:
        ls.append(type(th))
    return ls

class Embed:
    """
    DESCRIPTION ---
        Represents a Discord Embed
    
    PARAMS ---
        title [str]
        - The Embed Title, 256 chars max*
        
        type [str] 
        - Type of embed, "rich" by default
        
        desc [str] 
        - The Embed Description, 2048 chars max*
        - An alias resides under 'description', but this takes priority
        
        fields [list] 
        - The fields, in [name: str, value: str, inline: bool] format
        - - name is 256 chars max*
        - - value is 1024 chars max*
        - - inline is False by default
        - Any more than 25 fields will be discarded
        - Any invalid fields will silently be discarded
        
        foot [str] 
        - The footer, 2048 chars max*
        - An alias resides under 'footer', but this takes priority
        
        foot_icon [str]
        - The http[s] url of the footer icon**
        - An alias resides under 'footer_icon', but this takes priority
        
        foot_proxy_icon [str]
        - The proxied url of the footer icon
        - An alias resides under 'footer_proxy_icon', but this takes priority
        
        url [str] 
        - The url of the embed, http[s] only**
        
        time [datetime.datetime, str]
        - The Datetime object of the time you wish to put
        - Placing "now" will give you the current time in UTC
        - Placing a VALID ISO8601 timestamp will also work
        
        color [Color, int, str, tuple]
        - The color of the embed
        - - if str, must be in hex eg #004466, in that format
        - - if tuple, then it must be 3 ints with max value 255, RGB
        - - if int, then no problem
        - - if Color, then it must be a Color object from this library
        
        image [str]
        - The http[s] url of the image**
        
        image_proxy [str]
        - The proxied url of the image
        
        image_height [int]
        - How tall the image should be
        
        image_width [int]
        - How wide the image should be
        
        thumb [str]
        - The http[s] url of the thumbnail**
        - An alias resides under 'thumbnail', but this takes priority
        
        thumb_proxy [str]
        - The proxied url of the thumbnail
        - An alias resides under 'thumbnail_proxy', but this takes priority
        
        thumb_height [int]
        - How tall the thumbnail should be
        - An alias resides under 'thumbnail_height', but this takes priority
        
        thumb_width [int]
        - How wide the thumbnail should be
        - An alias resides under 'thumbnail_width', but this takes priority
        
        video [str]
        - The http[s] url of the video**
        
        video_height [int]
        - How tall the video should be
        
        video_width [int]
        - How wide the video should be
        
        provider [str]
        - Name of the provider
        
        provider_url [str]
        - The url of the provider
        
        author [str]
        - Name of the author, 256 chars max*
        
        author_url [str]
        - The url of the author
        
        author_icon [str]
        - The http[s] url of the author's pfp
        
        author_proxy_icon [str]
        - The proxied url of the author's pfp
        
        *All text will automatically be stripped to meet
         length requirements
         
        **All non http[s] or urls [not including proxied ones]
          will be silently discarded, but Discord does allow the 
          `attachment://<file_name>.<type>` scheme, and is supported
          here too.
          
    FUNCTIONS ---
        dict(Embed) -> dict
        - Returns the Discord readable version
        
        thing = Embed(**kwargs_from_above) -> Embed
        - Creates a new Embed object
        
        repr(Embed) -> str
        - The repr thing
        
        Embed.set(**kwargs_from_above)
        - Just like creating a new Embed object, but with the
          old params too
          
        Embed.add_field(field)
        - Adds a field
        
        Embed.add_fields(fields)
        - Adds many fields
        
        Embed.remove_field(index)
        - Removes field number index
        
        Embed.remove_fields(indexes)
        - Removes fields at the corresponding indexes
        
        Embed.set_field(index, field)
        - Sets field number index to field
        
        Embed.fromdict(dict_object)
        - Sets fields and things from the output template of `dict(embed)`
        
        Embed[param] -> Parameter
        - An alias for Embed.param if you want that
        
        Embed[param] = value
        - Shortcut for Embed.set(param = value), 
    """
    
    def __repr__(self):
        return f"<Embed object - '{self.title or '[no title]'}'>"
        
    def __aliases(self):
        self.thumbnail = self.thumb
        self.thumbnail_proxy = self.thumb_proxy
        self.thumbnail_height = self.thumb_height
        self.thumbnail_width = self.thumbwidth
        self.footer = self.foot
        self.footer_icon = self.foot_icon
        self.footer_proxy_icon = self.foot_proxy_icon
        self.description = self.desc
    
    def __init__(self, *, title = "", type = "rich", desc = "", description = "",
                 fields = [], foot = "", footer = "", foot_icon = "", timestamp = None,
                 footer_icon = "", foot_proxy_icon = "", footer_proxy_icon = "",
                 url = "", time = None, color = None, image = "", image_proxy = "",
                 image_width = 0, image_height = 0, thumb = "", thumbnail = "",
                 thumb_proxy = "", thumbnail_proxy = "", thumb_width = 0,
                 thumbnail_width = 0, thumb_height = 0, thumbnail_height = 0,
                 video = "", video_height = 0, video_width = 0, provider = "",
                 provider_url = "", author = "", author_url = "", author_icon = "",
                 author_proxy_icon = ""):
        self.title = str(title)[:257]
        self.type = str(type)
        self.desc = str(desc or description)[:2049]
        self.foot = str(foot or footer)[:2049]
        self.foot_icon = https(str(foot_icon or footer_icon))
        self.foot_proxy_icon = str(foot_proxy_icon or footer_proxy_icon)
        self.url = https(str(url))
        self.time = None
        self.color = None
        if type(time) == datetime.datetime:
            self.time = time
        elif time.lower() == "now":
            self.time = datetime.datetime.utcnow()
        elif re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}+\d{2}:\d{2}"):
            self.time = datetime.datetime.fromisoformat(time)
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
                self.fields << field[:-1]+[bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            else:
                pass
                #Invalid fields will silently be discarded
        self.__aliases()
        
    def __dict__(self):
        "Creates a JSON Embed object according to the Discord API"
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
        if self.image or self.image_proxy or self.image_width or self.image_height:
            emb["image"] = {}
            if self.image:
                emb["image"]["url"] = self.image
            if self.image_proxy:
                emb["image"]["proxy_url"] = self.image_proxy
            if self.image_width:
                emb["image"]["width"] = self.image_width
            if self.image_height:
                emb["image"]["height"] = self.image_height
        if self.thumb or self.thumb_proxy or self.thumb_width or self.thumb_height:
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
        if self.author or self.author_url or self.author_icon or self.author_proxy_icon:
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
                emb["fields"].append({"name": field[0], "value": field[1], "inline": field[2]})
        return emb
        
    def set(self, *, title = "", type = "rich", desc = "", description = "",
            fields = [], foot = "", footer = "", foot_icon = "",
            footer_icon = "", foot_proxy_icon = "", footer_proxy_icon = "",
            url = "", time = None, color = None, image = "", image_proxy = "",
            image_width = 0, image_height = 0, thumb = "", thumbnail = "",
            thumb_proxy = "", thumbnail_proxy = "", thumb_width = 0,
            thumbnail_width = 0, thumb_height = 0, thumbnail_height = 0,
            video = "", video_height = 0, video_width = 0, provider = "",
            provider_url = "", author = "", author_url = "", author_icon = "",
            author_proxy_icon = ""):
        self.title = str(title)[:257] or self.title
        self.type = str(type) or self.type
        self.desc = str(desc or description)[:2049] or self.desc
        self.foot = str(foot or footer)[:2049] or self.foot
        self.foot_icon = https(str(foot_icon or footer_icon)) or self.foot_icon
        self.foot_proxy_icon = str(foot_proxy_icon or footer_proxy_icon) or self.foot_proxy_icon
        self.url = https(str(url)) or self.url
        if type(time) == datetime.datetime:
            self.time = time
        elif time.lower() == "now":
            self.time = datetime.datetime.utcnow()
        if type(color) == Color:
            self.color = Color
        elif color:
            self.color = Color(color)
        self.image = https(str(image)) or self.image
        self.image_proxy = str(image_proxy) or self.image_proxy
        self.image_width = int(image_width) or self.image_width
        self.image_height = int(image_height) or self.image_height
        self.thumb = https(str(thumb or thumbnail)) or self.thumb
        self.thumb_proxy = str(thumb_proxy or thumbnail_proxy) or self.thumb_proxy
        self.thumb_width = int(thumb_width or thumbnail_width) or self.thumb_width
        self.thumb_height = int(thumb_height or thumbnail_height) or self.thumb_height
        self.video = https(str(video)) or self.video
        self.video_width = int(video_width) or self.video_width
        self.video_height = int(video_height) or self.video_height
        self.provider = str(provider) or self.provider
        self.provider_url = str(provider_url) or self.provider_url
        self.author = str(author)[:257] or self.author
        self.author_url = str(author_url) or self.author_url
        self.author_icon = https(str(author_icon)) or self.author_icon
        self.author_proxy_icon = str(author_proxy_icon) or self.author_proxy_icon
        if fields:
            self.fields = PrizmList([])
        for field in fields:
            if len(self.fields) >= 25:
                break
            if typed(field) == [str, str, bool]:
                self.fields << field
            elif typed(field) == [str, str, int]:
                self.fields << field[:-1]+[bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            else:
                pass
                #Invalid fields will silently be discarded
        self.__aliases()
    
    def add_fields(self, fields):
        for field in fields:
            if len(self.fields) >= 25:
                break
            if typed(field) == [str, str, bool]:
                self.fields << field
            elif typed(field) == [str, str, int]:
                self.fields << field[:-1]+[bool(field[-1])]
            elif typed(field) == [str, str]:
                self.fields << field + [False]
            #Invalid fields will silently be discarded
    
    def remove_field(self, index: int):
        del self.fields[index-1] #Humans don't count from 0
    
    def edit_field(self, index: int, field):
        if typed(field) == [str, str, bool]:
            self.fields[index-1] = field
        elif typed(field) == [str, str, int]:
            self.fields[index-1] = field[:-1]+[bool(field[-1])]
        elif typed(field) == [str, str]:
            self.fields[index-1] = field + [False]
        #Invalid fields will silently be discarded
    
    def add_field(self, index: int, field):
        if len(self.fields) > 25:
            return
        if typed(field) == [str, str, bool]:
            self.fields << field
        elif typed(field) == [str, str, int]:
            self.fields << field[:-1]+[bool(field[-1])]
        elif typed(field) == [str, str]:
            self.fields << field + [False]
        #Invalid fields will silently be discarded
            
    def remove_fields(self, indexes):
        for index in indexes:
            del self.fields[int(index)-1]
    
    def fromdict(self, emb):
        "Converts a dict to an Embed object"
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
                 emd["image"] = emb["img"]["url"]
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
            if width in emb["vid"]:
                emb["video_width"] = emb["video"]["width"]
            del emb["vid"]
        if "provider" in emb:
            if "url" in emb["provider"]:
                emb["provider_url"] = emb["provider"]["name"]
            if "name" in emd["provider"]:
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
            emb["fields"] = [(d["name"], d["value"], d["inline"]) for d in emb["fields"]]
        self.set(**emb) #Provides checks too :D
            
    def __getitem__(self, key):
        return self.__getattribute__(key)
    
    def __setitem__(self, key, val):
        self.set(**{key: val})
