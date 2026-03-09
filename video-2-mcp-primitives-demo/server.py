from mcp.server import FastMCP


# Definir el servidor MCP
mcp = FastMCP("support-copilot")


# RESOURCE
@mcp.resource("policy://refund")
def refund_policy():
    """Resource que devuelve la política de reembolso de la empresa."""
    with open("refund_policy.md", encoding="utf-8") as f:
        return f.read()


# PROMPT
@mcp.prompt()
def refund_response_template(order_id: str, decision: str):
    """Prompt que genera una respuesta para el cliente basada en la decisión de reembolso."""
    return f"""
            You are a support agent.

            Order ID: {order_id}

            Decision: {decision}

            Respond politely and reference the refund policy.
            """


# TOOL
@mcp.tool()
def create_refund_ticket(order_id: str, reason: str):
    """Tool que simula la creación de un ticket de reembolso en el sistema de soporte."""
    print("Creating refund ticket")

    return {
        "ticket_id": "REFUND-456",
        "status": "created"
    }


if __name__ == "__main__":
    mcp.run()
