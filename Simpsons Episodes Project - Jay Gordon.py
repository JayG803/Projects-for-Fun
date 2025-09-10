import random

episodes = [
    # Season 1
    {
        "title": "Simpsons Roasting on an Open Fire",
        "season": 1,
        "characters": ["Homer", "Marge", "Bart", "Lisa", "Maggie", "Santa's Little Helper"],
        "scenes": ["Homer works as a mall Santa", "Family adopts Santa's Little Helper"]
    },
    {
        "title": "Bart the Genius",
        "season": 1,
        "characters": ["Bart", "Homer", "Marge", "Lisa", "Principal Skinner"],
        "scenes": ["Bart cheats on an IQ test", "Bart goes to a gifted school"]
    },
    {
        "title": "Moaning Lisa",
        "season": 1,
        "characters": ["Lisa", "Bleeding Gums Murphy", "Homer", "Marge", "Bart"],
        "scenes": ["Lisa feels depressed", "Lisa plays saxophone with Bleeding Gums Murphy"]
    },
    # Season 2
    {
        "title": "Bart Gets an F",
        "season": 2,
        "characters": ["Bart", "Homer", "Marge", "Lisa", "Martin Prince"],
        "scenes": ["Bart struggles with school", "Bart prays to pass his test"]
    },
    {
        "title": "Two Cars in Every Garage and Three Eyes on Every Fish",
        "season": 2,
        "characters": ["Homer", "Mr. Burns", "Marge", "Bart", "Lisa"],
        "scenes": ["Bart catches Blinky the three-eyed fish", "Mr. Burns runs for governor"]
    },
    {
        "title": "Homer vs. Lisa and the 8th Commandment",
        "season": 2,
        "characters": ["Homer", "Lisa", "Marge", "Bart", "Ned Flanders"],
        "scenes": ["Homer gets illegal cable TV", "Lisa struggles with morality"]
    },
    # Season 3
    {
        "title": "Stark Raving Dad",
        "season": 3,
        "characters": ["Homer", "Lisa", "Bart", "Michael Jackson (Leon Kompowsky)"],
        "scenes": ["Homer goes to a mental institution", "Michael Jackson helps Bart write Lisa’s birthday song"]
    },
    {
        "title": "Flaming Moe's",
        "season": 3,
        "characters": ["Moe", "Homer", "Bart", "Lisa", "Marge"],
        "scenes": ["Homer invents the Flaming Moe drink", "Moe steals Homer’s idea"]
    },
    {
        "title": "Homer at the Bat",
        "season": 3,
        "characters": ["Homer", "Mr. Burns", "Smithers", "Bart", "Baseball Stars"],
        "scenes": ["Mr. Burns hires MLB players", "Homer wins softball game with Wonderbat"]
    },
    # Season 4
    {
        "title": "A Streetcar Named Marge",
        "season": 4,
        "characters": ["Marge", "Homer", "Bart", "Lisa", "Maggie"],
        "scenes": ["Marge stars in a play", "Maggie escapes the daycare"]
    },
    {
        "title": "Homer the Heretic",
        "season": 4,
        "characters": ["Homer", "Marge", "Bart", "Lisa", "Ned Flanders"],
        "scenes": ["Homer skips church", "Homer has a dream about God"]
    },
    {
        "title": "Marge vs. the Monorail",
        "season": 4,
        "characters": ["Homer", "Marge", "Bart", "Lisa", "Lyle Lanley", "Mr. Burns"],
        "scenes": ["Springfield buys a monorail", "Homer drives the monorail"]
    },
    # Season 5
    {
        "title": "Cape Feare",
        "season": 5,
        "characters": ["Bart", "Sideshow Bob", "Homer", "Marge", "Lisa"],
        "scenes": ["Sideshow Bob stalks Bart", "Family enters witness protection"]
    },
    {
        "title": "Homer Goes to College",
        "season": 5,
        "characters": ["Homer", "Mr. Burns", "Smithers", "College Nerds"],
        "scenes": ["Homer goes to college", "Homer throws wild parties"]
    },
    {
        "title": "Rosebud",
        "season": 5,
        "characters": ["Mr. Burns", "Smithers", "Homer", "Marge", "Bart", "Lisa", "Maggie"],
        "scenes": ["Mr. Burns loses his teddy bear Bobo", "Maggie adopts Bobo"]
    }
]

# --- Functions ---

def filter_by_character(name):
    """Find episodes featuring a specific character."""
    results = [ep for ep in episodes if name in ep["characters"]]
    return results

def filter_by_season(season):
    """Find episodes from a specific season."""
    results = [ep for ep in episodes if ep["season"] == season]
    return results

def ask_question(character):
    """Answer simple questions about a character."""
    results = filter_by_character(character)
    if results:
        print(f"\nEpisodes featuring {character}:")
        for ep in results:
            print(f"- {ep['title']} (Season {ep['season']})")
    else:
        print(f"\nSorry, no episodes found with {character} in this dataset.")

def quiz():
    """Simple Simpsons quiz game."""
    questions = [
        {
            "question": "What is the name of the Simpsons' dog?",
            "options": ["Santa's Little Helper", "Snowball II", "Bongo", "Laddie"],
            "answer": "Santa's Little Helper"
        },
        {
            "question": "Who shot Mr. Burns?",
            "options": ["Homer", "Maggie", "Smithers", "Bart"],
            "answer": "Maggie"
        },
        {
            "question": "What instrument does Lisa play?",
            "options": ["Piano", "Drums", "Saxophone", "Guitar"],
            "answer": "Saxophone"
        },
        {
            "question": "Which bartender runs Moe's Tavern?",
            "options": ["Barney", "Lenny", "Moe Szyslak", "Carl"],
            "answer": "Moe Szyslak"
        },
        {
            "question": "What drink did Homer invent?",
            "options": ["Flaming Moe", "Skittlebrau", "Buzz Cola", "Duff Beer"],
            "answer": "Flaming Moe"
        }
    ]

    q = random.choice(questions)
    print("\nQUIZ TIME!")
    print(q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    choice = input("Enter the number of your answer: ")
    try:
        if q["options"][int(choice) - 1] == q["answer"]:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. The correct answer is {q['answer']}.")
    except:
        print("Invalid choice!")

# --- Main Menu ---
def main():
    while True:
        print("\n--- The Simpsons Quiz ---")
        print("1. Filter episodes by character")
        print("2. Filter episodes by season")
        print("3. Ask about a character")
        print("4. Take a Simpsons quiz")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter character name: ")
            results = filter_by_character(name)
            if results:
                for ep in results:
                    print(f"- {ep['title']} (Season {ep['season']})")
            else:
                print("No episodes found.")
        elif choice == "2":
            season = int(input("Enter season number: "))
            results = filter_by_season(season)
            if results:
                for ep in results:
                    print(f"- {ep['title']} (Season {ep['season']})")
            else:
                print("No episodes found.")
        elif choice == "3":
            name = input("Ask about which character? ")
            ask_question(name)
        elif choice == "4":
            quiz()
        elif choice == "5":
            print("Goodbye! 🍩")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
