from typing import cast
import redis.asyncio as redis
from market_wizard_api.config import config


class RedisClient:
    _client: redis.Redis | None = None

    @classmethod
    def init_client(cls):
        if cls._client is None:
            cls._client = redis.Redis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                decode_responses=True,
                db=0,
                socket_timeout=5,
            )
        return cls._client

    @classmethod
    async def close_client(cls) -> None:
        if cls._client:
            await cls._client.aclose()

    @classmethod
    async def get_data(cls, unique_id: str) -> str | None:
        try:
            cached_data = await cls.init_client().get(unique_id)
            cached_data = cast(str | None, cached_data)

            return cached_data
        except (TimeoutError, ConnectionError) as e:
            return None

    @classmethod
    async def write_data(
        cls, unique_id: str, data: str, ttl: int | None = None
    ) -> None:

        try:
            await cls.init_client().set(unique_id, data)
        except (TimeoutError, ConnectionError) as e:
            return None
