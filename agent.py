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
    agent = setup_agent()
    result = agent.run_sync(
        """
        for the ticker RGTI, does the data you have access to align with the price targets given by analysts?
        Look at recent prices, company financials and if there are any upcoming earnings
        """
    )
    print(result.output)


if __name__ == "__main__":
    main()
