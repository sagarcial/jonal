from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start"""
    await update.message.reply_text('¡Bienvenido al bot de códigos!')


def main():
    # Reemplaza 'YOUR_TOKEN_HERE' con el token de tu bot de Telegram
    app = ApplicationBuilder().token('7903121315:AAGVzcwWEGO2HQHIgy7YraQ2hzKJe_sVeGI').build()

    # Handler para el comando /start
    app.add_handler(CommandHandler('start', start))

    # Inicia el bot
    app.run_polling()


if __name__ == '__main__':
    main()
