import os
from decouple import config

class Config(object):
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    DATABASE_URI = config("MONGO_DB_URI", default=None)
    DATABASE_NAME = config("DATABASE_NAME", default="forwardBot")
    BOT_OWNER_ID = [int(id) for id in config("OWNER_ID", default="").split() if id]
    BOT_SESSION = config("BOT_SESSION", default="forward_bot")

class temp(object):
    # डेवलपर की कोडिंग के लिए ज़रूरी एक्स्ट्रा वेरिएबल्स
    CODE = ""
    ID = ""
    U_NAME = ""
    B_NAME = ""
    
