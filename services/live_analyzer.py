import time

from providers.sofascore_provider import SofaScoreProvider



class LiveAnalyzer:


    def __init__(self):

        self.provider = SofaScoreProvider()



    def get_match_minute(self, event):

        try:

            # ============================
            # MINUTO REAL SOFASCORE CLOCK
            # ============================

            status = event.get(
                "status",
                {}
            )


            clock = status.get(
                "clock",
                {}
            )


            if clock:

                played = clock.get(
                    "played",
                    0
                )


                if played:

                    minute = int(played // 60)

                    if minute > 95:
                        minute = 90


                    return minute



            # ============================
            # FALLBACK TIMESTAMP
            # ============================


            match_time = event.get(
                "time",
                {}
            )


            period = status.get(
                "description",
                ""
            )


            start = match_time.get(
                "currentPeriodStartTimestamp"
            )


            if not start:

                return 0



            seconds = int(time.time()) - int(start)



            if period == "1st half":

                minute = seconds // 60



            elif period == "2nd half":

                minute = 45 + (seconds // 60)



            else:

                minute = 0



            if minute < 0:

                minute = 0



            if minute > 95:

                minute = 90



            return minute



        except Exception as e:


            print(
                f"Erro pegando minuto: {e}"
            )

            return 0





    def analyze_match(self, event):


        try:


            event_id = event.get(
                "id"
            )



            home = (
                event.get("homeTeam") or {}
            ).get(
                "name",
                "Casa"
            )



            away = (
                event.get("awayTeam") or {}
            ).get(
                "name",
                "Visitante"
            )



            home_score = (
                event.get("homeScore") or {}
            ).get(
                "current",
                0
            )



            away_score = (
                event.get("awayScore") or {}
            ).get(
                "current",
                0
            )



            minute = self.get_match_minute(
                event
            )



            corners = self.provider.get_corners(
                event_id
            )



            total_corners = corners.get(
                "total_corners",
                0
            )



            if minute > 0:

                corner_rate = round(
                    total_corners / minute,
                    3
                )


            else:

                corner_rate = 0



            return {


                "event_id": event_id,


                "match": f"{home} x {away}",


                "home_score": home_score,


                "away_score": away_score,


                "score": f"{home_score} - {away_score}",


                "minute": minute,


                "corners": corners,


                "corner_rate": corner_rate


            }



        except Exception as e:


            print(
                f"Erro no LiveAnalyzer: {e}"
            )


            return None