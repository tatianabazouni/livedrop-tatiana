import requests
import sys
import json
from datetime import datetime
from pathlib import Path

def get_ngrok_url():
    url = input("Enter your ngrok URL: ").strip().rstrip("/")
    if not url.startswith("http"):
        print("Invalid URL.")
        sys.exit(1)
    return url

def check_server(url):
    try:
        r = requests.get(f"{url}/health", timeout=10)
        if r.status_code == 200:
            print("Server is healthy.\n")
        else:
            print(f"Server error {r.status_code}")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

def chat_loop(url):
    endpoint = f"{url}/chat"
    log = []
    print("Type 'exit' to quit.\n")
    while True:
        q = input("You: ").strip()
        if q.lower() in ("exit", "quit"):
            break
        if not q:
            continue
        try:
            r = requests.post(endpoint, json={"query": q}, timeout=60)
            if r.status_code != 200:
                print(f"Error {r.status_code}: {r.text}")
                continue
            data = r.json()
            answer = data.get("response", "No response.")
            sources = data.get("sources", [])
            confidence = data.get("confidence", "Unknown")
            print(f"\n{answer}")
            print(f"Sources: {sources if sources else 'None'}")
            print(f"Confidence: {confidence}\n")
            log.append({"timestamp": datetime.now().isoformat(), "query": q, "response": data})
        except requests.RequestException as e:
            print(f"Network error: {e}")
    if log:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = Path(f"ngrok_chat_{ts}.json")
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=2, ensure_ascii=False)
        print(f"Log saved: {log_file}")

def main():
    url = get_ngrok_url()
    check_server(url)
    chat_loop(url)

if __name__ == "__main__":
    main()
