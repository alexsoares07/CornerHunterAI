from scraper.live_matches import get_live_matches


jogos = get_live_matches()

for jogo in jogos:
    print(jogo)
    