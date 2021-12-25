from pyrogram import filters
import requests as r
from zeldris import pbot as app

mod_name = "WebSS"
help = "/webss [URL] - Take A Screenshot Of A Webpage"



@app.on_message(filters.command("webss"))
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Give A Url To Fetch Screenshot.")
            return
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("Taking Screenshot")
        await m.edit("Uploading")
        try:
            x = r.get(f"https://webshot.amanoteam.com/print?q={url}")
            await app.send_photo(
                       message.chat.id,
                       photo=x)
        except TypeError:
            await m.edit("No Such Website.")
            return
            await m.delete()
        
    except Exception as e:
        await message.reply_text(str(e))
