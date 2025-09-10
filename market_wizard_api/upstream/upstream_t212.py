from aiocache import cached, SimpleMemoryCache

from fastapi import APIRouter, HTTPException

import asyncio
from t212.async_client import AsyncTrading212Client
from t212.models import PositionResponse, CashResponse
from aiocache import cached, SimpleMemoryCache
from market_wizard_api.models.portfolio.investments_summary import (
    Investment,
    InvestmentsSummaryResponse,
)
from market_wizard_api.models.portfolio.portfolio_summary import PortfolioSummary


@cached(ttl=60, cache=SimpleMemoryCache)
async def get_investments_summary() -> InvestmentsSummaryResponse:

    try:
        response = await AsyncTrading212Client.fetch_all_open_positions()
    except Exception as e:
        raise HTTPException(
            status_code=502, detail="Error fetching data from Trading212 API"
        ) from e

    items = []
    for item in response.root:
        total_invested = item.averagePrice * item.quantity
        current_value = item.currentPrice * item.quantity
        profit_loss_percentage = current_value / total_invested
        model = Investment(
            ticker=item.ticker,
            quantity=item.quantity,
            average_price=item.averagePrice,
            current_price=item.currentPrice,
            total_invested=total_invested,
            current_value=current_value,
            profit_loss=item.ppl,
            profit_loss_percentage=profit_loss_percentage - 1,
        )
        items.append(model)
    
    return InvestmentsSummaryResponse(root=items)


@cached(ttl=300, cache=SimpleMemoryCache)
async def get_portfolio_summary() -> PortfolioSummary:
    open_postitions_response: PositionResponse | Exception
    account_cash_response: CashResponse | Exception

    (open_postitions_response, account_cash_response) = await asyncio.gather(
        AsyncTrading212Client.fetch_all_open_positions(),
        AsyncTrading212Client.fetch_account_cash(),
        return_exceptions=True,
    )
    if isinstance(open_postitions_response, Exception) or isinstance(
        account_cash_response, Exception
    ):
        raise HTTPException(
            status_code=502, detail="Error fetching data from Trading212 API"
        )
    else:
        total_return = 0
        total_invested = 0
        current_value = 0
        profit_loss_percentage = 0
        number_of_investments = 0
        for item in open_postitions_response.root:
            total_invested += item.averagePrice * item.quantity
            current_value += item.currentPrice * item.quantity
            total_return += item.ppl
            number_of_investments += 1
            profit_loss_percentage = current_value / total_invested - 1

    return PortfolioSummary(
        total_return=total_return,
        total_invested=total_invested / 10,
        current_invested_value=current_value / 10,
        profit_loss_percentage=profit_loss_percentage,
        number_of_investments=number_of_investments,
        free_cash=account_cash_response.free,
        invested_cash=account_cash_response.invested,
        total_portfolio_value=account_cash_response.total,
    )


async def order_history_summary():
    return await AsyncTrading212Client.historical_order_data(0, None, 20)



if __name__ == "__main__":
    import asyncio

    async def main():
        resp = await order_history_summary()
        print(resp)

    asyncio.run(main())