import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut ! Bot fonctionnel ! 🚀')

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/start , /aide')

def main():
    # Ici on récupère le token depuis les variables d'environnement
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    
    if not TOKEN:
        print("8681412594:AAEMfaMbxzYmOiaYntjudR9HQ2jR9wGl49U")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.run_polling()

if __name__ == '__main__':
    main()
