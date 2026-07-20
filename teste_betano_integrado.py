from providers.betano_provider import BetanoProvider
from services.live_scanner import LiveScanner
from services.match_matcher import MatchMatcher



betano = BetanoProvider()

sofa = LiveScanner()

matcher = MatchMatcher()



jogos_betano = betano.get_live_matches()

jogos_sofa = sofa.scan_live_matches()



print("\n====== BETANO ======")


for jogo in jogos_betano:

    print(
        jogo["home"],
        "x",
        jogo["away"]
    )



print("\n====== SOFASCORE ======")


for jogo in jogos_sofa:

    print(
        jogo["match"]
    )



print("\n====== TESTE MATCH ======")


resultado = matcher.find_matches(
    jogos_betano,
    jogos_sofa
)


print(resultado)