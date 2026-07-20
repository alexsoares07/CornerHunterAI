import sqlite3
from datetime import datetime



class SignalDatabase:


    def __init__(self):

        self.conn = sqlite3.connect(
            "database/signals.db"
        )

        self.create_table()



    def create_table(self):

        cursor = self.conn.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            match TEXT,

            minute INTEGER,

            score TEXT,

            corners INTEGER,

            confidence INTEGER,

            level TEXT,

            reasons TEXT,

            created_at TEXT

        )
        """)


        self.conn.commit()



    def save_signal(self, signal):


        cursor = self.conn.cursor()


        corners = signal.get(
            "corners",
            {}
        ).get(
            "total_corners",
            0
        )


        cursor.execute(
        """
        INSERT INTO signals
        (
            match,
            minute,
            score,
            corners,
            confidence,
            level,
            reasons,
            created_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            signal.get(
                "match"
            ),

            signal.get(
                "minute"
            ),

            signal.get(
                "result"
            ),

            corners,

            signal.get(
                "confidence"
            ),

            signal.get(
                "level"
            ),

            str(
                signal.get(
                    "reasons"
                )
            ),

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )


        )


        self.conn.commit()