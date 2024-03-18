from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo

from MUSICBABY import app
from MUSICBABY.core.call import BABY
from MUSICBABY.utils import bot_sys_stats
from MUSICBABY.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL


# Define the repo and close buttons
repo_button = InlineKeyboardButton("• ʀᴇᴘᴏ •", callback_data="gib_source")
close_button = InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await BABY.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup(
            [
                [repo_button]
            ]
        ),
    )


@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/b1367262cdfbcd0b2af07.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [close_button]
            ]
        ),
    )
