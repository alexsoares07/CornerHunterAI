from analyzer.corner_analyzer import CornerAnalyzer
from models.match import Match


match = Match(
    home="Flamengo",
    away="Palmeiras",
    minute=84,
    home_score=1,
    away_score=1,
    corners=10,
    dangerous_attacks=95,
    shots=18,
    home_pressure="alta"
)

analyzer = CornerAnalyzer()

print(analyzer.recommendation(match))