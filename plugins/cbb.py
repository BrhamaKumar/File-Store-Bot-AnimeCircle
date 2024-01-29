#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/shidoteshika1'>The king 🜲</a>\n○ Language : <code>Python3</code>\n○ Library : Pyrogram asyncio {__version__}</a>\n○ Support Group : <a href='https://t.me/chatbox480'>Aɴɪᴍᴇ Cɪʀᴄʟᴇ 🜲</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close"),
                        InlineKeyboardButton("⬅️ Back", callback_data = "back")
                    ]
                ]
            )
        )
elif data == "back":
     reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ], [
        InlineKeyboardButton('⛩️ OUR OTHER CHANNELS ⛩️', url='https://t.me/animemoviesr/3171'),
    ]])  
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

 
