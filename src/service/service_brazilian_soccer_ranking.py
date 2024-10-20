from datetime import datetime

from src.exceptions.exceptions import YearException
from src.use_cases.brazilian_soccer_ranking_use_case import BrazilianSoccerRankingUseCase


class ServiceBrazilianSoccerRanking:
    def __init__(self):
        self.use_case = BrazilianSoccerRankingUseCase()

    async def brazilian_soccer_championship_ranking(self, year: int):
        current_year = datetime.now().year

        if not 2006 <= year <= current_year:
            raise YearException("year must be between 2006 and current year")

        return await self.use_case.execute(year)
