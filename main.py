import requests
import json

def main():
    """
    This script attempts to make an anonymous request to the DuckDuckGo chat API.
    It omits the tracking headers (x-vqd-hash-1 and x-fe-signals) to protect user privacy.
    However, the server is expected to block this request with a 418 "I'm a Teapot" error,
    demonstrating that anonymous access to the chat API is not permitted.
    """
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
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
    }

    payload = {
        "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
        "messages": [{"role": "user", "content": "Duck"}],
    }

    print("Attempting to make an anonymous request to the DuckDuckGo chat API...")
    try:
        with requests.post(url, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()
            print("Request successful. Response:")
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    print(decoded_line)

    except requests.exceptions.RequestException as e:
        print(f"Request failed as expected: {e}")
        print("This demonstrates that DuckDuckGo does not allow anonymous access to its chat API.")

if __name__ == "__main__":
    main()
