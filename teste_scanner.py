from services.live_scanner import LiveScanner


scanner = LiveScanner()


jogos = scanner.scan_live_matches()
print(jogos[0])

print("TOTAL ANALISADOS:", len(jogos))


for jogo in jogos[:5]:

    print("---------------------")
    print(jogo)