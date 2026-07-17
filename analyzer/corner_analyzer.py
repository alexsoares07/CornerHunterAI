class CornerAnalyzer:
    def __init__(
        self,
        minute,
        home_score,
        away_score,
        corners,
        dangerous_attacks,
        shots,
        home_pressure
    ):
        self.minute = minute
        self.home_score = home_score
        self.away_score = away_score
        self.corners = corners
        self.dangerous_attacks = dangerous_attacks
        self.shots = shots
        self.home_pressure = home_pressure

    def calculate_score(self):

        score = 0

        # Minutos finais têm maior chance de pressão
        if self.minute >= 75:
            score += 25
        elif self.minute >= 60:
            score += 15

        # Time da casa perdendo ou empatando
        if self.home_score <= self.away_score:
            score += 20

        # Quantidade de escanteios
        if self.corners >= 8:
            score += 20
        elif self.corners >= 6:
            score += 10

        # Ataques perigosos
        if self.dangerous_attacks >= 80:
            score += 15
        elif self.dangerous_attacks >= 50:
            score += 8

        # Finalizações
        if self.shots >= 12:
            score += 10
        elif self.shots >= 8:
            score += 5

        # Pressão da equipe da casa
        if self.home_pressure == "alta":
            score += 10

        return min(score, 100)


    def recommendation(self):

        score = self.calculate_score()

        if score >= 80:
            return {
                "entrada": True,
                "score": score,
                "mercado": "Over Escanteios"
            }

        return {
            "entrada": False,
            "score": score,
            "mercado": "Sem oportunidade"
        }