import yfinance as yf
from market_wizard_api.models.yfinance_models.models import OHLCVData

yf.enable_debug_mode()
ticker = "NVDA"
period = "1y"
response = list(yf.Ticker(ticker).history(period=period).to_json(orient="records"))
OHLCVData.model_validate(response)
print(response)
