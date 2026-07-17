import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from analyzer.corner_analyzer import CornerAnalyzer


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN CARREGADO:", TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
🤖 CornerHunter AI ONLINE

Sistema de análise Over Escanteios ativado.

Status:
✅ Telegram conectado
⏳ Aguardando partidas ao vivo
    """

    await update.message.reply_text(mensagem)


async def analisar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    jogo = CornerAnalyzer(
        minute=82,
        home_score=1,
        away_score=1,
        corners=9,
        dangerous_attacks=90,
        shots=14,
        home_pressure="alta"
    )

    resultado = jogo.recommendation()

    if resultado["entrada"]:
        mensagem = f"""
🚨 CORNER HUNTER AI

🚩 OPORTUNIDADE OVER ESCANTEIOS

🎯 Score: {resultado["score"]}/100

Mercado:
{resultado["mercado"]}

🔥 Pressão detectada
⏳ Final de jogo
"""
    else:
        mensagem = f"""
📊 CORNER HUNTER AI

Sem oportunidade.

Score:
{resultado["score"]}/100
"""

    await update.message.reply_text(mensagem)


def iniciar_bot():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )
    app.add_handler(
        CommandHandler("analisar", analisar)
    )

    print("🤖 Bot Telegram iniciado!")

    app.run_polling()