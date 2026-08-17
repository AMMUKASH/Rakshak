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
        self.OWNER_ID = int(getenv("OWNER_ID", "7246397998"))
        
        self.SESSION1 = getenv("SESSION", "AQJF8NUAkWtGWYP-9NSJ1wit0PRw8IMkqUV28fIFwb-X18whsd6BZLrUNFH7eOYvEMSby3c5zbNcCLQvbzgbd_xgSr5GPzo8Xk6kMUkrIJGz1HcTkzmk_o7iS3MTlpymsF4FVpetf5N97xdS0Ba_Ax5QStcKeV2bzRQBbeuF3ChOxdl8sFz2w5w0gCliw4QvmH0ne972lIzCYR9z9SGKqNG-Mzp3rn2htb2WeFiIDPzEYh3V5f80OMsmIX-b8fo61uH4d7EqewMmFil_K-H3PKw-iZta9Ukn8zy34uvw9tdTEeA_1Xb5NXPIgqAdfERC2LvI9QyLNBAXilzKqdgxHpXQkvpFUwAAAAIQ3DPLAA")
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
