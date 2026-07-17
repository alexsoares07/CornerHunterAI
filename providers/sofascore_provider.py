from sofascore_api import SofaScoreClient


class SofaScoreProvider:

    def __init__(self):
        self.client = SofaScoreClient()


    def get_corners(self, event_id):

        stats = self.client.get_event_statistics(event_id)

        for period in stats:

            if period["period"] == "ALL":

                for group in period["groups"]:

                    for item in group["statisticsItems"]:

                        if item["key"] == "cornerKicks":

                            return {
                                "home_corners": item["homeValue"],
                                "away_corners": item["awayValue"],
                                "total_corners": (
                                    item["homeValue"] +
                                    item["awayValue"]
                                )
                            }

        return None