from typing import List


class ScrapData:
    @classmethod
    async def get_teams_positions_and_names(cls, teams: List[str]) -> List[List[int | str]]:
        gen_data = (x.split("\n") for x in teams)

        teams_names = [
            [int(x[0]), x[1]]
            for x in gen_data
        ]

        return teams_names

    @classmethod
    async def get_teams_data_ranking(cls, teams: List[str]) -> List[List[int]]:
        gen_data = (x.split("\n\t\n") for x in teams)

        teams_raking = [
            [int(i) for i in x]
            for x in gen_data
        ]

        return teams_raking
