from services.telegram_sender import TelegramSender
from services.signal_generator import SignalGenerator



signal_generator = SignalGenerator()

telegram = TelegramSender()



analise = {

    "match": "Torque II x Nacional Reserve",

    "minute": 75,

    "score": "0 - 0",

    "corners": {

        "total_corners": 8

    },

    "score_engine": {

        "score": 80,

        "level": "🟢 OPORTUNIDADE",

        "reasons": [

            "Tempo favorável",

            "Muitos escanteios",

            "Ritmo aceitável"

        ]

    }

}



sinal = signal_generator.generate(
    analise
)



print("\nSINAL GERADO:")
print(sinal)



print("\nENVIANDO TELEGRAM...")


resposta = telegram.send(
    sinal
)



print("\nRESPOSTA TELEGRAM:")
print(resposta)