from decimal import Decimal

from typing import List

from pydantic import BaseModel


class SoccerTeam(BaseModel):
    position: int
    name: str
    points: int
    matches: int
    wins: int
    draws: int
    losses: int
    goals_for: int
    goals_against: int
    accuracy: Decimal


class BrazilianSoccerRanking(BaseModel):
    brazilian_soccer_ranking: List[SoccerTeam] = None
