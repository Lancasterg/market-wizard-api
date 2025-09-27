from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.mcp import MCPServerStreamableHTTP

import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
prompt = """
You are an investor making decisions about which companies to invest in.

You have access to the following MCP endpoints:
- stock_data
- balance_sheet
- financials
- stock_info
- available_tickers
- eps_trend
- price_targets
- news

You have access to financial data and need to use your initiative about which data you need to access
in order to answer the questions asked to you.

"""


def setup_agent() -> Agent:

    mcp_server = MCPServerStreamableHTTP("http://127.0.0.1:8084/mcp/")
    provider = GoogleProvider(
        api_key=GOOGLE_API_KEY, project="dev-sandbox", vertexai=False
    )
    model = GoogleModel("gemini-2.5-flash", provider=provider)
    agent = Agent(model, toolsets=[mcp_server])

    return agent


def main():
            # Tell me everything you know about the ticker "Hive".
        # I want you to gather all the information you can about it
    agent = setup_agent()
    result = agent.run_sync(
        # """
        # Summarize all the news stories for the ticker BITF 
        # Tell me if the sentiment towards BITF is positive or negative

        # Also look at the companies financials, price history and eps trend

        # I want to know if BITF is a good investment. I already own shares, but have lost a small amount of money on them. My entry point was $3.05
        # I am trying to decide whether to keep them or sell them. 

        # """

        """ 
        Can you compare BITF with HIVE please.

        Look at:
            - news sentiment
            - company financials
            - price history
            - eps trend
            - analyst price targets

        """
    )
    print(result.output)


if __name__ == "__main__":
    main()
