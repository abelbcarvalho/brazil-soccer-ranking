from src.core.web_scrapping.web_scrapping import WebScrapping
from src.utilities.adapter_league_ranking import adapter_league_ranking


class BrazilianSoccerRankingUseCase:
    def __init__(self):
        self.web_scrap = WebScrapping()

    async def execute(self, year: int) -> any:
        data_league = await self.web_scrap.brazilian_soccer_championship_ranking(year)

        return await adapter_league_ranking(data_league)
