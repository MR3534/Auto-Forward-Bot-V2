import os
from decouple import config

class Config(object):
    # इसमें कुछ भी नहीं बदलना है, यह सीधे रेंडर से क्रेडेंशियल उठाएगा
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    DATABASE_URI = config("MONGO_DB_URI", default=None)
    DATABASE_NAME = config("DATABASE_NAME", default="forwardBot")
    BOT_OWNER_ID = [int(id) for id in config("OWNER_ID", default="").split() if id]
    
