from fastapi import HTTPException, Response
from starlette import status

from src.service.service_brazilian_soccer_ranking import ServiceBrazilianSoccerRanking


class ControllerBrazilianSoccerRanking:
    def __init__(self):
        self.service = ServiceBrazilianSoccerRanking()

    async def brazilian_soccer_championship_ranking(self, year: int):
        try:
            data = await self.service.brazilian_soccer_championship_ranking(year)

            return Response(
                content=data.json(),
                status_code=status.HTTP_200_OK
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e.args[0]))
