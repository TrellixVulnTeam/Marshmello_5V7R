import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="alone ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("T")
        await asyncio.sleep(0.7)
        await event.edit("Th")
        await asyncio.sleep(0.7)
        await event.edit("The")
        await asyncio.sleep(0.7)
        await event.edit("The D")
        await asyncio.sleep(0.7)
        await event.edit("The Da")
        await asyncio.sleep(0.7)
        await event.edit("The Day")
        await asyncio.sleep(0.7)
        await event.edit("The Day I")
        await asyncio.sleep(0.7)
        await event.edit("The Day I L")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Le")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Lea")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Lear")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learn")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learnt")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learnt T")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learnt To")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learnt To L")
        await asyncio.sleep(0.7)
        await event.edit("The Day I Learnt To Li")
        await asyncio.sleep(0.7)
 
#      ProBoy Plugins kang with credits 
