from fastmcp import FastMCP
import asyncio

from market_wizard_api.clients import yf_client
from market_wizard_api.models.yfinance_models.models import IntervalEnum, PeriodEnum


mcp = FastMCP("Finance MCP")

mcp_app = mcp.http_app(path="/", transport="streamable-http", stateless_http=True)


@mcp.tool(name="stock_data", description="Get historical stock data")
async def stock_data(ticker: str, period: PeriodEnum, interval: IntervalEnum) -> str:
    data = await asyncio.to_thread(yf_client.yf_fetch_history, ticker, period, interval)
    return data.llm_readble


@mcp.tool(
    name="balance_sheet", description="Get historical balance sheets for the company"
)
async def balance_sheet(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_fetch_balance_sheet, ticker)
    return data.llm_readable


@mcp.tool(name="financials", description="Get financials for a company")
async def financials(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_fetch_financials, ticker)
    return data.llm_readable


@mcp.tool(name="stock_info", description="Get informtion about a company")
async def stock_info(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_fetch_stock_info, ticker)
    return data.llm_readable


@mcp.tool(name="available_tickers", description="Get a list of availble tickers")
async def available_tickers() -> str:
    # data = await asyncio.to_thread(yf_fetch_stock_info, ticker)
    # return data.llm_readable

    return """
        - RGTI
        - QBTS
        - IONQ
        - WULF
        - KLAR
        - PLTR
        - HIVE
        - BITF
        """


@mcp.tool(name="news", description="Get news about a company")
async def news(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_get_news, ticker)
    return data.llm_readable


@mcp.tool(
    name="eps_trend", description="Get the earnings per share trend for a company"
)
async def earnings(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_eps_trend, ticker)
    return data.llm_readable


@mcp.tool(name="price_targets", description="Get analyst price targets")
async def price_targets(ticker: str) -> str:
    data = await asyncio.to_thread(yf_client.yf_analyst_price_targets, ticker)
    return data.llm_readable
