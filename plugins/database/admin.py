import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from plugins.config import Config
from pyrogram import Client
from plugins.database.database import db
from plugins.functions.display_progress import humanbytes
from plugins.database.bcast import broadcast_handler




@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
