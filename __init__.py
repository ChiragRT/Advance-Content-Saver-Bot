#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("API_ID", default=28356026, cast=int)
API_HASH = config("API_HASH", default=5fea2d52ca31906c83cf6ca8fc8a4449)
BOT_TOKEN = config("BOT_TOKEN", default=6687651266:AAHZJ_ntJkVXJkqiyIdXtWH5KSr-2V0raEw)
SESSION = config("SESSION", default=AQGRXhcAkoPAr_kVAtWaQ9s1c9ba5SqqmJQtzpmiBrgHhyxo_5jZDaeW_OjIkSoBA_4YoUfpfan1sB54gYuPw_AlO8bnKnUnIp51h7kcMdR7oblDreYSKUC9qvU1AMpeAU1bMF2L7lXpgbIi0j4mBRNkxsIX6_VzbF2CG6riVJV0t_h0YfRDOQHI0BKgIbdA-Q8L103w01iIPXZ9H8GX45tCrs8hYzoGnSLByjIcKkSYRYFUy06qrMr7r6Jpn0Fkt6tGMwVucGxeUUXvLm5wMZsclXCu4qhmY0Jd5GBNPIBty4_HV9y3spDqqLm1Jl4o74-0K8ak9N2hOwfU5Li_J9B6E0fj2gAAAAGUw4P8AA)
FORCESUB = config("FORCESUB", default=dkdjddhsj)
AUTH = config("AUTH", default=6790808572)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
