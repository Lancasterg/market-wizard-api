from fastapi import APIRouter
from t212.async_client import AsyncTrading212Client
from t212.models import PositionResponse

router = APIRouter(
    prefix="/portfolio",  # all routes in this router will start with /positions
    tags=["portfolio"],  # helps organize docs (Swagger UI)
)

portfolio_router = APIRouter(prefix="/v1/portfolio")


@portfolio_router.get("/portfolio")
async def portfolio() -> PositionResponse:
    response = await AsyncTrading212Client.fetch_all_open_positions()
    # Adjust prices that in pence not pounds
    for item in response.root:
        if item.currentPrice > 1500:
            item.currentPrice /= 100
    return response