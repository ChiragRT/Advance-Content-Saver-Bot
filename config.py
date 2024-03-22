from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28356026")
    API_HASH = environ.get("API_HASH", "5fea2d52ca31906c83cf6ca8fc8a4449")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6687651266:AAHZJ_ntJkVXJkqiyIdXtWH5KSr-2V0raEw") 
    BOT_SESSION = environ.get("BOT_SESSION", "AQGRXhcAkoPAr_kVAtWaQ9s1c9ba5SqqmJQtzpmiBrgHhyxo_5jZDaeW_OjIkSoBA_4YoUfpfan1sB54gYuPw_AlO8bnKnUnIp51h7kcMdR7oblDreYSKUC9qvU1AMpeAU1bMF2L7lXpgbIi0j4mBRNkxsIX6_VzbF2CG6riVJV0t_h0YfRDOQHI0BKgIbdA-Q8L103w01iIPXZ9H8GX45tCrs8hYzoGnSLByjIcKkSYRYFUy06qrMr7r6Jpn0Fkt6tGMwVucGxeUUXvLm5wMZsclXCu4qhmY0Jd5GBNPIBty4_HV9y3spDqqLm1Jl4o74-0K8ak9N2hOwfU5Li_J9B6E0fj2gAAAAGUw4P8AA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ch77651629:60kpzb40FaOf3g4z@cluster0.m7qmg99.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "NEW SAVE RESTRICTED")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6790808572').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
