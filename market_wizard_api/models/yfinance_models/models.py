from datetime import datetime
from pydantic import BaseModel, RootModel, Field, ConfigDict
from enum import StrEnum


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
