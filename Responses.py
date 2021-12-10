from database import *


# get real time Resorts data
Resorts = populate_data()

# conversation logic
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup",):
        # return value is a tuple
        return "Hey! What can I do to help you today?",
    if user_message in ("recently open ski resorts", "resorts",):
        head = "Okay. Five ski resorts are currently or about to open:"
        info = print_resorts(Resorts)
        tail = "Which one do you prefer to go?"
        return head + "\n" * 2 + info, tail

    if user_message in ("weather",):
        return Resorts[0].weather[0].__str__(),
    return "I don't understand"
