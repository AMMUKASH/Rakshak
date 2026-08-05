# ALONE-CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "38138069"))
        self.API_HASH = getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8928629348:AAF48_FddTgNgkh2v79Crs81Wo25XaL1B38")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003960961858"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8724182918"))
        
        self.SESSION1 = getenv("SESSION1", getenv("SESSION", "AQJF8NUAPb1dU1cM3tKSams8orzjo35R_OZmHER-2_W3u_LMK_sE_4xw0pdlpnnhP7kctOeuEBnJe79NfyTZeMoH98ysWq93cw8GjrXQ5s2hlhB1ukUGHjQfvvHDQQgx36901jgub9vuFARqGJ2Z2L2DblnEW8E-YMj6s2icgECxLsLglgumc14P-mDDfa6Nq6EL3nZEJLGP-PZLm-TLkE4uy4MOoAPGaJdMlf8MzNaG-U3pckCmp_Hz8dykt_eXLvvDVd4yi3-kjGDJGxNenqLoLOIor-n8jTbRC54VJkP50aAYEgmQtEdTH_XJ4Wm8Tq8AnXTANnGF5dU_3O7FPU_GM3zkHgAAAAH33XYXAA"))
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NovaBot_Support")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+BTg9b8Xw9lhkMWUx")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15000"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "50"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://graph.org/file/11f30f6c28f84b225f241-f2cc62b7b1350d2603.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://graph.org/file/3946d3c34cb555d30f033-fd126d42b07f4b512f.jpg")
        
        # Fixed: Added START_IMG_URL so plugins can fetch the image properly
        self.START_IMG = getenv("START_IMG", "https://graph.org/file/cef970290f42f10dce041-6163916620a47a86db.jpg")
        self.START_IMG_URL = getenv("START_IMG_URL", self.START_IMG)

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
