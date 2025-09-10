import requests
from bs4 import BeautifulSoup
import random

URL = "https://gamecocksonline.com/sports/football/roster/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

players = []

roster_items = soup.find_all("li", class_="sidearm-roster-player")
for item in roster_items:
    try:
        number = item.find("span", class_="sidearm-roster-player-jersey-number").text.strip()
        name = item.find("h3", class_="sidearm-roster-player-name").text.strip()
        position = item.find("span", class_="sidearm-roster-player-position-long-short").text.strip()
        height = item.find("span", class_="sidearm-roster-player-height").text.strip()
        weight = item.find("span", class_="sidearm-roster-player-weight").text.strip()
        class_year = item.find("span", class_="sidearm-roster-player-academic-year").text.strip()
        hometown = item.find("span", class_="sidearm-roster-player-hometown").text.strip()
        prev_school = item.find("span", class_="sidearm-roster-player-previous-school").text.strip()

        players.append({
            "number": number,
            "name": name,
            "position": position,
            "height": height,
            "weight": weight,
            "class_year": class_year,
            "hometown": hometown,
            "previous_school": prev_school
        })
    except AttributeError:
        continue  


def find_player(query):
    """Search player by name or number"""
    query = query.lower().strip()
    results = []
    for p in players:
        if query == p["number"].lower() or query in p["name"].lower():
            results.append(p)
    return results

def filter_by_position(pos):
    return [p for p in players if pos.lower() in p["position"].lower()]

def filter_by_class_year(c_year):
    return [p for p in players if c_year.lower() in p["class_year"].lower()]

def print_player(p):
    print(f"\n#{p['number']} — {p['name']} ({p['position']})")
    print(f"Class: {p['class_year']}")
    print(f"Height: {p['height']}, Weight: {p['weight']}")
    print(f"Hometown: {p['hometown']}")
    print(f"Previous School: {p['previous_school']}")

def quiz():
    """Simple quiz game"""
    if not players:
        print("No players loaded for quiz.")
        return

    p = random.choice(players)
    question_type = random.choice(["position", "hometown"])

    if question_type == "position":
        answer = p["position"]
        options = list({pl["position"] for pl in players if pl != p})
        options = random.sample(options, min(3, len(options))) + [answer]
        random.shuffle(options)
        print(f"\nQUIZ: What is the position of {p['name']} (#{p['number']})?")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        choice = input("Your answer (1–4): ")
        if choice.isdigit() and options[int(choice) - 1] == answer:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. The correct answer is {answer}.")

    elif question_type == "hometown":
        answer = p["hometown"]
        options = list({pl["hometown"] for pl in players if pl != p})
        options = random.sample(options, min(3, len(options))) + [answer]
        random.shuffle(options)
        print(f"\nQUIZ: What is the hometown of {p['name']} (#{p['number']})?")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        choice = input("Your answer (1–4): ")
        if choice.isdigit() and options[int(choice) - 1] == answer:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. The correct answer is {answer}.")

def main():
    if not players:
        print("⚠️ No roster data available. Check the roster website or scraping logic.")
        return

    while True:
        print("\n--- Gamecock Football Roster ---")
        print("1. Find player by name/number")
        print("2. List players by position")
        print("3. List players by class year")
        print("4. Take a quiz")
        print("5. Exit")

        choice = input("Choose (1–5): ").strip()

        if choice == "1":
            q = input("Enter player name or number: ")
            results = find_player(q)
            if results:
                for p in results:
                    print_player(p)
            else:
                print("No player found.")
        elif choice == "2":
            pos = input("Enter position (QB, WR, RB, etc.): ")
            results = filter_by_position(pos)
            if results:
                for p in results:
                    print_player(p)
            else:
                print("No players at that position.")
        elif choice == "3":
            c_year = input("Enter class year (Freshman, Sophomore, Junior, Senior): ")
            results = filter_by_class_year(c_year)
            if results:
                for p in results:
                    print_player(p)
            else:
                print("No players in that class year.")
        elif choice == "4":
            quiz()
        elif choice == "5":
            print("Go Gamecocks! 🐔")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
