from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def weather(location:str) -> str:
    """give weather of location"""
    
    return "its always raining in mumbai"

if __name__=="__main__":
    mcp.run(transport="streamable-http")