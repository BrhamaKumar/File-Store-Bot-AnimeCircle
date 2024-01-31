#(©)Codexbotz

from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
                        text = f"<b>About this Bot:\n\n  A Telegram Bot for storing posts or files that can be accessed via a Special Link.\n\n👨‍💻 Modified by @Contactpkbot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("○ My Owner ○", url = "https://t.me/Contactpkbot")
                    ],[
                        InlineKeyboardButton('Movie Group', url = 'https://t.me/funnyzilla'),
InlineKeyboardButton('Latest Uploads', url = 'https://t.me/+nkkO3SNnQOs4NzJl')
                    ],[
                        InlineKeyboardButton("🔒 Close 🔒", callback_data = "close")
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
                 
