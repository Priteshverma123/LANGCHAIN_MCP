from mcp.server.fastmcp import FastMCP


mcp=FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """_summary_
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """_summary_
    Multiply two numbers
    """
    return a*b


# transport protocol stdio use the standard stinput/output methods

if __name__=="__main__":
    mcp.run(transport="stdio")
