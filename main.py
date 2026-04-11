import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut ! Bot fonctionnel sur Pella ! 🚀')

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('📋 Commandes :\n/start - Démarrer\n/aide - Aide')

def main():
    # Récupère le token depuis les variables d'environnement
    TOKEN = os.environ.get('8620189640:AAEkSY8UoguoGPnMsJPreKtuAm_v8C2l3X4')
    
    if not TOKEN:
        print("❌ ERREUR : Token Telegram non trouvé !")
        return
    
    # Crée l'application
    app = Application.builder().token(TOKEN).build()
    
    # Ajoute les commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    
    print("✅ Bot démarré avec succès !")
    app.run_polling()

if __name__ == '__main__':
    main()
