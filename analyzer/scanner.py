from analyzer.corner_analyzer import CornerAnalyzer
from providers.fake_provider import FakeProvider


class Scanner:

    def __init__(self):

        self.provider = FakeProvider()
        self.analyzer = CornerAnalyzer()

    def scan(self):

        oportunidades = []

        partidas = self.provider.get_live_matches()

        for partida in partidas:

            resultado = self.analyzer.recommendation(partida)

            if resultado["entrada"]:

                oportunidades.append({

                    "home": partida.home,
                    "away": partida.away,
                    "minute": partida.minute,
                    "score": resultado["score"],
                    "nivel": resultado["nivel"],
                    "mercado": resultado["mercado"]

                })

        return oportunidades