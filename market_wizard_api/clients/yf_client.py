from market_wizard_api.models.yfinance_models import models
from newspaper import Article
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


def yf_get_news(ticker: str) -> models.NewsResponse:
    data = yf.Ticker(ticker).get_news()
    response = models.NewsResponse.model_validate(data)
    for i, item in enumerate(response.root):
        response.root[i].full_text = yf_get_full_news_stories(item.content.clickThroughUrl.url)
    return response 


def yf_get_full_news_stories(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text



def yf_eps_trend(ticker: str) -> models.EPSTrend:
    data = yf.Ticker(ticker).get_eps_trend()
    return models.EPSTrend.from_df(data)


def yf_analyst_price_targets(ticker: str) -> models.AnalysPriceTargets:
    data = yf.Ticker(ticker).get_analyst_price_targets()
    return models.AnalysPriceTargets.model_validate(data)


# def yf_something():
#     yf.Ticker("NVDA").
