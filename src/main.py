
from src.chatbot import Chatbot

def main():
    """
    The main function for the chatbot CLI.
    """
    bot = Chatbot()
    print("Welcome to the Medical Prognosis Chatbot!")
    print("You can type 'exit' at any time to quit.")

    while True:
        user_input = input("\nPlease describe your symptoms (separated by commas): ")
        if user_input.lower() == "exit":
            break

        prognosis = bot.get_prognosis(user_input)

        if prognosis:
            print(f"\nBased on your symptoms, you might have: {prognosis['name']}")
            print(f"\nPrognosis: {prognosis['prognosis']}")
            print(f"\nSuggested Action: {prognosis['service_suggestion']}")
        else:
            print("\nI'm sorry, I couldn't find a matching condition based on your symptoms. Please consult a real doctor.")

if __name__ == "__main__":
    main()

