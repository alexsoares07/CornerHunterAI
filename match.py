from dataclasses import dataclass


@dataclass
class Match:

    home: str
    away: str

    minute: int

    home_score: int
    away_score: int

    corners: int

    dangerous_attacks: int

    shots: int

    home_pressure: str = "normal"