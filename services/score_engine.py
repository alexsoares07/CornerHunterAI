from config import MIN_SCORE


class ScoreEngine:


    def calculate(self, match):

        score = 0
        reasons = []


        minute = match.get(
            "minute",
            0
        )


        corners = (
            match.get("corners", {})
            .get("total_corners", 0)
        )


        home_score = match.get(
            "home_score",
            0
        )


        away_score = match.get(
            "away_score",
            0
        )


        corner_rate = match.get(
            "corner_rate",
            0
        )


        pressure = match.get(
            "pressure_score",
            0
        )



        # =========================
        # TEMPO DE JOGO
        # =========================


        if minute >= 80:

            score += 30

            reasons.append(
                "Final de jogo favorável"
            )


        elif minute >= 70:

            score += 25

            reasons.append(
                "Segundo tempo avançado"
            )


        elif minute >= 60:

            score += 15

            reasons.append(
                "Tempo favorável"
            )



        # =========================
        # ESCANTEIOS
        # =========================


        if corners >= 10:

            score += 35

            reasons.append(
                "Volume muito alto de escanteios"
            )


        elif corners >= 8:

            score += 30

            reasons.append(
                "Muitos escanteios"
            )


        elif corners >= 6:

            score += 20

            reasons.append(
                "Boa quantidade de escanteios"
            )



        elif corners >= 4:

            score += 10

            reasons.append(
                "Escanteios começando a subir"
            )



        # =========================
        # RITMO
        # =========================


        if corner_rate >= 0.12:

            score += 25

            reasons.append(
                "Ritmo muito alto"
            )


        elif corner_rate >= 0.08:

            score += 15

            reasons.append(
                "Ritmo aceitável"
            )



        # =========================
        # SITUAÇÃO DO JOGO
        # =========================


        if home_score < away_score:

            score += 20

            reasons.append(
                "Time da casa perdendo"
            )


        elif home_score > away_score:

            score += 15

            reasons.append(
                "Time visitante perdendo"
            )


        else:

            score += 5

            reasons.append(
                "Jogo empatado"
            )



        # =========================
        # PRESSÃO
        # =========================


        if pressure >= 50:

            score += 20

            reasons.append(
                "Pressão ofensiva alta"
            )


        elif pressure >= 30:

            score += 10

            reasons.append(
                "Pressão moderada"
            )



        # Limite

        if score > 100:

            score = 100



        # =========================
        # CLASSIFICAÇÃO
        # =========================


        if score >= 70:

            level = "🟢 OPORTUNIDADE"


        elif score >= 50:

            level = "🟡 MONITORAR"


        else:

            level = "❌ SEM INTERESSE"



        return {

            "score": score,

            "level": level,

            "reasons": reasons

        }