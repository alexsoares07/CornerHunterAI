class SignalGenerator:


    def generate(self, analysis):

        engine = analysis.get("score_engine", {})

        score = engine.get("score", 0)
        level = engine.get("level", "")


        if score < 70:
            return None


        return {

            "alert": level,

            "match": analysis.get("match"),

            "minute": analysis.get("minute"),

            "score": analysis.get("score"),

            "corners": analysis.get("corners"),

            "confidence": score,

            "reasons": engine.get("reasons")

        }