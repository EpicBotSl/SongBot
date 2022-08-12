from aiogram import types
from epic import *
from pyrogram import filters
from pyrogram import *
from pyrogram.types import *
from epic.covert import NotFoundTrack
from epic.covert import Track
from epic import bot 


@bot.on_message(filters.audio)
async def start(client, message):
async def recognize_song(message: types.Message):
    voice = await message.voice.download()
    info = await shazam.recognize_song(voice.name)
    try:
        serialized_track = Track(info)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=serialized_track.image,
                             caption=f"Трек: {serialized_track.subtitle} - {serialized_track.title}\n"
                                     f"[Слушать в Apple Music]({serialized_track.appleMusic_url})\n",
                             parse_mode='Markdown')
    except NotFoundTrack:
        await bot.send_message(chat_id=message.from_user.id, text='Не удалось найти песню. Попробуйте еще раз.')
