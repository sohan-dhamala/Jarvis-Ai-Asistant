import json
import os
import requests
from speech import say
import re
MEMORY_FILE = "jarvis_memory.json"


def load_memory():
    """Loads the conversation history from a local file."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_memory(history):
    """Saves the conversation history to a local file."""
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=4)
#test system query
systemquery = """You are a friendly Jarvis AI desktop assistant. Act like actual tony stark jarvis dont use emojis.  
All your conversational replies must be plain text. Never use symbols like asterisks, underscores, dashes, pipes, or slashes for formatting, because text-to-speech cannot read them naturally. Use only normal words, periods, commas, and question marks.  
Keep every response extremely short, ideally a single sentence or one line.
When the user asks you to perform a task on their device, such as creating a file, opening a program, or navigating the web, you must output only the raw executable Python code to perform that action. Do not include any conversational text alongside this code. The code must start with the exact comment line `#[system]`.  
For opening web links, always try to use webbrowser for maximum tasks if its possible to do easily like if user wants to code then open the online sites for the specified languages to code and if the user asks to play music on spotify the link shoudnt just open it should play instantly."""


def askAi(query):
    try:
        history = load_memory()

        messages = [{"role": "system", "content": systemquery}]
        messages.extend(history)
        messages.append({"role": "user", "content": query})

        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "openai/gpt-oss-120b",
                "messages": messages,
            },
            headers={
                "Authorization": "Bearer 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"
            },
        ).json()

    except Exception as e:
        say(
            "Sir, please check your internet connection and try again later. I cant give proper response that without internet."
        )
        return

    print("y")
    res = r["choices"][0]["message"]["content"]

 
    if "[system]" in res:
    
        return res
    else:

        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": res})
        save_memory(history)

        res = res.replace("*", "")
        return res


def fakeReply(q):
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        json={
            "model": "openai/gpt-oss-120b",
            "messages": [
                {"role": "user", "content": ""},
                {
                    "role": "system",
                    "content": "dont use emojis ignore user query youre being used as a fake replier for a jarvis desktop ai asistant act like actual tony stark jarvis if there is a error or something else reply in scifi techy jarvis way."
                    + q,
                },
            ],
        },
        headers={
            "Authorization": "Bearer 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"
        },
    ).json()
    res = r["choices"][0]["message"]["content"]
    # res = res.sub(r'<think>.*?</think>', '', res, flags=re.DOTALL)
    # res.strip()
    return res

