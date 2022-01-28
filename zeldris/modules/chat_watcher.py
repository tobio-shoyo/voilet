from zeldris import pbot as app
from zeldris.modules.mongodb.mongo_func import (add_served_user)

chat_watcher_group = 10

@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    if message.from_user:
        user_id = message.from_user.id
        await add_served_user(user_id)