from zeldris.modules.mongodb.mongo_func import get_served_users
from zeldris.__main__ import STATS
from zeldris import DEV_USERS, pbot as app
from pyrogram import filters

@app.on_message(filters.command("stamts") & filters.user(DEV_USERS))
async def stats_cmd(_, message):
    stats_text = "Current stats:\n" + "\n".join([mod.__stats__() for mod in STATS])
    served_users = str(len(await get_served_users()))
    text = stats_text.replace("USERS_COUNT",served_users)
    await message.reply_text(text)
