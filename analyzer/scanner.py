from analyzer.corner_analyzer import CornerAnalyzer
from scraper.live_matches import get_live_matches


def scan_matches():

    jogos = get_live_matches()

    oportunidades = []

    for jogo in jogos:

        analise = CornerAnalyzer(
            minute=jogo["minute"],
            home_score=jogo["home_score"],
            away_score=jogo["away_score"],
            corners=jogo["corners"],
            dangerous_attacks=jogo["dangerous_attacks"],
            shots=jogo["shots"],
            home_pressure="alta"
        )

        resultado = analise.recommendation()

        if resultado["entrada"]:
            oportunidades.append(
                {
                    "jogo": f'{jogo["home"]} x {jogo["away"]}',
                    "score": resultado["score"],
                    "mercado": resultado["mercado"]
                }
            )

    return oportunidades