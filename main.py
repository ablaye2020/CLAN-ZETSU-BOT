import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

print(f"🤖 Démarrage du bot avec token: {TOKEN[:10]}...")  # Affiche le début du token pour vérifier

async def start(update: Update, context):
    await update.message.reply_text(
        "⚔️ BIENVENUE DANS LE CLAN ZETSU ! ⚔️\n\n"
        "🔥 Le plus puissant des clans 🔥\n\n"
        "📜 Commandes :\n"
        "/regles - Les règles du clan\n"
        "/membres - Liste des membres\n"
        "/event - Prochains événements\n"
        "/chef - Message du chef"
    )

async def regles(update: Update, context):
    await update.message.reply_text(
        "📜 RÈGLES DU CLAN ZETSU :\n\n"
        "1️⃣ Respect entre tous les membres\n"
        "2️⃣ Activité régulière obligatoire\n"
        "3️⃣ Entraide et partage\n"
        "4️⃣ Pas de spam ni d'insultes\n\n"
        "⚔️ Ensemble, nous sommes plus forts !"
    )

async def membres(update: Update, context):
    await update.message.reply_text(
        "👥 MEMBRES DU CLAN ZETSU :\n\n"
        "👑 Chef : Zetsu\n"
        "⚔️ Co-chefs : À venir\n"
        "🛡️ Élites : À venir\n"
        "🎖️ Membres : Toi peut-être ?\n\n"
        "Rejoins-nous ! 🔥"
    )

async def event(update: Update, context):
    await update.message.reply_text(
        "📅 PROCHAINS ÉVÉNEMENTS :\n\n"
        "🎮 Tournoi hebdomadaire : Samedi 20h\n"
        "💬 Réunion du clan : Dimanche 18h\n"
        "🏆 Compétition mensuelle : À venir\n\n"
        "Ne manque rien ! ⚔️"
    )

async def chef(update: Update, context):
    await update.message.reply_text(
        "👑 MESSAGE DU CHEF :\n\n"
        "Fier de vous avoir dans le clan !\n"
        "Continuez comme ça et ensemble,\n"
        "nous deviendrons les meilleurs ! 🔥\n\n"
        "- Zetsu"
    )

async def repondre(update: Update, context):
    await update.message.reply_text(
        "🤖 Je suis le bot officiel du Clan Zetsu !\n"
        "Tape /start pour voir les commandes ⚔️"
    )

def main():
    print("⚔️ Initialisation du bot Clan Zetsu...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("regles", regles))
    app.add_handler(CommandHandler("membres", membres))
    app.add_handler(CommandHandler("event", event))
    app.add_handler(CommandHandler("chef", chef))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))
    
    print("🤖 Bot du Clan ZETSU en ligne ! ⚔️")
    app.run_polling()

if __name__ == "__main__":
    main()
