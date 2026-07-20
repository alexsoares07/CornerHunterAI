from providers.betano_provider import BetanoProvider
from services.live_scanner import LiveScanner
from services.match_matcher import MatchMatcher


class BetanoOpportunityScanner:


    def __init__(self):

        self.betano = BetanoProvider()

        self.sofa = LiveScanner()

        self.matcher = MatchMatcher()



    def scan(self):


        print("\nBUSCANDO JOGOS BETANO...")


        betano_games = (
            self.betano.get_live_matches()
        )



        print(
            "TOTAL BETANO:",
            len(betano_games)
        )



        print("\nBUSCANDO JOGOS SOFASCORE...")


        sofa_games = (
            self.sofa.scan_live_matches()
        )



        print(
            "TOTAL SOFASCORE:",
            len(sofa_games)
        )



        matches = self.matcher.find_matches(

            betano_games,

            sofa_games

        )



        print(
            "\nJOGOS COMPATÍVEIS:",
            len(matches)
        )



        resultados = []



        for item in matches:


            resultados.append(

                item["sofa"]

            )



        return resultados