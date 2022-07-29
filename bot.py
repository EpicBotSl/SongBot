import config 
from config import *
from script import *
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "Epic Developers",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="module"),
)


if __name__ == "__main__":
    print("⌛Updating & Analyzing bot⏳")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"""@{uname} is Accepted
╔════╗────────╔═══╗
║╔╗╔╗║────────║╔══╝
╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
──────────────────║║
──────────────────╚╝
Join For update @EpicBotsSl""")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")
