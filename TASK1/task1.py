# =========================================================
#        Decodelabs - SmartBot - Rule Based Chatbot
# =========================================================

import random
from datetime import datetime, date

# ---------------- BOT MEMORY ----------------
user_name = ""

# ---------------- RANDOM RESPONSES ----------------
jokes = [
    "Why don’t robots get tired? Because they recharge themselves 😂",
    "Why was the computer cold? It forgot to close Windows 🪟😂",
    "Why did the AI fail school? Too many neural breakdowns 🤖😂"
]

motivation = [
    "Believe in yourself and keep moving forward 🚀",
    "Every expert was once a beginner ⭐",
    "Success comes from consistency 💪",
    "Small progress is still progress 🌱"
]

# ---------------- WELCOME SCREEN ----------------
print("=" * 60)
print("        🤖 SMARTBOT - AI CHATBOT")
print("=" * 60)
print("Type 'Anything to Talk' to start chatting with SmartBot! 😊")
print("Type 'bye' anytime to exit")
print("=" * 60)

# ---------------- MAIN LOOP ----------------
while True:

    # Handle Ctrl + C safely
    try:
        user = input("\nYou: ").lower().strip()

    except KeyboardInterrupt:
        print("\n\nSmartBot: Program stopped safely 👋")
        break

    # Handle empty input
    if user == "":
        print("SmartBot: Please type something 😊")
        continue

    # ---------------- GREETINGS ----------------
    if user in ["hi", "hello", "hey"]:

        if user_name == "":
            print("SmartBot: Hello 👋 Nice to meet you!")

        else:
            print(f"SmartBot: Welcome back, {user_name} 😊")

    # ---------------- USER NAME ----------------
    elif "my name is" in user:

        name = user.replace("my name is", "").strip()

        if name == "":
            print("SmartBot: Please tell me your name properly 😊")

        else:
            user_name = name.title()
            print(f"SmartBot: Nice to meet you, {user_name}! 🎉")

    elif user == "what is my name":

        if user_name != "":
            print(f"SmartBot: Your name is {user_name} 😄")

        else:
            print("SmartBot: I don't know your name yet.")

    # ---------------- BOT DETAILS ----------------
    elif user == "your name":
        print("SmartBot: My name is SmartBot 2.0 🤖")

    elif user == "how are you":
        print("SmartBot: I'm functioning perfectly! ⚡")

    elif user == "your age":
        print("SmartBot: Robots don't age like humans 😎")

    # ---------------- TIME ----------------
    elif user == "time" or user == "what is the time":

        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("SmartBot: Current time is", current_time)

    # ---------------- DATE ----------------
    elif user == "date" or user == "what is the date":

        today = date.today()
        print("SmartBot: Today's date is", today)

    # ---------------- CALCULATOR ----------------
    elif user == "calculator":

        print("\n📌 Calculator Mode")
        print("Operations: +  -  *  /")

        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print("SmartBot: Result =", num1 + num2)

            elif operator == "-":
                print("SmartBot: Result =", num1 - num2)

            elif operator == "*":
                print("SmartBot: Result =", num1 * num2)

            elif operator == "/":

                if num2 != 0:
                    print("SmartBot: Result =", num1 / num2)

                else:
                    print("SmartBot: Cannot divide by zero ❌")

            else:
                print("SmartBot: Invalid operator ❌")

        except ValueError:
            print("SmartBot: Please enter valid numbers ❌")

    # ---------------- JOKES ----------------
    elif user == "joke":
        print("SmartBot:", random.choice(jokes))

    # ---------------- MOTIVATION ----------------
    elif user == "motivate me":
        print("SmartBot:", random.choice(motivation))

    # ---------------- GUESSING GAME ----------------
    elif user == "game":

        secret = random.randint(1, 5)

        print("\n🎮 Guess the number between 1 and 5")

        try:
            guess = int(input("Your guess: "))

            if guess == secret:
                print("SmartBot: 🎉 Correct! You won!")

            else:
                print(f"SmartBot: Wrong 😅 The number was {secret}")

        except ValueError:
            print("SmartBot: Please enter a valid number ❌")

    # ---------------- HELP MENU ----------------
    elif user == "help":

        print("\n" + "=" * 40)
        print("📌 AVAILABLE COMMANDS")
        print("=" * 40)

        print("👋 Greetings")
        print(" - hi")
        print(" - hello")
        print(" - hey")

        print("\n🧠 Chat Features")
        print(" - my name is ____")
        print(" - what is my name")
        print(" - your name")
        print(" - how are you")
        print(" - your age")

        print("\n🕒 Utility Features")
        print(" - time")
        print(" - what is the time")
        print(" - date")
        print(" - what is the date")
        print(" - calculator")

        print("\n🎉 Fun Features")
        print(" - joke")
        print(" - motivate me")
        print(" - game")

        print("\n🚪 Exit")
        print(" - bye")

        print("=" * 40)

    # ---------------- EXIT ----------------
    elif user == "bye":
        print("SmartBot: Goodbye 👋 Have an amazing day!")
        break

    # ---------------- UNKNOWN COMMAND ----------------
    else:
        print("SmartBot: Sorry 😅 I am not sure how to help with that.")