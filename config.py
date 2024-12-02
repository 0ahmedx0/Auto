from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21417190")
    API_HASH = environ.get("API_HASH", "49cd487bc068aa8ec3cd060a587017b0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7518380330:AAH2Xub5gKYf4jYGT0-cJxdqotPpBL1rLLA") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "cluster0-shard-00-01.quu8v.mongodb.net:27017")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8077445518').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    # safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

