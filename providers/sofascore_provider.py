from sofascore_api import SofaScoreClient
import time


class SofaScoreProvider:


    def __init__(self):

        self.client = SofaScoreClient()



    def get_event(self, event_id):

        try:

            event = self.client.get_event(
                event_id
            )

            return event


        except Exception as e:

            print(
                f"Erro buscando evento {event_id}: {e}"
            )

            return {}



    def get_minute(self, event_id):

        try:

            event = self.get_event(
                event_id
            )


            if not event:

                return 0



            status = event.get(
                "status",
                {}
            )


            # minuto oficial do SofaScore

            minute = status.get(
                "clock",
                {}
            ).get(
                "played",
                0
            )



            if minute:

                return int(minute)



            # fallback pelo tempo corrido

            start = event.get(
                "startTimestamp"
            )


            if start:

                elapsed = int(time.time()) - int(start)

                minute = elapsed // 60


                if minute > 0:

                    return minute



            return 0



        except Exception as e:

            print(
                f"Erro buscando minuto {event_id}: {e}"
            )

            return 0





    def get_statistics_map(self, event_id):

        try:


            stats = self.client.get_event_statistics(
                event_id
            )


            if not stats:

                return {}



            resultado = {}



            for period in stats:


                if period.get("period") != "ALL":

                    continue



                for group in period.get("groups", []):


                    for item in group.get("statisticsItems", []):


                        key = item.get("key")


                        if key:


                            resultado[key] = {


                                "home": item.get(
                                    "homeValue",
                                    0
                                ),


                                "away": item.get(
                                    "awayValue",
                                    0
                                )


                            }



            return resultado



        except Exception as e:


            print(
                f"Erro buscando estatísticas {event_id}: {e}"
            )


            return {}





    def get_corners(self, event_id):


        stats = self.get_statistics_map(
            event_id
        )


        corners = stats.get(
            "cornerKicks"
        )



        if corners:


            home = corners.get(
                "home",
                0
            )


            away = corners.get(
                "away",
                0
            )



            return {


                "home_corners": int(home),


                "away_corners": int(away),


                "total_corners": int(home)+int(away)


            }



        return {


            "home_corners": 0,


            "away_corners": 0,


            "total_corners": 0


        }