from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, RootModel, Field, ConfigDict
from enum import StrEnum


class PeriodEnum(StrEnum):
    _1_MIN = "1m"
    _15_MIN = "15m"
    _1_HOUE = "1h"
    _1_DAY = "1d"
    _1_WEEK = "1wk"
    _1_MONTH = "1mo"
    _3_MONTH = "3mo"
    _6_MONTH = "6mo"
    _1_YEAR = "1y"
    _2_YEAR = "2y"
    _5_YEAR = "5y"
    _10_YEAR = "10y"
    _YTD = "ytd"


class IntervalEnum(StrEnum):
    _1_MIN = "1m"
    _2_MIN = "2m"
    _5_MIN = "5m"
    _15_MIN = "15m"
    _30_MIN = "30m"
    _60_MIN = "60m"
    _1_DAY = "1d"
    _5_DAY = "5d"
    _1_MONTH = "1mo"


class OHLCVFields(StrEnum):
    DATE = "Date"
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    DIVIDENDS = "Dividends"
    STOCK_SPLITS = "Stock Splits"


class OHLCVRow(BaseModel):
    date: datetime = Field(alias="Date")
    open: float = Field(alias="Open")
    high: float = Field(alias="High")
    low: float = Field(alias="Low")
    close: float = Field(alias="Close")
    volume: float = Field(alias="Volume")
    dividends: float = Field(alias="Dividends")
    stock_splits: float = Field(alias="Stock Splits")

    model_config = ConfigDict(populate_by_name=True)


class OHLCVData(RootModel[list[OHLCVRow]]):
    pass

    @property
    def llm_readble(self) -> str:
        response = ""
        for item in self.root:
            row = (
                f"Date: {item.date} \n"
                + f"Open: {item.open} \n"
                + f"high: {item.high}\n"
                + f"low: {item.low}\n"
                + f"close: {item.close}\n"
                + f"volume: {item.volume}\n"
                + f"dividends: {item.dividends}\n"
                + f"stock_splits: {item.stock_splits}\n"
            )

            response = response + row
        return response


import pandas as pd
from datetime import datetime
from pydantic import BaseModel, RootModel, Field, ConfigDict
from enum import StrEnum


class BalanceSheetRow(BaseModel):
    date: datetime
    treasury_shares_number: float | None = Field(
        alias="TreasurySharesNumber", default=None
    )
    ordinary_shares_number: float | None = Field(
        alias="OrdinarySharesNumber", default=None
    )
    share_issued: float | None = Field(alias="ShareIssued", default=None)
    net_debt: float | None = Field(alias="NetDebt", default=None)
    total_debt: float | None = Field(alias="TotalDebt", default=None)
    tangible_book_value: float | None = Field(alias="TangibleBookValue", default=None)
    invested_capital: float | None = Field(alias="InvestedCapital", default=None)
    working_capital: float | None = Field(alias="WorkingCapital", default=None)
    net_tangible_assets: float | None = Field(alias="NetTangibleAssets", default=None)
    capital_lease_obligations: float | None = Field(
        alias="CapitalLeaseObligations", default=None
    )
    common_stock_equity: float | None = Field(alias="CommonStockEquity", default=None)
    total_capitalization: float | None = Field(
        alias="TotalCapitalization", default=None
    )
    total_equity_gross_minority_interest: float | None = Field(
        alias="TotalEquityGrossMinorityInterest", default=None
    )
    stockholders_equity: float | None = Field(alias="StockholdersEquity", default=None)
    gains_losses_not_affecting_retained_earnings: float | None = Field(
        alias="GainsLossesNotAffectingRetainedEarnings", default=None
    )
    other_equity_adjustments: float | None = Field(
        alias="OtherEquityAdjustments", default=None
    )
    retained_earnings: float | None = Field(alias="RetainedEarnings", default=None)
    additional_paid_in_capital: float | None = Field(
        alias="AdditionalPaidInCapital", default=None
    )
    capital_stock: float | None = Field(alias="CapitalStock", default=None)
    common_stock: float | None = Field(alias="CommonStock", default=None)
    preferred_stock: float | None = Field(alias="PreferredStock", default=None)
    total_liabilities_net_minority_interest: float | None = Field(
        alias="TotalLiabilitiesNetMinorityInterest", default=None
    )
    total_non_current_liabilities_net_minority_interest: float | None = Field(
        alias="TotalNonCurrentLiabilitiesNetMinorityInterest", default=None
    )
    other_non_current_liabilities: float | None = Field(
        alias="OtherNonCurrentLiabilities", default=None
    )
    preferred_securities_outside_stock_equity: float | None = Field(
        alias="PreferredSecuritiesOutsideStockEquity", default=None
    )
    derivative_product_liabilities: float | None = Field(
        alias="DerivativeProductLiabilities", default=None
    )
    non_current_deferred_liabilities: float | None = Field(
        alias="NonCurrentDeferredLiabilities", default=None
    )
    non_current_deferred_revenue: float | None = Field(
        alias="NonCurrentDeferredRevenue", default=None
    )
    long_term_debt_and_capital_lease_obligation: float | None = Field(
        alias="LongTermDebtAndCapitalLeaseObligation", default=None
    )
    long_term_capital_lease_obligation: float | None = Field(
        alias="LongTermCapitalLeaseObligation", default=None
    )
    long_term_debt: float | None = Field(alias="LongTermDebt", default=None)
    current_liabilities: float | None = Field(alias="CurrentLiabilities", default=None)
    other_current_liabilities: float | None = Field(
        alias="OtherCurrentLiabilities", default=None
    )
    current_deferred_liabilities: float | None = Field(
        alias="CurrentDeferredLiabilities", default=None
    )
    current_deferred_revenue: float | None = Field(
        alias="CurrentDeferredRevenue", default=None
    )
    current_debt_and_capital_lease_obligation: float | None = Field(
        alias="CurrentDebtAndCapitalLeaseObligation", default=None
    )
    current_capital_lease_obligation: float | None = Field(
        alias="CurrentCapitalLeaseObligation", default=None
    )
    current_debt: float | None = Field(alias="CurrentDebt", default=None)
    other_current_borrowings: float | None = Field(
        alias="OtherCurrentBorrowings", default=None
    )
    payables_and_accrued_expenses: float | None = Field(
        alias="PayablesAndAccruedExpenses", default=None
    )
    current_accrued_expenses: float | None = Field(
        alias="CurrentAccruedExpenses", default=None
    )
    interest_payable: float | None = Field(alias="InterestPayable", default=None)
    payables: float | None = Field(alias="Payables", default=None)
    total_tax_payable: float | None = Field(alias="TotalTaxPayable", default=None)
    accounts_payable: float | None = Field(alias="AccountsPayable", default=None)
    total_assets: float | None = Field(alias="TotalAssets", default=None)
    total_non_current_assets: float | None = Field(
        alias="TotalNonCurrentAssets", default=None
    )
    other_non_current_assets: float | None = Field(
        alias="OtherNonCurrentAssets", default=None
    )
    investments_and_advances: float | None = Field(
        alias="InvestmentsAndAdvances", default=None
    )
    investment_in_financial_assets: float | None = Field(
        alias="InvestmentinFinancialAssets", default=None
    )
    available_for_sale_securities: float | None = Field(
        alias="AvailableForSaleSecurities", default=None
    )
    goodwill_and_other_intangible_assets: float | None = Field(
        alias="GoodwillAndOtherIntangibleAssets", default=None
    )
    goodwill: float | None = Field(alias="Goodwill", default=None)
    net_ppe: float | None = Field(alias="NetPPE", default=None)
    accumulated_depreciation: float | None = Field(
        alias="AccumulatedDepreciation", default=None
    )
    gross_ppe: float | None = Field(alias="GrossPPE", default=None)
    leases: float | None = Field(alias="Leases", default=None)
    construction_in_progress: float | None = Field(
        alias="ConstructionInProgress", default=None
    )
    other_properties: float | None = Field(alias="OtherProperties", default=None)
    machinery_furniture_equipment: float | None = Field(
        alias="MachineryFurnitureEquipment", default=None
    )
    properties: float | None = Field(alias="Properties", default=None)
    current_assets: float | None = Field(alias="CurrentAssets", default=None)
    other_current_assets: float | None = Field(alias="OtherCurrentAssets", default=None)
    hedging_assets_current: float | None = Field(
        alias="HedgingAssetsCurrent", default=None
    )
    current_deferred_assets: float | None = Field(
        alias="CurrentDeferredAssets", default=None
    )
    prepaid_assets: float | None = Field(alias="PrepaidAssets", default=None)
    receivables: float | None = Field(alias="Receivables", default=None)
    accounts_receivable: float | None = Field(alias="AccountsReceivable", default=None)
    cash_cash_equivalents_and_short_term_investments: float | None = Field(
        alias="CashCashEquivalentsAndShortTermInvestments", default=None
    )
    other_short_term_investments: float | None = Field(
        alias="OtherShortTermInvestments", default=None
    )
    cash_and_cash_equivalents: float | None = Field(
        alias="CashAndCashEquivalents", default=None
    )
    cash_financial: float | None = Field(alias="CashFinancial", default=None)

    model_config = ConfigDict(populate_by_name=True)


class BalanceSheet(RootModel[list[BalanceSheetRow]]):
    @classmethod
    def from_df(cls, df: pd.DataFrame) -> "BalanceSheet":
        data_rows = []
        for col in df.columns:
            date_str = str(col)
            # Attempt to parse date, handle potential errors
            try:
                parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S%z")
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    # Fallback for dates that might not be in standard format, or if timezone is missing
                    # This might need more robust handling depending on actual data
                    parsed_date = (
                        datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                        if "Z" in date_str
                        else datetime.fromisoformat(date_str)
                    )

            row_data = df[col].rename(index=lambda x: x.replace(" ", "")).to_dict()
            row_data["date"] = parsed_date  # Add the date to the row data
            data_rows.append(BalanceSheetRow.model_validate(row_data))
        return cls(root=data_rows)

    @property
    def llm_readable(self) -> str:
        response = ""
        for item in self.root:
            row_details = f"Date: {item.date}\n"
            for field_name, field_value in item.model_dump(by_alias=False).items():
                if field_name != "date" and field_value is not None:
                    row_details += (
                        f"{field_name.replace('_', ' ').title()}: {field_value}\n"
                    )
            response += row_details + "\n"
        return response


class FinancialStatementRow(BaseModel):
    date: datetime
    tax_effect_of_unusual_items: float | None = Field(
        alias="TaxEffectOfUnusualItems", default=None
    )
    tax_rate_for_calcs: float | None = Field(alias="TaxRateForCalcs", default=None)
    normalized_ebitda: float | None = Field(alias="NormalizedEBITDA", default=None)
    total_unusual_items: float | None = Field(alias="TotalUnusualItems", default=None)
    total_unusual_items_excluding_goodwill: float | None = Field(
        alias="TotalUnusualItemsExcludingGoodwill", default=None
    )
    net_income_from_continuing_operation_net_minority_inte: float | None = Field(
        alias="NetIncomeFromContinuingOperationNetMinorityInte", default=None
    )
    reconciled_depreciation: float | None = Field(
        alias="ReconciledDepreciation", default=None
    )
    reconciled_cost_of_revenue: float | None = Field(
        alias="ReconciledCostOfRevenue", default=None
    )
    ebitda: float | None = Field(alias="EBITDA", default=None)
    ebit: float | None = Field(alias="EBIT", default=None)
    net_interest_income: float | None = Field(alias="NetInterestIncome", default=None)
    interest_expense: float | None = Field(alias="InterestExpense", default=None)
    interest_income: float | None = Field(alias="InterestIncome", default=None)
    normalized_income: float | None = Field(alias="NormalizedIncome", default=None)
    net_income_from_continuing_and_discontinued_operation: float | None = Field(
        alias="NetIncomeFromContinuingAndDiscontinuedOperation", default=None
    )
    total_expenses: float | None = Field(alias="TotalExpenses", default=None)
    total_operating_income_as_reported: float | None = Field(
        alias="TotalOperatingIncomeAsReported", default=None
    )
    diluted_average_shares: float | None = Field(
        alias="DilutedAverageShares", default=None
    )
    basic_average_shares: float | None = Field(alias="BasicAverageShares", default=None)
    diluted_eps: float | None = Field(alias="DilutedEPS", default=None)
    basic_eps: float | None = Field(alias="BasicEPS", default=None)
    diluted_ni_avail_to_com_stockholders: float | None = Field(
        alias="DilutedNIAvailtoComStockholders", default=None
    )
    net_income_common_stockholders: float | None = Field(
        alias="NetIncomeCommonStockholders", default=None
    )
    net_income: float | None = Field(alias="NetIncome", default=None)
    net_income_including_noncontrolling_interests: float | None = Field(
        alias="NetIncomeIncludingNoncontrollingInterests", default=None
    )
    net_income_continuous_operations: float | None = Field(
        alias="NetIncomeContinuousOperations", default=None
    )
    tax_provision: float | None = Field(alias="TaxProvision", default=None)
    pretax_income: float | None = Field(alias="PretaxIncome", default=None)
    other_income_expense: float | None = Field(alias="OtherIncomeExpense", default=None)
    other_non_operating_income_expenses: float | None = Field(
        alias="OtherNonOperatingIncomeExpenses", default=None
    )
    special_income_charges: float | None = Field(
        alias="SpecialIncomeCharges", default=None
    )
    other_special_charges: float | None = Field(
        alias="OtherSpecialCharges", default=None
    )
    impairment_of_capital_assets: float | None = Field(
        alias="ImpairmentOfCapitalAssets", default=None
    )
    restructuring_and_mergern_acquisition: float | None = Field(
        alias="RestructuringAndMergernAcquisition", default=None
    )
    gain_on_sale_of_security: float | None = Field(
        alias="GainOnSaleOfSecurity", default=None
    )
    net_non_operating_interest_income_expense: float | None = Field(
        alias="NetNonOperatingInterestIncomeExpense", default=None
    )
    total_other_finance_cost: float | None = Field(
        alias="TotalOtherFinanceCost", default=None
    )
    interest_expense_non_operating: float | None = Field(
        alias="InterestExpenseNonOperating", default=None
    )
    interest_income_non_operating: float | None = Field(
        alias="InterestIncomeNonOperating", default=None
    )
    operating_income: float | None = Field(alias="OperatingIncome", default=None)
    operating_expense: float | None = Field(alias="OperatingExpense", default=None)
    research_and_development: float | None = Field(
        alias="ResearchAndDevelopment", default=None
    )
    selling_general_and_administration: float | None = Field(
        alias="SellingGeneralAndAdministration", default=None
    )
    selling_and_marketing_expense: float | None = Field(
        alias="SellingAndMarketingExpense", default=None
    )
    general_and_administrative_expense: float | None = Field(
        alias="GeneralAndAdministrativeExpense", default=None
    )
    other_g_and_a: float | None = Field(alias="OtherGandA", default=None)
    gross_profit: float | None = Field(alias="GrossProfit", default=None)
    cost_of_revenue: float | None = Field(alias="CostOfRevenue", default=None)
    total_revenue: float | None = Field(alias="TotalRevenue", default=None)
    operating_revenue: float | None = Field(alias="OperatingRevenue", default=None)

    model_config = ConfigDict(populate_by_name=True)


class FinancialStatement(RootModel[list[FinancialStatementRow]]):
    pass

    @classmethod
    def from_df(cls, df: pd.DataFrame) -> "FinancialStatement":
        data_rows = []
        for col in df.columns:
            date_str = str(col)
            try:
                parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S%z")
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    parsed_date = (
                        datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                        if "Z" in date_str
                        else datetime.fromisoformat(date_str)
                    )

            row_data = df[col].rename(index=lambda x: x.replace(" ", "")).to_dict()
            row_data["date"] = parsed_date
            data_rows.append(FinancialStatementRow.model_validate(row_data))
        return cls(root=data_rows)

    @property
    def llm_readable(self) -> str:
        response = ""
        for item in self.root:
            row_details = f"Date: {item.date.strftime('%Y-%m-%d')}\n"
            for field_name, field_value in item.model_dump(by_alias=False).items():
                if field_name != "date" and field_value is not None:
                    row_details += (
                        f"{field_name.replace('_', ' ').title()}: {field_value}\n"
                    )
            response += row_details + "\n"
        return response


class CompanyOfficer(BaseModel):
    max_age: Optional[int] = Field(alias="maxAge", default=None)
    name: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None)
    title: Optional[str] = Field(default=None)
    year_born: Optional[int] = Field(alias="yearBorn", default=None)
    fiscal_year: Optional[int] = Field(alias="fiscalYear", default=None)
    total_pay: Optional[int] = Field(alias="totalPay", default=None)
    exercised_value: Optional[int] = Field(alias="exercisedValue", default=None)
    unexercised_value: Optional[int] = Field(alias="unexercisedValue", default=None)

    model_config = ConfigDict(populate_by_name=True)


class StockInfo(BaseModel):
    address1: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    state: Optional[str] = Field(default=None)
    zip: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    website: Optional[str] = Field(default=None)
    industry: Optional[str] = Field(default=None)
    industry_key: Optional[str] = Field(alias="industryKey", default=None)
    industry_disp: Optional[str] = Field(alias="industryDisp", default=None)
    sector: Optional[str] = Field(default=None)
    sector_key: Optional[str] = Field(alias="sectorKey", default=None)
    sector_disp: Optional[str] = Field(alias="sectorDisp", default=None)
    long_business_summary: Optional[str] = Field(
        alias="longBusinessSummary", default=None
    )
    full_time_employees: Optional[int] = Field(alias="fullTimeEmployees", default=None)
    company_officers: Optional[list[CompanyOfficer]] = Field(
        alias="companyOfficers", default_factory=list
    )
    audit_risk: Optional[int] = Field(alias="auditRisk", default=None)
    board_risk: Optional[int] = Field(alias="boardRisk", default=None)
    compensation_risk: Optional[int] = Field(alias="compensationRisk", default=None)
    share_holder_rights_risk: Optional[int] = Field(
        alias="shareHolderRightsRisk", default=None
    )
    overall_risk: Optional[int] = Field(alias="overallRisk", default=None)
    governance_epoch_date: Optional[int] = Field(
        alias="governanceEpochDate", default=None
    )
    compensation_as_of_epoch_date: Optional[int] = Field(
        alias="compensationAsOfEpochDate", default=None
    )
    executive_team: Optional[list[Any]] = Field(
        alias="executiveTeam", default_factory=list
    )
    max_age: Optional[int] = Field(alias="maxAge", default=None)
    price_hint: Optional[int] = Field(alias="priceHint", default=None)
    previous_close: Optional[float] = Field(alias="previousClose", default=None)
    open: Optional[float] = Field(default=None)
    day_low: Optional[float] = Field(alias="dayLow", default=None)
    day_high: Optional[float] = Field(alias="dayHigh", default=None)
    regular_market_previous_close: Optional[float] = Field(
        alias="regularMarketPreviousClose", default=None
    )
    regular_market_open: Optional[float] = Field(
        alias="regularMarketOpen", default=None
    )
    regular_market_day_low: Optional[float] = Field(
        alias="regularMarketDayLow", default=None
    )
    regular_market_day_high: Optional[float] = Field(
        alias="regularMarketDayHigh", default=None
    )
    payout_ratio: Optional[float] = Field(alias="payoutRatio", default=None)
    beta: Optional[float] = Field(default=None)
    forward_pe: Optional[float] = Field(alias="forwardPE", default=None)
    volume: Optional[int] = Field(default=None)
    regular_market_volume: Optional[int] = Field(
        alias="regularMarketVolume", default=None
    )
    average_volume: Optional[int] = Field(alias="averageVolume", default=None)
    average_volume10_days: Optional[int] = Field(
        alias="averageVolume10days", default=None
    )
    average_daily_volume10_day: Optional[int] = Field(
        alias="averageDailyVolume10Day", default=None
    )
    bid: Optional[float] = Field(default=None)
    ask: Optional[float] = Field(default=None)
    bid_size: Optional[int] = Field(alias="bidSize", default=None)
    ask_size: Optional[int] = Field(alias="askSize", default=None)
    market_cap: Optional[int] = Field(alias="marketCap", default=None)
    fifty_two_week_low: Optional[float] = Field(alias="fiftyTwoWeekLow", default=None)
    fifty_two_week_high: Optional[float] = Field(alias="fiftyTwoWeekHigh", default=None)
    all_time_high: Optional[float] = Field(alias="allTimeHigh", default=None)
    all_time_low: Optional[float] = Field(alias="allTimeLow", default=None)
    price_to_sales_trailing12_months: Optional[float] = Field(
        alias="priceToSalesTrailing12Months", default=None
    )
    fifty_day_average: Optional[float] = Field(alias="fiftyDayAverage", default=None)
    two_hundred_day_average: Optional[float] = Field(
        alias="twoHundredDayAverage", default=None
    )
    trailing_annual_dividend_rate: Optional[float] = Field(
        alias="trailingAnnualDividendRate", default=None
    )
    trailing_annual_dividend_yield: Optional[float] = Field(
        alias="trailingAnnualDividendYield", default=None
    )
    currency: Optional[str] = Field(default=None)
    tradeable: Optional[bool] = Field(default=None)
    enterprise_value: Optional[int] = Field(alias="enterpriseValue", default=None)
    profit_margins: Optional[float] = Field(alias="profitMargins", default=None)
    float_shares: Optional[int] = Field(alias="floatShares", default=None)
    shares_outstanding: Optional[int] = Field(alias="sharesOutstanding", default=None)
    shares_short: Optional[int] = Field(alias="sharesShort", default=None)
    shares_short_prior_month: Optional[int] = Field(
        alias="sharesShortPriorMonth", default=None
    )
    shares_short_previous_month_date: Optional[int] = Field(
        alias="sharesShortPreviousMonthDate", default=None
    )
    date_short_interest: Optional[int] = Field(alias="dateShortInterest", default=None)
    shares_percent_shares_out: Optional[float] = Field(
        alias="sharesPercentSharesOut", default=None
    )
    held_percent_insiders: Optional[float] = Field(
        alias="heldPercentInsiders", default=None
    )
    held_percent_institutions: Optional[float] = Field(
        alias="heldPercentInstitutions", default=None
    )
    short_ratio: Optional[float] = Field(alias="shortRatio", default=None)
    short_percent_of_float: Optional[float] = Field(
        alias="shortPercentOfFloat", default=None
    )
    implied_shares_outstanding: Optional[int] = Field(
        alias="impliedSharesOutstanding", default=None
    )
    book_value: Optional[float] = Field(alias="bookValue", default=None)
    price_to_book: Optional[float] = Field(alias="priceToBook", default=None)
    last_fiscal_year_end: Optional[int] = Field(alias="lastFiscalYearEnd", default=None)
    next_fiscal_year_end: Optional[int] = Field(alias="nextFiscalYearEnd", default=None)
    most_recent_quarter: Optional[int] = Field(alias="mostRecentQuarter", default=None)
    net_income_to_common: Optional[int] = Field(alias="netIncomeToCommon", default=None)
    trailing_eps: Optional[float] = Field(alias="trailingEps", default=None)
    forward_eps: Optional[float] = Field(alias="forwardEps", default=None)
    enterprise_to_revenue: Optional[float] = Field(
        alias="enterpriseToRevenue", default=None
    )
    enterprise_to_ebitda: Optional[float] = Field(
        alias="enterpriseToEbitda", default=None
    )
    week_change_52: Optional[float] = Field(alias="52WeekChange", default=None)
    sand_p52_week_change: Optional[float] = Field(
        alias="SandP52WeekChange", default=None
    )
    quote_type: Optional[str] = Field(alias="quoteType", default=None)
    current_price: Optional[float] = Field(alias="currentPrice", default=None)
    target_high_price: Optional[float] = Field(alias="targetHighPrice", default=None)
    target_low_price: Optional[float] = Field(alias="targetLowPrice", default=None)
    target_mean_price: Optional[float] = Field(alias="targetMeanPrice", default=None)
    target_median_price: Optional[float] = Field(
        alias="targetMedianPrice", default=None
    )
    recommendation_mean: Optional[float] = Field(
        alias="recommendationMean", default=None
    )
    recommendation_key: Optional[str] = Field(alias="recommendationKey", default=None)
    number_of_analyst_opinions: Optional[int] = Field(
        alias="numberOfAnalystOpinions", default=None
    )
    total_cash: Optional[int] = Field(alias="totalCash", default=None)
    total_cash_per_share: Optional[float] = Field(
        alias="totalCashPerShare", default=None
    )
    ebitda: Optional[int] = Field(default=None)
    total_debt: Optional[int] = Field(alias="totalDebt", default=None)
    quick_ratio: Optional[float] = Field(alias="quickRatio", default=None)
    current_ratio: Optional[float] = Field(alias="currentRatio", default=None)
    total_revenue: Optional[int] = Field(alias="totalRevenue", default=None)
    debt_to_equity: Optional[float] = Field(alias="debtToEquity", default=None)
    revenue_per_share: Optional[float] = Field(alias="revenuePerShare", default=None)
    return_on_assets: Optional[float] = Field(alias="returnOnAssets", default=None)
    return_on_equity: Optional[float] = Field(alias="returnOnEquity", default=None)
    gross_profits: Optional[int] = Field(alias="grossProfits", default=None)
    free_cashflow: Optional[int] = Field(alias="freeCashflow", default=None)
    operating_cashflow: Optional[int] = Field(alias="operatingCashflow", default=None)
    revenue_growth: Optional[float] = Field(alias="revenueGrowth", default=None)
    gross_margins: Optional[float] = Field(alias="grossMargins", default=None)
    ebitda_margins: Optional[float] = Field(alias="ebitdaMargins", default=None)
    operating_margins: Optional[float] = Field(alias="operatingMargins", default=None)
    financial_currency: Optional[str] = Field(alias="financialCurrency", default=None)
    symbol: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    region: Optional[str] = Field(default=None)
    type_disp: Optional[str] = Field(alias="typeDisp", default=None)
    quote_source_name: Optional[str] = Field(alias="quoteSourceName", default=None)
    triggerable: Optional[bool] = Field(default=None)
    custom_price_alert_confidence: Optional[str] = Field(
        alias="customPriceAlertConfidence", default=None
    )
    regular_market_change_percent: Optional[float] = Field(
        alias="regularMarketChangePercent", default=None
    )
    regular_market_price: Optional[float] = Field(
        alias="regularMarketPrice", default=None
    )
    corporate_actions: Optional[list[Any]] = Field(
        alias="corporateActions", default_factory=list
    )  # Assuming Any for now as it's empty
    post_market_time: Optional[int] = Field(alias="postMarketTime", default=None)
    regular_market_time: Optional[int] = Field(alias="regularMarketTime", default=None)
    exchange: Optional[str] = Field(default=None)
    message_board_id: Optional[str] = Field(alias="messageBoardId", default=None)
    exchange_timezone_name: Optional[str] = Field(
        alias="exchangeTimezoneName", default=None
    )
    exchange_timezone_short_name: Optional[str] = Field(
        alias="exchangeTimezoneShortName", default=None
    )
    gmt_off_set_milliseconds: Optional[int] = Field(
        alias="gmtOffSetMilliseconds", default=None
    )
    market: Optional[str] = Field(default=None)
    esg_populated: Optional[bool] = Field(alias="esgPopulated", default=None)
    short_name: Optional[str] = Field(alias="shortName", default=None)
    long_name: Optional[str] = Field(alias="longName", default=None)
    full_exchange_name: Optional[str] = Field(alias="fullExchangeName", default=None)
    average_daily_volume3_month: Optional[int] = Field(
        alias="averageDailyVolume3Month", default=None
    )
    fifty_two_week_low_change: Optional[float] = Field(
        alias="fiftyTwoWeekLowChange", default=None
    )
    fifty_two_week_low_change_percent: Optional[float] = Field(
        alias="fiftyTwoWeekLowChangePercent", default=None
    )
    fifty_two_week_range: Optional[str] = Field(alias="fiftyTwoWeekRange", default=None)
    fifty_two_week_high_change: Optional[float] = Field(
        alias="fiftyTwoWeekHighChange", default=None
    )
    fifty_two_week_high_change_percent: Optional[float] = Field(
        alias="fiftyTwoWeekHighChangePercent", default=None
    )
    fifty_two_week_change_percent: Optional[float] = Field(
        alias="fiftyTwoWeekChangePercent", default=None
    )
    earnings_timestamp: Optional[int] = Field(alias="earningsTimestamp", default=None)
    earnings_timestamp_start: Optional[int] = Field(
        alias="earningsTimestampStart", default=None
    )
    earnings_timestamp_end: Optional[int] = Field(
        alias="earningsTimestampEnd", default=None
    )
    earnings_call_timestamp_start: Optional[int] = Field(
        alias="earningsCallTimestampStart", default=None
    )
    earnings_call_timestamp_end: Optional[int] = Field(
        alias="earningsCallTimestampEnd", default=None
    )
    is_earnings_date_estimate: Optional[bool] = Field(
        alias="isEarningsDateEstimate", default=None
    )
    eps_trailing_twelve_months: Optional[float] = Field(
        alias="epsTrailingTwelveMonths", default=None
    )
    eps_forward: Optional[float] = Field(alias="epsForward", default=None)
    eps_current_year: Optional[float] = Field(alias="epsCurrentYear", default=None)
    price_eps_current_year: Optional[float] = Field(
        alias="priceEpsCurrentYear", default=None
    )
    fifty_day_average_change: Optional[float] = Field(
        alias="fiftyDayAverageChange", default=None
    )
    fifty_day_average_change_percent: Optional[float] = Field(
        alias="fiftyDayAverageChangePercent", default=None
    )
    two_hundred_day_average_change: Optional[float] = Field(
        alias="twoHundredDayAverageChange", default=None
    )
    two_hundred_day_average_change_percent: Optional[float] = Field(
        alias="twoHundredDayAverageChangePercent", default=None
    )
    source_interval: Optional[int] = Field(alias="sourceInterval", default=None)
    exchange_data_delayed_by: Optional[int] = Field(
        alias="exchangeDataDelayedBy", default=None
    )
    ipo_expected_date: Optional[str] = Field(alias="ipoExpectedDate", default=None)
    average_analyst_rating: Optional[str] = Field(
        alias="averageAnalystRating", default=None
    )
    crypto_tradeable: Optional[bool] = Field(alias="cryptoTradeable", default=None)
    has_pre_post_market_data: Optional[bool] = Field(
        alias="hasPrePostMarketData", default=None
    )
    first_trade_date_milliseconds: Optional[int] = Field(
        alias="firstTradeDateMilliseconds", default=None
    )
    post_market_change_percent: Optional[float] = Field(
        alias="postMarketChangePercent", default=None
    )
    post_market_price: Optional[float] = Field(alias="postMarketPrice", default=None)
    post_market_change: Optional[float] = Field(alias="postMarketChange", default=None)
    regular_market_change: Optional[float] = Field(
        alias="regularMarketChange", default=None
    )
    regular_market_day_range: Optional[str] = Field(
        alias="regularMarketDayRange", default=None
    )
    market_state: Optional[str] = Field(alias="marketState", default=None)
    display_name: Optional[str] = Field(alias="displayName", default=None)
    trailing_peg_ratio: Optional[float] = Field(alias="trailingPegRatio", default=None)

    model_config = ConfigDict(populate_by_name=True)

    @property
    def llm_readable(self) -> str:
        readable_output = f"Company: {self.long_name or self.short_name or 'N/A'}\n"
        readable_output += f"Symbol: {self.symbol or 'N/A'}\n"
        readable_output += f"Industry: {self.industry_disp or self.industry or 'N/A'}\n"
        readable_output += f"Sector: {self.sector_disp or self.sector or 'N/A'}\n"
        readable_output += f"Address: {self.address1 or 'N/A'}, {self.city or 'N/A'}, {self.state or 'N/A'} {self.zip or 'N/A'}, {self.country or 'N/A'}\n"
        readable_output += f"Website: {self.website or 'N/A'}\n"
        readable_output += f"Phone: {self.phone or 'N/A'}\n"
        readable_output += f"Full Time Employees: {self.full_time_employees or 'N/A'}\n"
        readable_output += (
            f"Long Business Summary: {self.long_business_summary or 'N/A'}\n"
        )
        readable_output += (
            f"Current Price: {self.current_price or 'N/A'} {self.currency or ''}\n"
        )
        readable_output += (
            f"Previous Close: {self.previous_close or 'N/A'} {self.currency or ''}\n"
        )
        readable_output += (
            f"Day Range: {self.day_low or 'N/A'} - {self.day_high or 'N/A'}\n"
        )
        readable_output += f"52 Week Range: {self.fifty_two_week_low or 'N/A'} - {self.fifty_two_week_high or 'N/A'}\n"
        readable_output += f"Market Cap: {self.market_cap or 'N/A'}\n"
        readable_output += f"Volume: {self.volume or 'N/A'}\n"
        readable_output += (
            f"Average Volume (10 days): {self.average_volume10_days or 'N/A'}\n"
        )
        readable_output += f"Recommendation: {self.recommendation_key.replace('_', ' ').title() if self.recommendation_key else 'N/A'} (Mean: {self.recommendation_mean or 'N/A'} from {self.number_of_analyst_opinions or 'N/A'} analysts)\n"
        readable_output += f"Trailing EPS: {self.trailing_eps or 'N/A'}\n"
        readable_output += f"Forward EPS: {self.forward_eps or 'N/A'}\n"
        readable_output += f"Total Revenue: {self.total_revenue or 'N/A'}\n"
        readable_output += f"Gross Profits: {self.gross_profits or 'N/A'}\n"
        readable_output += f"EBITDA: {self.ebitda or 'N/A'}\n"
        readable_output += f"Total Cash: {self.total_cash or 'N/A'}\n"
        readable_output += f"Total Debt: {self.total_debt or 'N/A'}\n"
        readable_output += f"Return on Equity: {self.return_on_equity or 'N/A'}\n"
        readable_output += f"Profit Margins: {self.profit_margins or 'N/A'}\n"

        if self.company_officers:
            readable_output += "\nCompany Officers:\n"
            for officer in self.company_officers:
                readable_output += (
                    f"  - {officer.name or 'N/A'}, {officer.title or 'N/A'}"
                )
                if officer.age:
                    readable_output += f" (Age: {officer.age})"
                if officer.total_pay:
                    readable_output += f" (Total Pay: {officer.total_pay})"
                readable_output += "\n"

        return readable_output


class PeriodEstimate(BaseModel):
    period: str = Field(..., alias="period")
    current: float = Field(..., alias="current")
    days7Ago: float = Field(..., alias="7daysAgo")
    days30Ago: float = Field(..., alias="30daysAgo")
    days60Ago: float = Field(..., alias="60daysAgo")
    days90Ago: float = Field(..., alias="90daysAgo")
    model_config = ConfigDict(populate_by_name=True)


class EPSTrend(RootModel[list[PeriodEstimate]]):
    @classmethod
    def from_df(cls, df: pd.DataFrame) -> "EPSTrend":
        records = []
        for index, row in df.iterrows():
            records.append(
                PeriodEstimate(
                    period=index,
                    current=row["current"],
                    days7Ago=row["7daysAgo"],
                    days30Ago=row["30daysAgo"],
                    days60Ago=row["60daysAgo"],
                    days90Ago=row["90daysAgo"],
                )
            )
        return cls(records)

    @property
    def llm_readable(self) -> str:
        data = []
        for item in self.root:
            data.append(
                {
                    "period": item.period,
                    "current": item.current,
                    "7daysAgo": item.days7Ago,
                    "30daysAgo": item.days30Ago,
                    "60daysAgo": item.days60Ago,
                    "90daysAgo": item.days90Ago,
                }
            )
        df = pd.DataFrame(data).set_index("period")
        return df.to_string()


class AnalysPriceTargets(BaseModel):
    current: float
    high: float
    low: float
    mean: float
    median: float

    @property
    def llm_readable(self) -> str:
        return (
            f"Current: {self.current}\n"
            f"High: {self.high}\n"
            f"Low: {self.low}\n"
            f"Mean: {self.mean}\n"
            f"Median: {self.median}"
        )
