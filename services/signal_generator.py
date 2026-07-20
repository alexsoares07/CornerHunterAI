class SignalGenerator:


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


        minute = analysis.get(
            "minute",
            0
        )


        corners = (
            analysis.get(
                "corners",
                {}
            )
            .get(
                "total_corners",
                0
            )
        )



        # =========================
        # FILTROS DE SEGURANÇA
        # =========================


        if level != "🟢 OPORTUNIDADE":

            return None



        if score < 70:

            return None



        if minute < 60:

            return None



        if corners < 6:

            return None



        # =========================
        # SINAL APROVADO
        # =========================


        return {


            "alert": "🚨 OPORTUNIDADE DE CANTOS",



            "match": analysis.get(
                "match",
                ""
            ),



            "minute": minute,



            "result": analysis.get(
                "score",
                ""
            ),



            "corners": analysis.get(
                "corners",
                {}
            ),



            "confidence": score,



            "level": level,



            "reasons": reasons

        }