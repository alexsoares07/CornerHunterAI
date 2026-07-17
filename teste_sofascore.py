from providers.fake_provider import FakeProvider


provider = FakeProvider()

jogos = provider.get_live_matches()

print("Jogos ao vivo encontrados:")

for jogo in jogos:
    print(jogo)