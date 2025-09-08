from fastapi.concurrency import asynccontextmanager
from market_wizard_api import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from t212.async_client import AsyncTrading212Client

import uvicorn

from market_wizard_api.routers import y_finance_router, portfolio_router


app = FastAPI(
    title=config.APP_NAME,
    description="Market wizard api",
    version="0.0.1",
)


origins = [
    "*",  # Allows all origins
    "http://127.0.0.1:3000",
    "http://localhost:3000"
    "http://127.0.0.1:8084",  # Your FastAPI backend URL (though not strictly needed for origins, good for testing)
]

app.include_router(y_finance_router)
app.include_router(portfolio_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": f"Welcome to {config.APP_NAME}"}


@asynccontextmanager
async def lifespan(app: FastAPI):

    AsyncTrading212Client.init_client()

    yield
    AsyncTrading212Client.close_client()


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
