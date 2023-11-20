#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/Xayonara_Contact_bot'><i><b>⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ亗 Ðя_S𝚃𝚁𝙰𝙽𝙶𝙴</b></i></a>\n📝 ʟᴀɴɢᴜᴀɢᴇ : <code>ᴘʏᴛʜᴏɴ 3</code>\n📚 ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>\n<b>😎 ᴍʏ ꜰʀɪᴇɴᴅ : <a href='https://t.me/abhishekrathoree'>𝐀𝐁𝐇𝐈</a>\n\n <spoiler><b>🔋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - <a href='https://t.me/Xayonara_Contact_bot'>xᴀʏᴏɴᴀʀᴀ</a></b></spoiler>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close")
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
