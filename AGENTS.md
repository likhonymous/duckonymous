# Agent Documentation

This document provides an overview of the agent framework used in this project, details on available agents, and instructions for creating new ones.

## 🤖 Agent Framework

All agents in this application are built upon a common foundation to ensure consistency and extensibility.

- **Base Class**: Every agent must inherit from the `BaseAgent` abstract class located in `backend/app/agents/base.py`.
- **Core Method**: Each agent is required to implement an asynchronous `run()` method, which contains the agent's core logic and returns a structured dictionary as its result.

This structure allows the system to treat all agents uniformly, making them easy to integrate, test, and manage.

---

## 🦆 Duckonymous Agent

The `Duckonymous` agent is an experimental agent designed to test and demonstrate how external APIs handle requests that lack specific tracking headers.

- **Purpose**: To prove that anonymous requests to the DuckDuckGo Chat API are blocked.
- **Location**: The agent's code is located at `backend/app/agents/duckonymous.py`.

### Interaction Pattern

1.  **API Endpoint**: The agent is exposed via a `GET` endpoint in the FastAPI application at `/duckonymous`. This is configured in `backend/app/main.py`.
2.  **Execution**: When the endpoint is hit, it creates an instance of the `DuckonymousAgent` and calls its `run()` method.
3.  **Input**: The current version of the agent requires no input, as it uses a hardcoded payload for its test request.
4.  **Output**: The agent returns a JSON object containing the results of the API call. On a successful block (the expected outcome), the JSON will look like this:
    ```json
    {
      "status": 418,
      "success": false,
      "error": "Client error '418 I'm a teapot' for url '...'"
    }
    ```

---

## 🛠️ Extension Guide

Adding a new agent to the system is straightforward.

### 1. Create the Agent Class
Create a new file in `backend/app/agents/`, for example, `my_new_agent.py`. Inside this file, define a new class that inherits from `BaseAgent`.

```python
# backend/app/agents/my_new_agent.py
from .base import BaseAgent
from typing import Dict, Any

class MyNewAgent(BaseAgent):
    name = "my-new-agent"
    description = "This is a new agent that does something cool."

    async def run(self, some_input: str) -> Dict[str, Any]:
        # Agent logic goes here
        return {"message": f"Processed input: {some_input}"}
```

### 2. Expose via FastAPI
Open `backend/app/main.py` and add a new endpoint to expose your agent.

```python
# backend/app/main.py
# ... existing imports
from agents.my_new_agent import MyNewAgent

# ... existing code

@app.get("/my-new-agent/{some_input}")
async def my_new_agent_endpoint(some_input: str):
    agent = MyNewAgent()
    result = await agent.run(some_input)
    return result
```

### 3. Testing
You can test your new endpoint by running the server and sending a request, for example, using `curl`.

```bash
# Make sure the uvicorn server is running
curl http://localhost:8000/my-new-agent/hello
```

---

##  sandbox️ Sandbox Note

For any agent that needs to perform potentially risky operations, such as executing arbitrary code, accessing the file system extensively, or interacting with external websites in a complex manner, it is crucial to run them within the designated **sandbox environment**. The main FastAPI application is not isolated and should only host trusted, well-defined agents.
