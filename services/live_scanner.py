from sofascore_api import SofaScoreClient
from services.live_analyzer import LiveAnalyzer
from services.score_engine import ScoreEngine
from services.signal_generator import SignalGenerator


class LiveScanner:

    def __init__(self):

        self.sofa = SofaScoreClient()
        self.analyzer = LiveAnalyzer()
        self.score_engine = ScoreEngine()
        self.signal_generator = SignalGenerator()


    def scan_live_matches(self):

        games = self.sofa.get_live_events()

        results = []


        for game in games:

            try:

                # Analisa dados do jogo
                analysis = self.analyzer.analyze_match(game)


                if not analysis:
                    continue


                # Calcula pontuação
                score = self.score_engine.calculate(analysis)


                analysis["score_engine"] = score


                # Gera sinal se atingir critério
                signal = self.signal_generator.generate(analysis)


                if signal:

                    analysis["signal"] = signal


                results.append(analysis)



            except Exception as e:

                print(
                    f"Erro analisando jogo {game.get('id')}: {e}"
                )

                continue



        return results