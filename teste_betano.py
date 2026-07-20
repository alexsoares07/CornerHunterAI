from providers.betano_provider import BetanoProvider


betano = BetanoProvider()


jogos = betano.get_live_matches()


print("\nRESULTADO FINAL")

for jogo in jogos[:10]:

    print("----------------")

    print(jogo)