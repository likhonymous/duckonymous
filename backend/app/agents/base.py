from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    Every agent should implement the `run` method.
    """

    name: str = "base-agent"
    description: str = "Abstract agent interface."

    @abstractmethod
    async def run(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Run the agent and return structured output.
        """
        pass
