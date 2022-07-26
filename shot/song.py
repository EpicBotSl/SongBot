import os
import requests
import aiohttp
import youtube_dl

from pyrogram.types import *
from pyrogram import Client, filters
from youtube_search import YoutubeSearch

app = Client 

@app.on_message(filters.command("song"))
async def song_commad_group(client, message: Message, _):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SG_B_1"],
                    url=f"https://t.me/epsongbot?start=song",
                ),
            ]
        ]
    )
    await message.reply_text(_["song_1"], reply_markup=upl)


# Song Module


@app.on_message(filters.command("song"))
async def song_commad_private(client, message: Message, _):
    await message.delete()
    url = await YouTube.url(message)
    if url:
        if not await YouTube.exists(url):
            return await message.reply_text(_["song_5"])
        mystic = await message.reply_text(_["play_1"])
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(url)
        if str(duration_min) == "None":
            return await mystic.edit_text(_["song_3"])
        if int(duration_sec) > 400:
            return await mystic.edit_text(
                _["play_4"].format(
                    400, duration_min
                )
            )
        buttons = song_markup(_, vidid)
        await mystic.delete()
        return await message.reply_photo(
            thumbnail,
            caption=_["song_4"].format(title),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["song_2"])
    mystic = await message.reply_text(_["play_1"])
    query = message.text.split(None, 1)[1]
    try:
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(query)
    except:
        return await mystic.edit_text(_["play_3"])
    if str(duration_min) == "None":
        return await mystic.edit_text(_["song_3"])
    if int(duration_sec) > 400:
        return await mystic.edit_text(
            _["play_6"].format(400, duration_min)
        )
    buttons = song_markup(_, vidid)
    await mystic.delete()
    return await message.reply_photo(
        thumbnail,
        caption=_["song_4"].format(title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
