import httpx
from typing import Dict, Any
from .base import BaseAgent

class DuckonymousAgent(BaseAgent):
    """
    Duckonymous Agent
    Attempts an anonymous request to the DuckDuckGo chat API.
    Expected to fail with 418 (I'm a teapot), proving anonymous
    access is blocked.
    """

    name = "duckonymous"
    description = "Tests anonymous DuckDuckGo Chat API access."

    async def run(self) -> Dict[str, Any]:
        url = "https://duckduckgo.com/duckchat/v1/chat"

        headers = {
            "accept": "text/event-stream",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://duckduckgo.com",
            "referer": "https://duckduckgo.com/",
            "sec-ch-ua": '"Chromium";v="139", "DuckDuckGo";v="139", "Not;A=Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
            ),
        }

        payload = {
            "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
            "messages": [{"role": "user", "content": "Duck"}],
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=payload)
                response.raise_for_status()

                return {
                    "status": response.status_code,
                    "success": True,
                    "response": response.text.splitlines(),
                }
            except httpx.RequestError as e:
                return {"status": None, "success": False, "error": str(e)}
            except httpx.HTTPStatusError as e:
                return {
                    "status": e.response.status_code,
                    "success": False,
                    "error": str(e),
                }
