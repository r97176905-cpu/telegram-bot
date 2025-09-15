from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main tumhara bot hoon.")

if __name__ == "__main__":
    app = ApplicationBuilder().token("8100257278:AAEw0hQktNR3pCvW5q6CvAHE2qQiPvKsL04").build()
    app.add_handler(CommandHandler("start", start))
    print("Bot chal raha hai...")
    app.run_polling()