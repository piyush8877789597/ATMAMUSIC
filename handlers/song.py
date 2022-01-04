#BHATAKTI_ATMA 

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)


@Client.on_message(filters.command("song") & ~filters.edited)
async def song(client, message):
    cap = "**💥 𝚂𝙾𝙽𝙶🎸𝚄𝙿𝙻𝙾𝙰𝙳𝙴𝙳💿 𝙱𝚈✌\n🔊 [𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸 🇮🇳 𝙰𝚃𝙼𝙰 💞 𝙼𝚄𝚂𝙸𝙲](https://t.me/lovely_friends_2) 🌷 ...**"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("**🔍 Sɘɑɤƈɦɩɳʛ ...**")
    if not url:
        await rkp.edit("**💥𝙰𝙱𝙱𝙴 𝙱𝙷𝙰𝙸 𝚈𝙰 𝚄𝚂𝙺𝙸 𝙱𝙷𝙴𝙽💞𝚂𝙾𝙽𝙶🔐𝙺𝙰🤞\n🎸𝙽𝙰𝙰𝙼🤟𝙱𝚃𝙰🌷 ...**")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("**❌ 𝙽𝙾𝙸 😬𝙼𝙸𝙻𝙰 𝚈𝙴 𝚂𝙾𝙽𝙶 𝙼𝚄𝙹𝙷𝙴😑...**")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("**🔁 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("**📤 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙷𝙾 𝚁𝙷𝙰 𝙷 ...**"),
        lol = "./etc/tg_vc_bot.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)
        await rkp.delete()
