from services.signal_generator import SignalGenerator


signal = SignalGenerator()


teste = {

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

            "Muitos escanteios"

        ]

    }

}


print(signal.generate(teste))