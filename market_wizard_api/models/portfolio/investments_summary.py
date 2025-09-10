from pydantic import BaseModel, Field, ConfigDict, RootModel


class Investment(BaseModel):
    ticker: str = Field(..., description="The stock symbol")
    quantity: float = Field(..., description="Quantity of the stock owned")
    average_price: float = Field(..., description="Average purchase price of the stock")
    current_price: float = Field(..., description="Current market price of the stock")
    total_invested: float = Field(..., description="Total amount invested in the stock")
    current_value: float = Field(..., description="Current market value of the stock")
    profit_loss: float = Field(..., description="Profit or loss from the investment")
    profit_loss_percentage: float = Field(
        ..., description="Profit or loss percentage of the portfolio"
    )

    model_config = ConfigDict(populate_by_name=True)


class InvestmentsSummaryResponse(RootModel[list[Investment]]):
    pass
