# AutoGen Learning Project

A comprehensive learning repository for exploring Microsoft's AutoGen framework for building multi-agent conversational AI systems.

## 📋 Project Overview

This project contains hands-on examples and implementations of AutoGen's multi-agent capabilities, from basic single agents to complex multi-agent teams with human-in-the-loop interactions. The repository is organized into different learning modules to progressively build understanding of AutoGen's features.

## 🏗️ Project Structure

```
AutoGen/
├── README.md
├── requirements.txt
├── first-autogen.ipynb              # Initial notebook (placeholder)
│
├── Basic AutoGen/                   # Fundamentals
│   ├── basic-autogen.ipynb         # Your first AutoGen agent
│   └── models.ipynb                # Model configuration examples
│
├── AgentChat Agent/                 # Agent communication patterns
│   ├── agent.ipynb                 # Agent creation and setup
│   ├── messages.ipynb              # Message handling
│   ├── running_&_observing.ipynb   # Agent execution monitoring
│   ├── structured_output.ipynb     # Structured response formatting
│   └── tools.ipynb                 # Tool integration
│
├── MulitAgent/                      # Multi-agent systems
│   ├── multiagent.ipynb            # Multi-agent team setup
│   ├── singleagent_team.ipynb      # Single agent teams
│   ├── team_operations.ipynb       # Team management operations
│   ├── managing_multiAgent_state.ipynb  # State management
│   ├── observing_teams.ipynb       # Team monitoring
│   ├── load_teamstate.ipynb        # State persistence
│   ├── termination.ipynb           # Termination conditions
│   └── team_state.json             # Saved team state
│
├── Advanced Integrations/           # Advanced features
│   └── human_in_loop.ipynb         # Human-in-the-loop workflows
│
├── Aysnc Functionality/             # Asynchronous operations
│   ├── async_function.ipynb        # Async function examples
│   └── aysnchronous.py             # Python async utilities
│
├── Analyzer GPT/                    # Data analysis agent
│   ├── app.py, main.py             # Main application and backend
│   ├── agents/, config/, models/, prompts/, teams/, temp/
│
├── DSA Solver Agent/                # Algorithmic problem-solving agent
│   ├── agent_backend.py, app.py, main.py
│   ├── agents/, config/, teams/, temp/, utils/
│
├── Travel Planner Agent/            # Automated travel planning agent
│   ├── main.py
│   ├── agents/, config/, models/, teams/, tests/, utils/
│
├── Autogen Projects/                # Project-level scripts and experiments
│   ├── AI-Interviewer.py           # Example project: AI-driven interviewer
│
└── autogen-env/                     # Virtual environment
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── share/
```
## 🧩 Project Highlights

### Analyzer GPT
An AI-powered digital data analysis agent. Users can upload datasets and request analyses in natural language. The agent executes code securely (using Docker), analyzes data, and streams results (text, charts, images) back to the user. Ideal for data scientists, analysts, and anyone needing automated insights from data.

**Features:**
- Upload CSVs and request custom analyses
- Secure code execution in isolated containers
- Multi-agent collaboration for analysis and code execution
- Real-time result streaming and visualization

### DSA Solver Agent
An agent system for solving Data Structures and Algorithms (DSA) problems. Accepts coding problems, selects appropriate algorithms, generates solutions, and explains reasoning. Useful for students, educators, and interview preparation.

**Features:**
- Accepts and solves coding problems
- Generates code and step-by-step explanations
- Supports various DSA topics and problem types
- Can be extended for custom problem sets

### Travel Planner Agent
An intelligent agent for automated travel planning. Accepts user preferences, searches for flights/hotels/activities, and generates optimized itineraries. Adapts plans based on feedback and can be extended for additional travel services.

**Features:**
- Accepts travel preferences and requirements
- Searches and books travel options
- Generates day-by-day itineraries
- Adapts to user feedback and changes

### Autogen Projects
Contains project-level scripts and experiments, such as the AI-Interviewer agent. These serve as templates or inspiration for building new agent-based solutions.

**Example:**
- AI-Interviewer.py: Simulates interview scenarios, asks questions, evaluates answers, and provides feedback for job seekers or educators.


## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- API key for your chosen model provider (Google/Gemini, OpenAI, Azure, etc.)

### Installation

1. **Clone/Download the repository**
   ```bash
   git clone <your-repo-url>
   cd AutoGen
   ```

2. **Set up virtual environment** (if not already created)
   ```bash
   python -m venv autogen-env
   .\autogen-env\Scripts\activate  # Windows
   # source autogen-env/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here  # if using OpenAI
   AZURE_API_KEY=your_azure_api_key_here    # if using Azure
   ```

### Running the Examples

Start with the basic examples and progress through the modules:

1. **Basic AutoGen** - Learn fundamental concepts
2. **AgentChat Agent** - Understand agent communication
3. **MulitAgent** - Explore multi-agent systems
4. **Advanced Integrations** - Human-in-the-loop workflows
5. **Async Functionality** - Asynchronous operations

## 📚 Learning Path

### 1. Basic AutoGen
- `basic-autogen.ipynb`: Create your first assistant agent using Gemini
- `models.ipynb`: Configure different model clients

### 2. AgentChat Agent
- `agent.ipynb`: Agent creation and configuration
- `messages.ipynb`: Message types and handling
- `structured_output.ipynb`: Formatting agent responses
- `tools.ipynb`: Integrating external tools

### 3. Multi-Agent Systems
- `multiagent.ipynb`: Creating teams of specialized agents
- `team_operations.ipynb`: Managing team interactions
- `termination.ipynb`: Setting up termination conditions
- `managing_multiAgent_state.ipynb`: State management across agents

### 4. Advanced Features
- `human_in_loop.ipynb`: Interactive workflows with user input
- `async_function.ipynb`: Asynchronous agent operations

## 🔧 Key Features Demonstrated

- **Single Agent Creation**: Basic assistant agents with custom system messages
- **Multi-Agent Teams**: Collaborative agent systems with role specialization
- **Human-in-the-Loop**: Interactive workflows requiring user input
- **State Management**: Persistent team states across sessions
- **Termination Conditions**: Custom stopping criteria for conversations
- **Async Operations**: Non-blocking agent operations
- **Model Integration**: Support for multiple AI providers (Gemini, OpenAI, Azure)

## 🛠️ Dependencies

The project uses the following main packages:

- `autogen-agentchat`: Core AutoGen agent chat functionality
- `autogen-core`: AutoGen core components
- `autogen_ext[openai,azure,docker]`: Extensions for OpenAI and Azure integration
- `groq`: Groq model integration
- `python-dotenv`: Environment variable management


## 📖 Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

**Happy Learning with AutoGen!** 🤖✨
