# ALONE-CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "38138069"))
        self.API_HASH = getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8868866271:AAHz_eFiUHYNWhQ74SjHYUQDluJVSxEaO-E")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003992133346"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7101011030"))
        
        self.SESSION1 = getenv("SESSION", "1AZWarzwBu1wL0jYWg3tCmgg2CNTZKCyMFWh1hHncjfxhjwRBWu1PcEYKCGqOqtdvMuek8__wXzX37g47TVYuJ3w6xiNkQ22DKtHnpDCvIVBAaH5jtN8Gqy3xP7MeoUrtAGx83jl1fbXZHV08zMEK-hG0MVnBPm-uASe-XanlvU61sP4JPT1yReNKwlaCY9SSE6fEMjq4AufaI1ffAnVAOzurAM_HzAyVdQ2_sjViROhbsReQ8PC4sHfO9jPfGSDJnQo5Xr6tjfaW6klpMw1ftt8CBP_zq9Pfpx-mDEOBptHFK_2Uf3r2UoP0mjxuz_VlBtY-QUEgmsATpIhnWDEO2_YUrE_Zi7M=")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vrindawan62034")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+LGPEm34pKHg0Zjg5")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15000"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://graph.org/file/11f30f6c28f84b225f241-f2cc62b7b1350d2603.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://graph.org/file/3946d3c34cb555d30f033-fd126d42b07f4b512f.jpg")
        self.START_IMG = getenv("START_IMG", "https://graph.org/file/dc3de0bf818b895181611-87b2da544f0d3c852c.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
