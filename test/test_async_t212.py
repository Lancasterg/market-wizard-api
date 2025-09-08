from t212.async_client import AsyncTrading212Client
import asyncio
import json


async def run():
    response = await AsyncTrading212Client.fetch_all_open_positions()
    print(response.model_dump_json(indent=4))


asyncio.run(run())
