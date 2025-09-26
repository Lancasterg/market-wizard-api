from market_wizard_api.models.yfinance_models import models

import yfinance as yf
import numpy as np


def yf_fetch_history(
    ticker: str, period: models.PeriodEnum, interval: models.IntervalEnum
) -> models.OHLCVData:
    """
    Fetch stock history data from yfinance and validate it using OHLCVData model.
    """
    data = yf.Ticker(ticker).history(period=period, interval=interval).reset_index()
    data[models.OHLCVFields.DATE] = np.array(data[models.OHLCVFields.DATE])
    return models.OHLCVData.model_validate(data.to_dict(orient="records"))


def yf_fetch_balance_sheet(ticker: str) -> models.BalanceSheet:
    data = yf.Ticker(ticker).get_balance_sheet()
    return models.BalanceSheet.from_df(data)


def yf_fetch_financials(ticker: str) -> models.FinancialStatement:
    data = yf.Ticker(ticker).get_financials()
    return models.FinancialStatement.from_df(data)


def yf_fetch_stock_info(ticker: str) -> models.StockInfo:
    data = yf.Ticker(ticker).get_info()
    return models.StockInfo.model_validate(data)


def yf_get_available_tickers():
    return """
        - RGTI
        - QBTS
        - IONQ
        - WULF
        - KLAR
        - PLTR
        - HIVE
        """


def yf_get_news(ticker: str):
    return yf.Ticker(ticker).get_news()


def yf_eps_trend(ticker: str) -> models.EPSTrend:
    data = yf.Ticker(ticker).get_eps_trend()
    return models.EPSTrend.from_df(data)


def yf_analyst_price_targets(ticker: str) -> models.AnalysPriceTargets:
    data = yf.Ticker(ticker).get_analyst_price_targets()
    return models.AnalysPriceTargets.model_validate(data)
