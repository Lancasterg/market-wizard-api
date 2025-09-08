import market_wizard_api.config.config_utils as env

HOST: str = env.env_str("HOST", default="127.0.0.1")
PORT: int = env.env_int("PORT", default=8084)
APP_NAME: str = env.env_str("APP_NAME", default="wizard_server")
