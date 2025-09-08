import yfinance as yf
import asyncio

from fastapi import APIRouter
from market_wizard_api.models.yfinance_models.models import OHLCVData, OHLCVFields
import numpy as np

y_finance_router = APIRouter(
    prefix="/v1/finance",
    tags=["finance"],
)


@y_finance_router.get("/stock_history/{ticker}/{period}")
async def stock_data(ticker: str, period: str) -> OHLCVData:

    def fetch_history() -> OHLCVData:
        """
        Fetch stock history data from yfinance and validate it using OHLCVData model.
        """
        data = yf.Ticker(ticker).history(period=period).reset_index()
        data[OHLCVFields.DATE] = np.array(data[OHLCVFields.DATE].dt.to_pydatetime())
        return OHLCVData.model_validate(data.to_dict(orient="records"))

    data = await asyncio.to_thread(fetch_history)

    return data
