from models.match import Match
from providers.base_provider import BaseProvider


class FakeProvider(BaseProvider):

    def get_live_matches(self) -> list[Match]:

        return [

            Match(
                home="Manchester City",
                away="Arsenal",
                minute=82,
                home_score=1,
                away_score=1,
                corners=9,
                dangerous_attacks=92,
                shots=16,
                home_pressure="alta"
            ),

            Match(
                home="Flamengo",
                away="Palmeiras",
                minute=77,
                home_score=0,
                away_score=1,
                corners=8,
                dangerous_attacks=88,
                shots=14,
                home_pressure="alta"
            )

        ]