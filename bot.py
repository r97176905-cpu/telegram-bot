import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main tumhara bot hoon.")

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot chal raha hai...")
    app.run_polling()
