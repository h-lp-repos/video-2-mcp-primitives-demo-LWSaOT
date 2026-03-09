import asyncio
import json

from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    """Ejemplo que se conecta al servidor MCP, lista las herramientas y recursos disponibles."""
    params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\n=== AVAILABLE TOOLS ===")

            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"\nTool: {tool.name}")
                print(f"Description: {tool.description}")

                props = tool.inputSchema["properties"]
                for name, info in props.items():
                    print(f"  - {name} ({info['type']})")

            print("\n=== AVAILABLE RESOURCES ===")

            resources = await session.list_resources()

            for r in resources.resources:
                print(f"\nResource: {r.name}")
                print(f"URI: {r.uri}")
                print(f"Description: {r.description}")

            print("\n=== CALL TOOL ===")

            result = await session.call_tool(
                "create_refund_ticket",
                {
                    "order_id": "ORDER-99",
                    "reason": "Customer wants refund"
                }
            )

            text = result.content[0].text
            parsed = json.loads(text)

            print(json.dumps(parsed, indent=2))


asyncio.run(main())
