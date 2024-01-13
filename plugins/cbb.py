#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
     if data == "start":
        await query.message.edit_text(
            text=Txt.START_MSG.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ], [
        InlineKeyboardButton('⛩️ OUR OTHER CHANNELS ⛩️', url='https://t.me/animemoviesr/3171'),
    ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/shidoteshika1'>The king 🜲</a>\n○ Language : <code>Python3</code>\n○ Library : Pyrogram asyncio {__version__}</a>\n○ Support Group : <a href='https://t.me/chatbox480'>Aɴɪᴍᴇ Cɪʀᴄʟᴇ 🜲</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

 
