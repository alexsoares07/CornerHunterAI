from sofascore_api import SofaScoreClient


sofa = SofaScoreClient()

jogos = sofa.get_live_events()

jogo = jogos[0]


print("ID:", jogo["id"])

print(
    "Jogo:",
    jogo["homeTeam"]["name"],
    "x",
    jogo["awayTeam"]["name"]
)

print(
    "Placar:",
    jogo["homeScore"].get("current"),
    "-",
    jogo["awayScore"].get("current")
)

print(
    "Minuto:",
    jogo.get("time", {}).get("current")
)