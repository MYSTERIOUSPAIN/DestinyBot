import os
import urllib

import aiohttp
import requests
from pyrogram import filters
from DestinyBot import pbot


@pbot.on_message(filters.command("meme"))
async def memes(client, message):
    async with aiohttp.ClientSession() as destiny_session:
        async with destiny_session.get(
            "https://meme-api.herokuapp.com/gimme/wholesomememes"
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])

@pbot.on_message(filters.command("cursed"))
async def cursedmemes(client, message):
    async with aiohttp.ClientSession() as destiny_session:
        async with destiny_session.get(
            "https://meme-api.herokuapp.com/gimme/cursedcomments"
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])

@pbot.on_message(filters.command("shitpost"))
async def shitpost(client, message):
    async with aiohttp.ClientSession() as destiny_session:
        async with destiny_session.get(
            "https://meme-api.herokuapp.com/gimme/shitposting"
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])
_help_ = """
*Memes*
Note: This module utilizes meme-api.heroku.com, which uses reddit as a source.
 ✮ `/meme`*:* To get random wholesome memes from subreddit r/wholesomememes.
 ✮ `/cursed`*:* To get random Cursed Comments posts from the subreddit r/cursedcomments.
 ✮ `/shitpost`*:* To get random memes from subreddit r/shitposting.
"""

__mod_name__ = "Memes"