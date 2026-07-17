from analyzer.corner_analyzer import CornerAnalyzer


jogo = CornerAnalyzer(
    minute=82,
    home_score=1,
    away_score=1,
    corners=9,
    dangerous_attacks=90,
    shots=14,
    home_pressure="alta"
)


resultado = jogo.recommendation()

print(resultado)