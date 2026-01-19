import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Il token viene preso dalle Environment Variables (Render)
TOKEN = os.environ.get("BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao! 👋\n"
        "Sono un bot automatico.\n\n"
        "Puoi lasciare qui il tuo messaggio e ti risponderò appena possibile ✅"
    )

# Risposta automatica a QUALSIASI messaggio
async def auto_reply(update: Update, context: Contex_
