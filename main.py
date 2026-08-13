import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID", "20400000"))
API_HASH = os.environ.get("API_HASH", "123456789abcdef")
MAKER_TOKEN = os.environ.get("MAKER_TOKEN", "")

app = Client("bot_maker", api_id=API_ID, api_hash=API_HASH, bot_token=MAKER_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "👋 **أهلاً بك عزيزي المطور!**\n\n"
        "✨ تم تشغيل البوت بنجاح على السيرفر.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("قناة المطور", url="https://t.me/your_channel")]
        ])
    )

app.run()
