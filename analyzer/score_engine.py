from config import MIN_SCORE


class ScoreEngine:

    def calculate(self, match):

        score = 0
        reasons = []

        minute = match.get("minute", 0)

        corners = match.get(
            "corners", {}
        ).get("total_corners", 0)

        home_score = match.get("home_score", 0)
        away_score = match.get("away_score", 0)

        corner_rate = match.get("corner_rate", 0)

        pressure = match.get("pressure_score", 0)

        # =========================
        # TEMPO
        # =========================

        if minute >= 75:

            score += 30
            reasons.append("Final de jogo")

        elif minute >= 60:

            score += 20
            reasons.append("Segundo tempo")

        elif minute >= 45:

            score += 10
            reasons.append("Início do segundo tempo")

        # =========================
        # ESCANTEIOS
        # =========================

        if corners >= 10:

            score += 35
            reasons.append("Muitos escanteios")

        elif corners >= 8:

            score += 30
            reasons.append("Muitos escanteios")

        elif corners >= 6:

            score += 20
            reasons.append("Boa quantidade de escanteios")

        elif corners >= 4:

            score += 10
            reasons.append("Escanteios começando a subir")

        # =========================
        # RITMO
        # =========================

        if corner_rate >= 0.18:

            score += 20
            reasons.append("Ritmo muito alto")

        elif corner_rate >= 0.12:

            score += 15
            reasons.append("Ritmo alto")

        elif corner_rate >= 0.08:

            score += 10
            reasons.append("Ritmo aceitável")

        # =========================
        # PLACAR
        # =========================

        diff = abs(home_score - away_score)

        if diff == 0:

            score += 5
            reasons.append("Jogo empatado")

        elif diff == 1:

            score += 15
            reasons.append("Jogo aberto")

        # =========================
        # PRESSÃO
        # =========================

        if pressure >= 70:

            score += 25
            reasons.append("Pressão muito alta")

        elif pressure >= 50:

            score += 15
            reasons.append("Pressão ofensiva alta")

        elif pressure >= 30:

            score += 8
            reasons.append("Pressão moderada")

        # =========================
        # BÔNUS
        # =========================

        if minute >= 70 and corners >= 8:

            score += 10
            reasons.append("Cenário ideal para Over")

        if minute >= 75 and diff <= 1:

            score += 10
            reasons.append("Final equilibrado")

        if score > 100:

            score = 100

        # =========================
        # CLASSIFICAÇÃO
        # =========================

        if score >= 70:

            level = "🟢 OPORTUNIDADE"

        elif score >= 45:

            level = "🟡 MONITORAR"

        else:

            level = "❌ SEM INTERESSE"

        return {
            "score": score,
            "level": level,
            "reasons": reasons
        }