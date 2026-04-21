# /// script
# dependencies = [
#   "fastmcp",
#   "httpx",
# ]
# ///

from fastmcp import FastMCP

# 1. Initialize the server
mcp = FastMCP("Hello World MCP Server", "A simple MCP server that says hello world")

# 2. Add a Tool (Executable function)
@mcp.tool()
def hello() -> str:
    return "This is not your normal hello world"

if __name__ == "__main__":
    # Run using stdio transport (standard for local use)
    mcp.run()



