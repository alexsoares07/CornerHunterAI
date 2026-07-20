from services.telegram_sender import TelegramSender
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID



telegram = TelegramSender(
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID
)



teste = {

    "alert": "🚨 OPORTUNIDADE",

    "match": "Viettel U21 x PVF CAND U21",

    "minute": 75,

    "score": "1 - 0",

    "corners": {
        "total_corners": 8
    },

    "confidence": 75,

    "reasons": [
        "Segundo tempo avançado",
        "Muitos escanteios",
        "Ritmo alto"
    ]

}



resultado = telegram.send(teste)


print("RESPOSTA TELEGRAM:")
print(resultado)