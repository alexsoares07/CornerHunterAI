class ScoreEngine:


    def calculate(self, analysis):

        score = 0
        reasons = []


        minute = analysis.get("minute", 0)

        corners = analysis.get("corners", {})

        total_corners = corners.get("total_corners", 0)

        rate = analysis.get("corner_rate", 0)



        # Jogo avançado
        if minute >= 60:
            score += 20
            reasons.append("Segundo tempo avançado")


        # Volume de cantos
        if total_corners >= 5:
            score += 25
            reasons.append("Boa quantidade de escanteios")


        elif total_corners >= 3:
            score += 15
            reasons.append("Escanteios moderados")



        # Ritmo
        if rate >= 0.10:
            score += 30
            reasons.append("Ritmo alto de escanteios")


        elif rate >= 0.06:
            score += 20
            reasons.append("Ritmo aceitável")



        # Limite
        if score > 100:
            score = 100



        if score >= 85:
            level = "🔥 PREMIUM"

        elif score >= 70:
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