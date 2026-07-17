from providers.fake_provider import FakeProvider


class MatchService:

    def __init__(self):
        self.provider = SofaScoreProvider()

    def get_matches(self):
        return self.provider.get_live_matches()