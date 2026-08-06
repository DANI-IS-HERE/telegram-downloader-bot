import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Njan Downloader Bot aanu.\n"
        "🔗 Oru link ayakkuka, njan process cheyyam."
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.startswith("http"):
        await update.message.reply_text(
            "⏳ Link kitti!\n"
            "Processing start cheyyunnu..."
        )
    else:
        await update.message.reply_text(
            "❌ Please oru valid link ayakkuka."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link)
)

print("Bot Running...")

app.run_polling()