from providers.sofascore_provider import SofaScoreProvider
import time


class LiveAnalyzer:

    def __init__(self):
        self.provider = SofaScoreProvider()


    def get_match_minute(self, event):

        match_time = event.get("time", {})
        status = event.get("status", {})

        if not match_time:
            return None

        period = status.get("description")

        start = match_time.get("currentPeriodStartTimestamp")

        if not start:
            return None


        seconds = int(time.time()) - start


        if period == "1st half":
            return seconds // 60


        elif period == "2nd half":
            return 45 + (seconds // 60)


        return None



    def analyze_match(self, event):

        event_id = event["id"]

        home = event["homeTeam"]["name"]
        away = event["awayTeam"]["name"]


        home_score = event["homeScore"].get("current", 0)
        away_score = event["awayScore"].get("current", 0)


        minute = self.get_match_minute(event)


        try:
            corners = self.provider.get_corners(event_id)

        except Exception:
            return None


        home_corners = corners.get("home_corners", 0)
        away_corners = corners.get("away_corners", 0)

        total_corners = home_corners + away_corners


        # ritmo de cantos
        corner_rate = 0

        if minute and minute > 0:
            corner_rate = round(total_corners / minute, 3)



        analysis = {

            "event_id": event_id,

            "match": f"{home} x {away}",

            "score": f"{home_score} - {away_score}",

            "minute": minute,

            "corners": {

                "home_corners": home_corners,

                "away_corners": away_corners,

                "total_corners": total_corners

            },

            "corner_rate": corner_rate

        }


        return analysis