# LangChain MCP Integration Project

A demonstration project showcasing the integration of **Model Context Protocol (MCP)** with LangChain and LangGraph to create intelligent agents with external tool capabilities.

## 🚀 About This Project

This project explores the powerful combination of MCP servers with LangChain's agent framework to build AI agents that can interact with external tools and services. I've started experimenting with MCP to understand how it can enhance AI applications by providing standardized interfaces for tool integration.

## 🔧 What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables AI applications to securely connect to external data sources and tools. It provides a standardized way for AI models to:

- Access external APIs and services
- Interact with databases and file systems
- Perform calculations and data processing
- Integrate with third-party applications

MCP acts as a bridge between AI models and the external world, allowing for more capable and versatile AI applications while maintaining security and control.

### Key Benefits of MCP:
- **Standardized Interface**: Consistent way to connect AI models with external tools
- **Security**: Controlled access to external resources
- **Extensibility**: Easy to add new tools and capabilities
- **Interoperability**: Works across different AI frameworks and models

## 🏗️ Project Structure

```
langchain-mcp/
├── client.py          # Main MCP client implementation
├── main.py           # Entry point
├── README.md         # This file
└── requirements.txt  # Dependencies
```

## 🛠️ Current Implementation

This project demonstrates:

1. **Multi-Server MCP Client**: Connects to multiple MCP servers simultaneously
2. **Math Server Integration**: Local Python-based math computation server
3. **Weather API Integration**: HTTP-based weather service
4. **LangGraph Agent**: ReAct agent that can use MCP tools intelligently

### Supported Tools:
- **Math Operations**: Complex mathematical calculations via local MCP server
- **Weather Queries**: Real-time weather information via HTTP MCP server

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- GROQ API key (for the language model)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create .env file
GROQ_API_KEY=your_groq_api_key_here
```

### Running the Project

```bash
python client.py
```

## 🔍 How It Works

The project uses a **ReAct agent** (Reasoning + Acting) that can:

1. **Analyze** user queries to determine what tools are needed
2. **Plan** the sequence of actions required
3. **Execute** tool calls via MCP servers
4. **Synthesize** results into coherent responses

### Example Interactions:

- **Math Query**: "What is (3 + 5) x 12?"
  - Agent identifies this as a math problem
  - Calls the math MCP server
  - Returns calculated result: 96

- **Weather Query**: "What is the weather in California?"
  - Agent recognizes this as a weather request
  - Calls the weather MCP server
  - Returns current weather information

## 🎯 Why MCP Matters

MCP represents a significant advancement in AI tooling because it:

- **Standardizes** how AI models interact with external systems
- **Simplifies** the process of adding new capabilities to AI applications
- **Enhances** security by providing controlled access mechanisms
- **Enables** more complex, multi-step AI workflows

## 🚧 Future Enhancements

Planning to expand this project with:

- [ ] Database integration via MCP
- [ ] File system operations
- [ ] Web scraping capabilities
- [ ] Custom business logic servers
- [ ] Authentication and authorization mechanisms
- [ ] Monitoring and logging capabilities

## 🤝 Contributing

This is an experimental project to explore MCP capabilities. Feel free to:
- Suggest new MCP server integrations
- Improve the agent's reasoning capabilities
- Add new example use cases
- Enhance error handling and robustness

## 📚 Learning Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

## 🔗 Tech Stack

- **MCP**: Model Context Protocol for tool integration
- **LangChain**: Framework for building applications with language models
- **LangGraph**: Library for building stateful, multi-actor applications
- **GROQ**: Fast inference for language models
- **Python**: Core programming language

## 📈 Project Status

🟢 **Active Development** - Actively exploring MCP capabilities and building new integrations

---

*This project is part of my exploration into the Model Context Protocol and its potential for building more capable AI applications. MCP represents an exciting direction for AI tooling, and I'm excited to see how it evolves!*