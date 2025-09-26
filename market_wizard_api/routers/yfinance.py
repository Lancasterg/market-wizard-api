import asyncio

from fastapi import APIRouter
from market_wizard_api.models.yfinance_models.models import (
    IntervalEnum,
    OHLCVData,
    OHLCVFields,
    PeriodEnum,
)

from market_wizard_api.clients.yf_client import yf_fetch_history

y_finance_router = APIRouter(
    prefix="/v1/finance",
    tags=["finance"],
)


@y_finance_router.get("/stock_history/{ticker}/{period}")
async def stock_data(
    ticker: str, period: PeriodEnum, interval: IntervalEnum
) -> OHLCVData:

    data: OHLCVData = await asyncio.to_thread(
        yf_fetch_history, ticker, period, interval
    )

    return data


@y_finance_router.get("a")
async def a():
    pass
