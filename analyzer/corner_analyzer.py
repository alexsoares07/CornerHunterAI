from analyzer.score_engine import ScoreEngine
from models.match import Match


class CornerAnalyzer:

    def __init__(self):

        self.engine = ScoreEngine()

    def recommendation(self, match: Match):

        score = self.engine.calculate(match)

        if score >= 90:
            nivel = "🔥 Premium"

        elif score >= 80:
            nivel = "🟢 Excelente"

        elif score >= 70:
            nivel = "🟡 Boa"

        else:
            nivel = "🔴 Sem entrada"

        return {
            "entrada": score >= 80,
            "score": score,
            "nivel": nivel,
            "mercado": "Over Escanteios"
        }