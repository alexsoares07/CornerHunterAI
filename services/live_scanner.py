from sofascore_api import SofaScoreClient

from services.live_analyzer import LiveAnalyzer
from services.score_engine import ScoreEngine
from services.signal_generator import SignalGenerator

import traceback


class LiveScanner:

    def __init__(self):

        self.sofa = SofaScoreClient()

        self.analyzer = LiveAnalyzer()

        self.score_engine = ScoreEngine()

        self.signal_generator = SignalGenerator()

    def scan_live_matches(self):

        try:
            games = self.sofa.get_live_events()
        except Exception as e:
            print(f"Erro buscando jogos ao vivo: {e}")
            return []

        results = []

        for game in games:

            try:

                analysis = self.analyzer.analyze_match(game)

                if analysis is None:
                    continue

                score = self.score_engine.calculate(analysis)

                analysis["score_engine"] = score

                signal = self.signal_generator.generate(analysis)

                if signal is not None:
                    analysis["signal"] = signal

                results.append(analysis)

            except Exception:

                print(f"\n===== ERRO NO JOGO {game.get('id')} =====")
                traceback.print_exc()
                print("=========================================\n")

                continue

        return results