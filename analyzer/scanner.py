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

        jogos = self.sofa.get_live_events()

        resultados = []


        for jogo in jogos:


            # ==============================
            # FILTRO SOMENTE JOGOS AO VIVO
            # ==============================

            status = jogo.get("status", {})


            if isinstance(status, dict):

                tipo_status = status.get("type")


                if tipo_status != "inprogress":

                    continue



            # ==============================
            # ADICIONA ID ÚNICO DA PARTIDA
            # ==============================

            event_id = jogo.get("id")


            if event_id is None:

                continue



            analysis = self.analyzer.analyze_match(jogo)


            if analysis is None:

                continue



            # Guarda o ID dentro da análise

            analysis["event_id"] = event_id



            score = self.score_engine.calculate(
                analysis
            )


            analysis["score_engine"] = score



            signal = self.signal_generator.generate(
                analysis
            )



            if signal is not None:


                # envia o ID junto no sinal

                signal["event_id"] = event_id


                analysis["signal"] = signal



            resultados.append(
                analysis
            )


        return resultados



def scan_matches():

    scanner = LiveScanner()

    return scanner.scan_live_matches()