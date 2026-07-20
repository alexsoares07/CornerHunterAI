from services.entry_engine import EntryEngine


engine = EntryEngine()


analysis = {

    "minute": 80,

    "corners": {

        "total_corners": 7

    }

}


resultado = engine.generate_entry(
    analysis,
    80
)


print(resultado)