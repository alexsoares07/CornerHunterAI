from services.entry_engine import EntryEngine


class SignalGenerator:

    def __init__(self):

        self.entry_engine = EntryEngine()



    def generate(self, analysis):


        engine = analysis.get(
            "score_engine",
            {}
        )


        score = engine.get(
            "score",
            0
        )


        level = engine.get(
            "level",
            ""
        )


        reasons = engine.get(
            "reasons",
            []
        )



        # Apenas oportunidades reais

        if level != "🟢 OPORTUNIDADE":

            return None



        corners = analysis.get(
            "corners",
            {}
        )



        # GERA A ENTRADA

        entry = self.entry_engine.generate_entry(
            analysis,
            score
        )



        return {


            "event_id": analysis.get(
                "event_id"
            ),


            "alert": "🚨 OPORTUNIDADE DE CANTOS",



            "match": analysis.get(
                "match",
                "Jogo desconhecido"
            ),



            "minute": analysis.get(
                "minute",
                0
            ),



            "result": analysis.get(
                "score",
                "0 - 0"
            ),



            "corners": {


                "home_corners": corners.get(
                    "home_corners",
                    0
                ),


                "away_corners": corners.get(
                    "away_corners",
                    0
                ),


                "total_corners": corners.get(
                    "total_corners",
                    0
                )


            },


            "confidence": score,


            "level": level,


            "entry": entry,


            "reasons": reasons

        }