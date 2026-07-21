import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from analyzer.scanner import scan_matches


# ==============================
# CONFIGURAÇÃO
# ==============================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("BOT_TOKEN")


print("=" * 50)
print("TOKEN CARREGADO COM SUCESSO")
print("=" * 50)


if not TOKEN:
    raise Exception("TOKEN DO TELEGRAM NÃO ENCONTRADO")


# ==============================
# CONTROLE DE SINAIS
# ==============================

CHAT_ID = None

ENVIADOS = set()


SCORE_MINIMO = 50



# ==============================
# START TELEGRAM
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global CHAT_ID

    CHAT_ID = update.effective_chat.id

    await update.message.reply_text(
        "🤖 CornerHunter AI conectado!\n\n"
        "📡 Monitor de escanteios ativado.\n"
        f"🎯 Score mínimo: {SCORE_MINIMO}"
    )

    print("CHAT ID SALVO:", CHAT_ID)



# ==============================
# MONITOR
# ==============================


async def monitor():

    global CHAT_ID


    while True:

        try:

            print("\n")
            print("=" * 30)
            print("MONITORANDO JOGOS...")
            print("=" * 30)


            jogos = scan_matches()


            print("Jogos analisados:", len(jogos))


            for jogo in jogos:


                score = jogo.get(
                    "score",
                    jogo.get("score_engine", {}).get("score",0)
                )


                nome = jogo.get(
                    "jogo",
                    jogo.get("match","")
                )


                minuto = jogo.get("minuto",0)

                cantos = jogo.get(
                    "escanteios",
                    jogo.get("corners",{}).get("total_corners",0)
                )


                print("\nANALISE:")
                print(jogo)



                if score >= SCORE_MINIMO:


                    chave = nome


                    if chave not in ENVIADOS:


                        mensagem = (
                            "🔥 CORNERHUNTER AI - SINAL\n\n"
                            f"⚽ Jogo: {nome}\n"
                            f"⏱ Minuto: {minuto}'\n"
                            f"🚩 Escanteios: {cantos}\n"
                            f"📊 Score: {score}\n\n"
                            "🎯 Entrada: Over Escanteios"
                        )


                        print("\nENVIANDO SINAL:")
                        print(mensagem)



                        if CHAT_ID:


                            await app.bot.send_message(
                                chat_id=CHAT_ID,
                                text=mensagem
                            )

                            print("✅ SINAL ENVIADO TELEGRAM")


                        else:

                            print(
                                "⚠️ CHAT_ID ainda não conectado"
                            )


                        ENVIADOS.add(chave)



            print("\nAguardando 60 segundos...")


        except Exception as e:

            print(
                "ERRO MONITOR:",
                e
            )


        await asyncio.sleep(60)



# ==============================
# INICIAR BOT
# ==============================


async def iniciar():

    global app


    app = (
        Application
        .builder()
        .token(TOKEN)
        .connect_timeout(60)
        .read_timeout(60)
        .write_timeout(60)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    print("=" * 50)
    print("🤖 CornerHunter AI iniciado!")
    print("📡 Monitor automático ligado.")
    print("⏳ Scanner a cada 60 segundos.")
    print("=" * 50)



    await app.initialize()

    await app.start()

    await app.updater.start_polling()


    asyncio.create_task(
        monitor()
    )


    await asyncio.Event().wait()



# ==============================
# EXECUÇÃO
# ==============================


if __name__ == "__main__":

    asyncio.run(
        iniciar()
    )