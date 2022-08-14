from epic import *
from pyrogram import filters
from epic import bot
from pyrogram import *
from pyrogram.types import *
from config import *
from epic.broadcast import broadcast_handler
from database.access_db  import db
from epic.fsub import *


START_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton('📞 HELPS', callback_data="hp")
                 ],
                 [
                 InlineKeyboardButton('✨ ABOUT ✨', callback_data="ab"),
                 InlineKeyboardButton('</ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</>🇱🇰', url="https://t.me/EpicBotsSl")
                 ]])

START_MSG = f"""
🎶 Welcome To Song DownloaderBot ✓

✨You Can download Song & Get lyrics Using This Bot
~ Click to help button to Know more about
"""


HELP = """
**✨How to download Song ?**
Ex :
`/search Justin Bieber lonely`
or normaly send you want song Name

**✨How To Find Lyrics**

Ex : 
`/lyrics justin bieber boyfriend`
"""


M_back = InlineKeyboardMarkup([[
                 InlineKeyboardButton('⏎', callback_data="mback")
                 ]])


ABOUT_TXT = f"""
👀ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝔫𝔞𝔳𝔞𝔫𝔧𝔞𝔫𝔞](https://t.me/NA_VA_N_JA_NA1)
🔥ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [GITᕼᑌᗷ](https://github.com/EpicBotSl/ImNavanjana)
🔰ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
⚡ʙᴀꜱᴇᴅ ᴏɴ : [ᴘʏʀᴏɢʀᴀᴍ](https://pyrogram.org)
🚦ᴍᴀᴅᴇ ᴡɪᴛʜ : [ᴘʏᴛʜᴏɴ](https://python.org)
      [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🇱🇰](https://t.me/EpicBotsSl)
"""

@bot.on_message(filters.command("start"))
async def help(bot, message):
    if await forcesub(bot, message):
       return
    await message.reply_photo("https://telegra.ph/file/ddaed04b00b6a96dbf7bb.jpg", caption=START_MSG, reply_markup=START_BUTTON)

@bot.on_message(filters.command('broadcast') & filters.user(BOT_OWNER))
async def c_status(_, update):
    await broadcast_handler(update)


@bot.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "hp":
         await update.message.edit_text(
             text=HELP,
             reply_markup=M_BACK,
             disable_web_page_preview=True
         )
    elif update.data == "ab":
         await update.message.edit_text(
             text=ABOUT_TXT,
             reply_markup=M_BACK,
             disable_web_page_preview=True
         )
    elif update.data == "mback":
         await update.message.edit_text(
             text=START_MSG,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
