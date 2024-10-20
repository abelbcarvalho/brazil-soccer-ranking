from decimal import Decimal

from src.models.models import BrazilianSoccerRanking, SoccerTeam


async def adapter_league_ranking(data: tuple) -> BrazilianSoccerRanking:
    if not (len(data[0]) == len(data[1])):
        raise Exception("teams names dada data ranking not linked whole as well")

    league = BrazilianSoccerRanking()
    league.brazilian_soccer_ranking = []

    for team, rank in zip(*data):
        points = rank[7]
        matches = rank[0]
        accuracy = Decimal(f"{(points / (matches * 3)) * 100}")

        league.brazilian_soccer_ranking.append(
            SoccerTeam(
                position=team[0],
                name=team[1],
                matches=matches,
                wins=rank[1],
                draws=rank[2],
                losses=rank[3],
                goals_for=rank[4],
                goals_against=rank[5],
                goals_difference=rank[6],
                points=points,
                accuracy=accuracy
            )
        )

    return league
