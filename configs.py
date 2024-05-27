# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23251905"))
    API_HASH = getenv("API_HASH", "77d10190a6643863ed0fdb86f7e691c5")
    BOT_TOKEN = getenv("BOT_TOKEN", "6982307590:AAHPRZwDjAO-_dSYp7nCpb4OqRuKZqUbrXo")
    FSUB = getenv("FSUB", "Nope Noss Bot")
    CHID = int(getenv("CHID", "-1002108507583"))
    SUDO = list(map(int, getenv("SUDO", "6134208096").split()))
    MONGO_URI = getenv("MONGO_URI")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
