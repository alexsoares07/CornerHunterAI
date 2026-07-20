from services.live_scanner import LiveScanner


scanner = LiveScanner()


jogos = scanner.scan_live_matches()


print("TOTAL ANALISADOS:", len(jogos))


for jogo in jogos:

    print("\n==============================")
    print("PARTIDA:", jogo.get("match"))
    print("PLACAR:", jogo.get("score"))
    print("MINUTO:", jogo.get("minute"))

    print(
        "ESCANTEIOS:",
        jogo.get("corners")
    )

    print(
        "RITMO:",
        jogo.get("corner_rate")
    )

    print(
        "PRESSÃO:",
        jogo.get("pressure_score")
    )


    if "score_engine" in jogo:

        print("\nSCORE ENGINE:")

        print(
            "PONTOS:",
            jogo["score_engine"].get("score")
        )

        print(
            "NÍVEL:",
            jogo["score_engine"].get("level")
        )

        print(
            "MOTIVOS:"
        )

        for motivo in jogo["score_engine"].get("reasons", []):

            print("-", motivo)



    if "signal" in jogo:

        print("\n🚨 SINAL GERADO")

        print(
            jogo["signal"]
        )