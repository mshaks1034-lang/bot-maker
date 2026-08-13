import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
MAKER_TOKEN = os.environ.get("MAKER_TOKEN", "")

app = Client("bot_maker", api_id=API_ID, api_hash=API_HASH, bot_token=MAKER_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "👋 **أهلاً بك في مصنع بوتات الحماية المجاني!**\n\n"
        "لإنشاء بوت حماية خاص بك، أرسل لي **Token** البوت الخاص بك (الذي استخرجته من @BotFather):",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("قناة المطور", url="https://t.me/your_channel")]
        ])
    )

@app.on_message(filters.text & filters.private & ~filters.command("start"))
async def make_bot(client, message):
    token = message.text.strip()
    if ":" in token and len(token) > 15:
        await message.reply_text(
            "✅ **تم استلام التوكن بنجاح!**\n\n"
            "⚠️ جاري تفعيل بوت الحماية الخاص بك على السيرفر...\n\n"
            f"🔹 التوكن المستلم: `{token}`"
        )
    else:
        await message.reply_text("❌ **التوكن غير صحيح!** يرجى التأكد وإرسال توكن صالح من @BotFather.")

app.run()
