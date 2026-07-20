import os
from pathlib import Path

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from analyzer.scanner import scan_matches
from services.telegram_sender import TelegramSender


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("BOT_TOKEN")

print("TOKEN CARREGADO:", TOKEN)


telegram_sender = TelegramSender()

sinais_enviados = set()


async def monitorar(context: ContextTypes.DEFAULT_TYPE):

    print("\n==============================")
    print("MONITORANDO JOGOS...")
    print("==============================")

    jogos = scan_matches()

    print(f"Jogos analisados: {len(jogos)}")

    for jogo in jogos:

        signal = jogo.get("signal")

        if signal is None:
            continue

        chave = (
            signal["match"],
            signal["minute"],
        )

        if chave in sinais_enviados:
            continue

        print("\n🚨 NOVO SINAL")
        print(signal)

        telegram_sender.send(signal)

        sinais_enviados.add(chave)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
🤖 CornerHunter AI ONLINE

Sistema de análise Over Escanteios ativado.

✅ Telegram conectado
✅ Scanner automático ligado
✅ Monitorando jogos ao vivo
"""

    await update.message.reply_text(mensagem)


async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    partidas = scan_matches()

    if not partidas:

        await update.message.reply_text(
            "Nenhum jogo encontrado."
        )

        return

    mensagem = "📊 JOGOS AO VIVO\n\n"

    for jogo in partidas:

        engine = jogo.get("score_engine", {})

        mensagem += (
            f"⚽ {jogo['match']}\n"
            f"⏱ {jogo['minute']}'\n"
            f"📊 {jogo['score']}\n"
            f"🚩 Escanteios: {jogo['corners']['total_corners']}\n"
            f"🔥 Score: {engine.get('score',0)}\n"
            f"{engine.get('level','')}\n\n"
        )

        await update.message.reply_text(mensagem)


async def analisar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    partidas = scan_matches()

    oportunidades = []

    for jogo in partidas:

        signal = jogo.get("signal")

        if signal is not None:
            oportunidades.append(signal)

    if not oportunidades:

        await update.message.reply_text(
            "📊 Nenhuma oportunidade encontrada no momento."
        )

        return

    mensagem = "🚨 OPORTUNIDADES ENCONTRADAS\n\n"

    for signal in oportunidades:

        mensagem += (
            f"⚽ {signal['match']}\n"
            f"⏱ {signal['minute']}'\n"
            f"📊 {signal['result']}\n"
            f"🚩 Escanteios: {signal['corners']['total_corners']}\n"
            f"🔥 Confiança: {signal['confidence']}\n\n"
        )

    await update.message.reply_text(mensagem)


def iniciar_bot():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", jogos))
    app.add_handler(CommandHandler("analisar", analisar))

    # Executa o monitor automaticamente a cada 60 segundos
    app.job_queue.run_repeating(
        monitorar,
        interval=60,
        first=5,
    )

    print("=" * 50)
    print("🤖 Bot Telegram iniciado!")
    print("📡 Monitor automático ligado.")
    print("⏳ Verificando jogos a cada 60 segundos...")
    print("=" * 50)

    app.run_polling()