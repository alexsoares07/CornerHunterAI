from providers.base_provider import BaseProvider
from models.match import Match


class SofaScoreProvider(BaseProvider):

    def get_live_matches(self) -> list[Match]:

        print("🔄 Buscando partidas no SofaScore...")

        return []