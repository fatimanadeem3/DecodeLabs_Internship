# =========================================================
#          AI RECOMMENDATION SYSTEM 
# =========================================================

import os
import time

# =========================================================
# DATABASE
# =========================================================

recommendation_data = [

    {
        "title": "Interstellar",
        "type": "Movie",
        "tags": ["sci-fi", "space", "adventure"]
    },

    {
        "title": "John Wick",
        "type": "Movie",
        "tags": ["action", "thriller", "crime"]
    },

    {
        "title": "The Notebook",
        "type": "Movie",
        "tags": ["romance", "drama"]
    },

    {
        "title": "Minecraft",
        "type": "Game",
        "tags": ["creative", "survival", "adventure"]
    },

    {
        "title": "FIFA 25",
        "type": "Game",
        "tags": ["sports", "competition"]
    },

    {
        "title": "Python Programming",
        "type": "Book",
        "tags": ["coding", "technology", "education"]
    },

    {
        "title": "Atomic Habits",
        "type": "Book",
        "tags": ["motivation", "self-improvement"]
    }

]

# =========================================================
# FUNCTIONS
# =========================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def loading_animation():

    print("\nAnalyzing Your Preferences", end="")

    for i in range(3):
        time.sleep(0.5)
        print(".", end="")

    print("\n")


def calculate_similarity(user_interests, item_tags):

    matched_tags = []

    for interest in user_interests:

        if interest in item_tags:
            matched_tags.append(interest)

    similarity_score = len(matched_tags)

    return similarity_score, matched_tags


def generate_recommendations(user_interests):

    results = []

    for item in recommendation_data:

        score, matched = calculate_similarity(
            user_interests,
            item["tags"]
        )

        if score > 0:

            results.append({

                "title": item["title"],
                "type": item["type"],
                "score": score,
                "matched_tags": matched

            })

    results.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True
    )

    return results


def show_recommendations(recommendations):

    print("=" * 65)
    print("                RECOMMENDED ITEMS")
    print("=" * 65)

    if len(recommendations) == 0:

        print("\nNo Recommendations Found.\n")
        return

    for item in recommendations:

        print(f"""
Title            : {item['title']}
Category         : {item['type']}
Similarity Score : {item['score']}
Matched Interests: {", ".join(item['matched_tags'])}
""")

        if item["score"] >= 3:
            status = "Highly Recommended"

        elif item["score"] == 2:
            status = "Recommended"

        else:
            status = "Worth Trying"

        print(f"Recommendation   : {status}")

        print("-" * 65)


# =========================================================
# MAIN PROGRAM
# =========================================================

while True:

    clear_screen()

    print("=" * 65)
    print("              AI RECOMMENDATION SYSTEM")
    print("=" * 65)

    print("""
1. Get Recommendations
2. Exit
""")

    user_choice = input("Enter Your Choice: ")

    # =====================================================
    # OPTION 1
    # =====================================================

    if user_choice == "1":

        clear_screen()

        print("=" * 65)
        print("                 ENTER YOUR INTERESTS")
        print("=" * 65)

        print("""
Available Interests:

sci-fi
space
adventure
action
thriller
crime
romance
drama
creative
survival
sports
competition
coding
technology
education
motivation
self-improvement
""")

        interests_input = input(
            "\nEnter Interests (comma separated): "
        ).lower()

        user_interests = [
            interest.strip()
            for interest in interests_input.split(",")
        ]

        loading_animation()

        recommendations = generate_recommendations(
            user_interests
        )

        show_recommendations(recommendations)

        input("\nPress Enter To Return To Main Menu...")

    # =====================================================
    # OPTION 2
    # =====================================================

    elif user_choice == "2":

        clear_screen()

        print("""
=========================================================
      THANK YOU FOR USING THE SYSTEM
=========================================================
""")

        break

    # =====================================================
    # INVALID OPTION
    # =====================================================

    else:

        print("\nInvalid Choice. Please Try Again.")

        time.sleep(1.5)