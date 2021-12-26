import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from zeldris import client as telethn
from zeldris.events import register as nobara

from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown


@nobara(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    reason = str(event.pattern_match.group(1)).strip()
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions = [mention_markdown(x.id, unicode_truncate(x.username, 100), version=2)]
        for chunk in chunks(mentions, 1000):
            message = reason.join(chunk)
    await event.reply(message)
    await event.delete()


@nobara(pattern="^/users ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n @{x.username}"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()



def chunks(elements, size):
    n = max(1, size)
    return (elements[i:i + n] for i in range(0, len(elements), n))


def unicode_truncate(s, length, encoding='utf-8'):
    encoded = s.encode(encoding)[:length]
    return encoded.decode(encoding, 'ignore')




__mod_name__ = "Tagger"
__help__ = """
  ➢ `/tagall : Tag everyone in a chat
"""
