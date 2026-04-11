import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuration des logs pour voir ce qui se passe
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Je suis ton bot et je fonctionne parfaitement ! 🚀")

# Commande /aide
async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Commandes disponibles :\n/start - Démarrer le bot\n/aide - Voir cette aide")

# Commande /ping (pour tester)
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong ! Le bot est bien vivant !")

def main():
    # Récupère le token depuis les variables d'environnement de Pella
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        print("8681412594:AAEMfaMbxzYmOiaYntjudR9HQ2jR9wGl49U")
        return
    
    print(f"✅ Token trouvé (longueur: {len(TOKEN)} caractères)")
    
    # Crée l'application
    app = Application.builder().token(TOKEN).build()
    
    # Ajoute les commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("ping", ping))
    
    print("🚀 Bot démarré ! En attente de messages...")
    
    # Lance le bot
    app.run_polling()

if __name__ == "__main__":
    main()
