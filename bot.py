from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Reemplaza con el token que obtuviste de BotFather
TOKEN = ""
CHAT_ID = ''  # Usa el chat ID obtenido

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Enviar mensaje al chat específico
    await context.bot.send_message(chat_id=CHAT_ID, text="¡Hola! Soy tu bot de Telegram.")

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Usa /start para iniciar la interacción conmigo.')

def main():
    # Crea una aplicación con tu token
    application = Application.builder().token(TOKEN).build()

    # Registra los comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()