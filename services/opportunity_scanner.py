from providers.betano_provider import BetanoProvider
from services.live_scanner import LiveScanner
from services.match_matcher import MatchMatcher
from services.score_engine import ScoreEngine



class OpportunityScanner:


    def __init__(self):

        self.betano = BetanoProvider()

        self.sofa = LiveScanner()

        self.matcher = MatchMatcher()

        self.score = ScoreEngine()



    def scan(self):


        oportunidades = []


        jogos_betano = (
            self.betano.get_live_matches()
        )


        jogos_sofa = (
            self.sofa.scan_live_matches()
        )



        encontrados = self.matcher.find_matches(

            jogos_betano,

            jogos_sofa

        )



        for jogo in encontrados:


            sofa_data = jogo["sofa"]


            pontos = self.score.calculate(
                sofa_data
            )


            oportunidades.append({

                "betano": jogo["betano"],

                "sofa": sofa_data,

                "score": pontos

            })



        return oportunidades