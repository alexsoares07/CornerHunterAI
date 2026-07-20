import os
import json
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


# ==============================
# CONFIGURAÇÃO
# ==============================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


TOKEN = os.getenv("BOT_TOKEN")


print("TOKEN CARREGADO:", TOKEN)


telegram_sender = TelegramSender()



# ==============================
# MEMÓRIA DOS SINAIS
# ==============================

ARQUIVO_SINAIS = BASE_DIR / "sinais_enviados.json"



def carregar_sinais():

    if ARQUIVO_SINAIS.exists():

        with open(
            ARQUIVO_SINAIS,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return set(json.load(arquivo))

    return set()



def salvar_sinais():

    with open(
        ARQUIVO_SINAIS,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            list(sinais_enviados),
            arquivo,
            indent=4
        )



sinais_enviados = carregar_sinais()



# ==============================
# MONITOR AUTOMÁTICO
# ==============================

async def monitorar(context: ContextTypes.DEFAULT_TYPE):

    print("\n==============================")
    print("MONITORANDO JOGOS...")
    print("==============================")


    jogos = scan_matches()


    print(
        f"Jogos analisados: {len(jogos)}"
    )


    for jogo in jogos:


        signal = jogo.get("signal")


        if signal is None:
            continue



        event_id = signal.get(
            "event_id"
        )



        if event_id is None:

            print(
                "⚠️ Sinal sem event_id ignorado"
            )

            continue



        if event_id in sinais_enviados:

            print(
                f"⏭️ Sinal já enviado: {event_id}"
            )

            continue



        print("\n🚨 NOVO SINAL")

        print(signal)



        telegram_sender.send(
            signal
        )



        sinais_enviados.add(
            event_id
        )


        salvar_sinais()




# ==============================
# COMANDO START
# ==============================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    mensagem = """
🤖 CornerHunter AI ONLINE

Sistema Over Escanteios ativado.

✅ Telegram conectado
✅ Scanner automático ligado
✅ Monitorando jogos ao vivo
"""


    await update.message.reply_text(
        mensagem
    )




# ==============================
# COMANDO JOGOS
# ==============================

async def jogos(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    partidas = scan_matches()


    if not partidas:

        await update.message.reply_text(
            "Nenhum jogo encontrado."
        )

        return



    mensagem = "📊 JOGOS AO VIVO\n\n"



    for jogo in partidas:


        engine = jogo.get(
            "score_engine",
            {}
        )


        mensagem += (
            f"⚽ {jogo.get('match')}\n"
            f"⏱ {jogo.get('minute')}'\n"
            f"🚩 Escanteios: "
            f"{jogo.get('corners',{}).get('total_corners',0)}\n"
            f"🔥 Score: {engine.get('score',0)}\n\n"
        )


    await update.message.reply_text(
        mensagem
    )




# ==============================
# COMANDO ANALISAR
# ==============================

async def analisar(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    partidas = scan_matches()


    oportunidades = []


    for jogo in partidas:


        signal = jogo.get(
            "signal"
        )


        if signal:

            oportunidades.append(
                signal
            )



    if not oportunidades:

        await update.message.reply_text(
            "📊 Nenhuma oportunidade encontrada."
        )

        return



    mensagem = (
        "🚨 OPORTUNIDADES\n\n"
    )


    for signal in oportunidades:


        mensagem += (
            f"⚽ {signal['match']}\n"
            f"⏱ {signal['minute']}'\n"
            f"🚩 Cantos: "
            f"{signal['corners']['total_corners']}\n"
            f"🔥 Confiança: "
            f"{signal['confidence']}\n\n"
        )


    await update.message.reply_text(
        mensagem
    )




# ==============================
# INICIAR BOT
# ==============================

def iniciar_bot():


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CommandHandler(
            "jogos",
            jogos
        )
    )


    app.add_handler(
        CommandHandler(
            "analisar",
            analisar
        )
    )



    app.job_queue.run_repeating(
        monitorar,
        interval=60,
        first=5
    )



    print("=" * 50)
    print("🤖 Bot Telegram iniciado!")
    print("📡 Monitor automático ligado.")
    print("⏳ Verificando jogos a cada 60 segundos...")
    print("=" * 50)



    app.run_polling()




# ==============================
# EXECUÇÃO
# ==============================

if __name__ == "__main__":

    iniciar_bot()