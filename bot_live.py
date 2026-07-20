import time
import traceback


from providers.betano_provider import BetanoProvider
from services.live_scanner import LiveScanner
from services.telegram_sender import TelegramSender
from services.match_matcher import MatchMatcher

from database.signal_database import SignalDatabase



class CornerHunterBot:


    def __init__(self):


        self.betano = BetanoProvider()


        self.sofa_scanner = LiveScanner()


        self.telegram = TelegramSender()


        self.matcher = MatchMatcher()


        # BANCO DE SINAIS

        self.database = SignalDatabase()



        self.sent_games = set()




    def run_cycle(self):


        print("\n==============================")
        print("BUSCANDO JOGOS BETANO...")
        print("==============================")


        try:

            betano_games = self.betano.get_live_matches()


        except Exception as e:

            print(
                "Erro Betano:",
                e
            )

            return



        print(
            f"TOTAL BETANO: {len(betano_games)}"
        )



        print("\nBUSCANDO SOFASCORE...")



        try:

            sofa_games = self.sofa_scanner.scan_live_matches()


        except Exception as e:

            print(
                "Erro SofaScore:",
                e
            )

            return



        print(
            f"TOTAL ANALISADOS SOFA: {len(sofa_games)}"
        )



        matches = self.matcher.find_matches(
            betano_games,
            sofa_games
        )



        print(
            f"JOGOS COMPATÍVEIS: {len(matches)}"
        )



        print("\n==============================")
        print("ANÁLISES DOS JOGOS")
        print("==============================")



        for item in matches:


            sofa = item.get(
                "sofa",
                {}
            )


            print("\n------------------------------")


            print(
                "JOGO:",
                sofa.get("match")
            )


            print(
                "PLACAR:",
                sofa.get("score")
            )


            print(
                "MINUTO:",
                sofa.get("minute")
            )


            print(
                "ESCANTEIOS:",
                sofa.get("corners")
            )


            print(
                "RITMO:",
                sofa.get("corner_rate")
            )



            score_engine = sofa.get(
                "score_engine",
                {}
            )


            print(
                "PONTOS:",
                score_engine.get("score")
            )


            print(
                "NÍVEL:",
                score_engine.get("level")
            )


            print(
                "MOTIVOS:"
            )


            for motivo in score_engine.get(
                "reasons",
                []
            ):

                print(
                    "-",
                    motivo
                )



            signal = sofa.get(
                "signal"
            )



            if not signal:

                continue



            match_name = signal.get(
                "match"
            )



            if match_name in self.sent_games:

                continue



            print("\nENVIANDO TELEGRAM...")


            resposta = self.telegram.send(
                signal
            )



            if resposta and resposta.get("ok"):



                # SALVA NO BANCO

                self.database.save_signal(
                    signal
                )



                self.sent_games.add(
                    match_name
                )



                print(
                    "\n🚨 SINAL SALVO NO BANCO:",
                    match_name
                )





    def start(self):


        print("""
====================================
🚀 CORNERHUNTER AI INICIADO
====================================
""")


        while True:


            try:

                self.run_cycle()


            except Exception:


                traceback.print_exc()



            print(
                "\nAguardando próxima varredura..."
            )



            time.sleep(
                60
            )







if __name__ == "__main__":


    bot = CornerHunterBot()

    bot.start()