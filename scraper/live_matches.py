class LiveMatch:

    def __init__(
        self,
        home,
        away,
        minute,
        home_score,
        away_score,
        corners,
        dangerous_attacks,
        shots
    ):
        self.home = home
        self.away = away
        self.minute = minute
        self.home_score = home_score
        self.away_score = away_score
        self.corners = corners
        self.dangerous_attacks = dangerous_attacks
        self.shots = shots


    def get_data(self):

        return {
            "home": self.home,
            "away": self.away,
            "minute": self.minute,
            "home_score": self.home_score,
            "away_score": self.away_score,
            "corners": self.corners,
            "dangerous_attacks": self.dangerous_attacks,
            "shots": self.shots
        }



def get_live_matches():

    partidas = [

        LiveMatch(
            home="Manchester City",
            away="Arsenal",
            minute=82,
            home_score=1,
            away_score=1,
            corners=9,
            dangerous_attacks=88,
            shots=15
        )

    ]

    return [
        partida.get_data()
        for partida in partidas
    ]