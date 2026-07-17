from pysofascore import SofaScore

from providers.base_provider import BaseProvider
from models.match import Match


class SofaScoreProvider(BaseProvider):

    def __init__(self):

        self.sofa = SofaScore()


    def get_live_matches(self) -> list[Match]:

        events = self.sofa.get_live_events()

        matches = []


        for event in events:

            match = Match(

                home=event["homeTeam"]["name"],

                away=event["awayTeam"]["name"],

                minute=event.get("time", {}).get("current", 0),

                home_score=event["homeScore"]["current"],

                away_score=event["awayScore"]["current"],

                corners=0,

                dangerous_attacks=0,

                shots=0,

                home_pressure="normal"

            )

            matches.append(match)


        return matches