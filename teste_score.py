from analyzer.score_engine import ScoreEngine
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

engine = ScoreEngine()

print(engine.calculate(match))