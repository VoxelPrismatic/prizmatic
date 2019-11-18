class RawFile:
    """
    DESCRIPTION ---
        Represents a file that is awaiting a download
        
    PARAMS ---
        url [str]
        - The url to download
        
    FUNCTIONS ---
        thing = RawFile(url)
        - Creates a new RawFile object
        
        await thing.get()
        - Download the file, returns the BytesIO object
        - If already downloaded, just return the file
        
        thing()
        - Returns the BytesIO object as is
        
        await thing.update()
        - Re downloads the file
    """
    def __init__(self, url):
        self.url = url
        self.downloaded = False
        self.data = io.BytesIO()
    
    async def get(self):
        if not self.downloaded:
            async with asyncio.ClientSession() as c:
                async with c.get(self.url) as r:
                    self.data = io.BytesIO(await r.read())
            self.downloaded = True
        return self.data
    
    def __call__(self):
        return self.data
    
    def __repr__(self):
        return f"<RawFile of {self.url} // Has{' not' if not self.downloaded else ''} been downloaded>"
    
    def update(self):
        async with asyncio.ClientSession() as c:
            async with c.get(self.url) as r:
                self.data = io.BytesIO(await r.read())
        self.downloaded = True
        return self.data