from sofascore_api import SofaScoreClient

sofa = SofaScoreClient()

jogos = sofa.get_live_events()

jogo = jogos[0]

print(jogo.keys())

print("STATUS:")
print(jogo.get("status"))

print("TIME:")
print(jogo.get("time"))