from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import asyncio

from dotenv import load_dotenv

load_dotenv()



async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["C:\\Personal\\MCP\\langchain_mcp\\app\\mcptools\\mathserver.py"],
                "transport":"stdio",
            },
            
            "weather":{
                "url": "http://localhost:8000/mcp",
                "transport":"streamable-http",
            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
     
    tools=await client.get_tools()
    model= ChatGroq(model="qwen-qwq-32b")
    agent= create_react_agent(
        model, tools
    )
    
    math_response= await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is (3 + 5) x 12?"}]}
    )
    
    print("Math Response:" , math_response['messages'][-1].content)
    
    weather_response= await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in california?"}]}
    )
    
    print("Math Response:" , weather_response['messages'][-1].content)
    
asyncio.run(main())