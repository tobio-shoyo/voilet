from pyrogram import filters
import requests as r
from zeldris import pbot as app
from zeldris.utils.errors import capture_err

__mod_name__ = "WebSS"
__help__ = "`/webss` [URL] - Take A Screenshot Of A Webpage"


@app.on_message(filters.command("webss"))
@capture_err
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Give A Url To Fetch Screenshot.")
            return
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        try:
        x = r.get(f"https://webshot.amanoteam.com/print?q={url}")
        if x.status_code != 200:
            return
        else:
            await app.send_photo(
                message.chat.id,
                photo=x,
            )
        except TypeError:
            await m.edit("No Such Website.")
            return
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
