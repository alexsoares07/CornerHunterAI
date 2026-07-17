from config import *
from models.match import Match


class ScoreEngine:

    def calculate(self, match: Match) -> int:

        score = 0

        # Minuto
        if match.minute >= MIN_MINUTE + 5:
            score += 25
        elif match.minute >= MIN_MINUTE:
            score += 20
        elif match.minute >= 65:
            score += 10

        # Situação do placar
        if match.home_score < match.away_score:
            score += 20
        elif match.home_score == match.away_score:
            score += 15

        # Escanteios
        if match.corners >= MIN_CORNERS + 1:
            score += 20
        elif match.corners >= MIN_CORNERS - 1:
            score += 12

        # Ataques perigosos
        if match.dangerous_attacks >= 90:
            score += 20
        elif match.dangerous_attacks >= 70:
            score += 12

        # Finalizações
        if match.shots >= 15:
            score += 10
        elif match.shots >= 10:
            score += 5

        # Pressão
        if match.home_pressure.lower() == "alta":
            score += 10

        return min(score, 100)