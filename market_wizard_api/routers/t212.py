from fastapi import APIRouter
from t212 import AsyncTrading212Client
from t212.models import PositionResponse, CashResponse
from market_wizard_api.models.portfolio.investments_summary import (
    InvestmentsSummaryResponse,
)
from market_wizard_api.models.portfolio.portfolio_summary import PortfolioSummary
from market_wizard_api.upstream.upstream_t212 import (
    get_investments_summary,
    get_portfolio_summary,
)

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


@portfolio_router.get("/investments_summary")
async def investments_summary() -> InvestmentsSummaryResponse:
    return await get_investments_summary()


@portfolio_router.get("/portfolio_summary")
async def portfolio_summary() -> PortfolioSummary:
    return await get_portfolio_summary()
