from prompts import classify_intent
from logger import log_route

print("Prompt Router Started")

while True:
    user_input = input("\nUser: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    intent, confidence = classify_intent(user_input)

    print(f"Detected Intent: {intent}")
    print(f"Confidence: {confidence}")

    log_route(user_input, intent, confidence)

    if intent == "code":
        print("Routing to Code Expert...")
    elif intent == "data":
        print("Routing to Data Analyst...")
    elif intent == "writing":
        print("Routing to Writing Coach...")
    elif intent == "career":
        print("Routing to Career Advisor...")
    else:
        print("Intent unclear. Asking for clarification.")
