class EntryEngine:


    def generate_entry(self, analysis, confidence):

        minute = analysis.get(
            "minute",
            0
        )


        corners = analysis.get(
            "corners",
            {}
        )


        total_corners = corners.get(
            "total_corners",
            0
        )



        # ==========================
        # REGRA DE ODD
        # ==========================

        if confidence >= 100:

            odd_minima = "1.40"

        else:

            odd_minima = "1.50"



        # ==========================
        # ESCOLHA DA LINHA
        # ==========================


        # Final de jogo
        if minute >= 80:


            if total_corners <= 7:

                mercado = "Over 8.5 Escanteios"


            elif total_corners <= 9:

                mercado = "Over 9.5 Escanteios"


            else:

                mercado = "Over 10.5 Escanteios"



        # Meio/final do segundo tempo

        elif minute >= 65:


            if total_corners <= 6:

                mercado = "Over 8.5 Escanteios"


            elif total_corners <= 8:

                mercado = "Over 9.5 Escanteios"


            else:

                mercado = "Over 10.5 Escanteios"



        # Antes dos 65

        else:


            if total_corners <= 7:

                mercado = "Over 9.5 Escanteios"


            else:

                mercado = "Over 10.5 Escanteios"



        return {


            "market": mercado,


            "odd_minimum": odd_minima,


            "confidence": confidence


        }