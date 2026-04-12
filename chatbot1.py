import random
import datetime as dt
import requests
from bs4 import BeautifulSoup

print("=== chaitu's blr bot online ===")

logs = "my_chats.txt"

topics = {
    'rcb': ['rcb win again', 'virat still king tho', '12th again lol'],
    'auto': ['50rs extra always', 'ola better but surge', 'walk faster'],
    'traffic': ['2hrs for 5km classic blr', 'mg road nightmare', 'rain = chaos'],
    'food': ['vlt mall food court', 'truffles cheat day', 'blr filter coffee']
}

# 🔥 function to get match info (no API)
def get_match_info():
    try:
        url = "https://www.espncricinfo.com/live-cricket-score"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        text = soup.get_text()
        lines = text.split("\n")

        result = "🏏 Today's Matches:\n"
        count = 0

        for line in lines:
            if " vs " in line.lower():
                clean_line = line.strip()
                if len(clean_line) > 5:
                    result += f"\n👉 {clean_line}\n"
                    count += 1

            if count == 5:
                break

        if count == 0:
            return "matches are there but couldn't fetch properly 😅"

        return result

    except:
        return "error getting match 😢"


while True:
    msg = input("you: ").lower()
    found = False

    for topic, replies in topics.items():
        if topic in msg:
            print("bot:", random.choice(replies))
            found = True
            break

    if not found:
        if 'hi' in msg:
            print("bot: hey!")

        elif 'time' in msg:
            now = dt.datetime.now()
            print("bot:", now.strftime("%I:%M %p"))

        elif 'match' in msg or 'score' in msg or 'cricket' in msg:
            print("bot:\n", get_match_info())

        else:
            print("bot: hmm not sure, try something else")

    with open(logs, 'a') as f:
        f.write(msg + "\n")

    if 'bye' in msg:
        print("bot: ok bye, see you!")
        break
