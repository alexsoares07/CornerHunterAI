from sofascore_api import SofaScoreClient
from services.live_analyzer import LiveAnalyzer


sofa = SofaScoreClient()

analyzer = LiveAnalyzer()


jogos = sofa.get_live_events()


resultado = analyzer.analyze_match(jogos[0])


print(resultado)