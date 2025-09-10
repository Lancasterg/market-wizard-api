from pydantic import BaseModel, Field, ConfigDict


class PortfolioSummary(BaseModel):
    total_return: float = Field(
        ..., alias="totalReturn", description="Total return of the portfolio"
    )
    total_invested: float = Field(
        ..., alias="totalInvested", description="Total amount invested in the portfolio"
    )
    current_invested_value: float = Field(
        ..., alias="currentInvestedValue", description="Current market value of the portfolio"
    )
    profit_loss_percentage: float = Field(
        ...,
        alias="profitLossPercentage",
        description="Overall profit or loss percentage of the portfolio",
    )
    number_of_investments: int = Field(
        ...,
        alias="numberOfInvestments",
        description="Number of different investments in the portfolio",
    )
    free_cash: float = Field(
        ..., alias="freeCash", description="Free cash balance in the account"
    )
    invested_cash: float = Field(
        ..., alias="investedCash", description="Invested cash balance in the account"
    )
    total_portfolio_value: float = Field(
        ..., alias="totalPortfolioValue", description="Total value of the portfolio"
    )
    model_config = ConfigDict(populate_by_name=True)
