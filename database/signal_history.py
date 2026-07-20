import sqlite3



class SignalHistory:


    def __init__(self):

        self.conn = sqlite3.connect(
            "database/signals.db"
        )



    def show_all(self):


        cursor = self.conn.cursor()


        cursor.execute(
            """
            SELECT *
            FROM signals
            ORDER BY id DESC
            """
        )


        rows = cursor.fetchall()



        if not rows:

            print(
                "Nenhum sinal salvo."
            )

            return



        print("\n==============================")
        print("HISTÓRICO DE SINAIS")
        print("==============================")



        for row in rows:


            print("\n------------------------------")


            print(
                "ID:",
                row[0]
            )


            print(
                "JOGO:",
                row[1]
            )


            print(
                "MINUTO:",
                row[2]
            )


            print(
                "PLACAR:",
                row[3]
            )


            print(
                "ESCANTEIOS:",
                row[4]
            )


            print(
                "CONFIANÇA:",
                row[5]
            )


            print(
                "DATA:",
                row[8]
            )



    def statistics(self):


        cursor = self.conn.cursor()



        cursor.execute(
            """
            SELECT COUNT(*),
            AVG(confidence)
            FROM signals
            """
        )


        result = cursor.fetchone()



        print("\n==============================")
        print("ESTATÍSTICAS")
        print("==============================")


        print(
            "Total de sinais:",
            result[0]
        )


        print(
            "Confiança média:",
            round(
                result[1] or 0,
                2
            )
        )