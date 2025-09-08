# market-wizard-api

Backend for the [market-wizard web application](https://github.com/Lancasterg/market-wizard-frontend), which allows users to visualise their trading 212 investment portfolio. It uses the async `python-trading-212` library that I have also written. 

---

## Installation

```bash
git clone git@github.com:Lancasterg/market-wizard-api.git
cd market-wizard-api
poetry install
````

---

## Configuration

Set your Trading 212 API key and environment as environment variables:

```bash
export T212_API_KEY=123_YOUR_API_KEY
export T212_ENVIRONMENT=live   # or demo
```

---

## Usage

```
poetry run python -m market_wizard_api.server.py
```
In a new terminal window:

```
bash curls/stock_data.sh
```