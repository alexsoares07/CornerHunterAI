from models.match import Match


jogo = Match(
    home="Flamengo",
    away="Palmeiras",
    minute=83,
    home_score=1,
    away_score=1,
    corners=9,
    dangerous_attacks=92,
    shots=17,
    home_pressure="alta"
)

print(jogo)
