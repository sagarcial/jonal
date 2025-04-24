from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start"""
    # Texto de bienvenida y menú en un solo mensaje
    text = "¡Bienvenido al bot de códigos!\nSelecciona una opción:"  
    keyboard = [
        [InlineKeyboardButton("Código hogar", callback_data="codigo_hogar"), InlineKeyboardButton("Código de acceso temporal", callback_data="codigo_temporal")],
        [InlineKeyboardButton("Código de inicio de sesión", callback_data="codigo_login"), InlineKeyboardButton("Restablecimiento de contraseña", callback_data="restablecer_contrasena")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja los clicks en los botones del menú"""
    query = update.callback_query
    await query.answer()
    selection = query.data
    # Aquí podrías agregar lógica específica según la selección
    await query.edit_message_text(f"Has seleccionado: {selection}")



def main():
    # Reemplaza 'YOUR_TOKEN_HERE' con el token de tu bot de Telegram
    app = ApplicationBuilder().token('7903121315:AAGVzcwWEGO2HQHIgy7YraQ2hzKJe_sVeGI').build()

    # Handler para el comando /start
    app.add_handler(CommandHandler('start', start))

    # Inicia el bot
    app.run_polling()


if __name__ == '__main__':
    main()
