from fastapi import APIRouter
from fastapi.openapi.models import Response

from src.controllers.controller_brazilian_soccer_ranking import ControllerBrazilianSoccerRanking


controller_brazilian_soccer_ranking = ControllerBrazilianSoccerRanking()


router = APIRouter(prefix="/api/v1")


@router.post("/ranking/{year}")
async def brazilian_soccer_championship_ranking(year: int):
    return await controller_brazilian_soccer_ranking.brazilian_soccer_championship_ranking(year)
