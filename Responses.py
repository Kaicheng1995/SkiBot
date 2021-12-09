from database import *

Resorts = get_all_data()

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"
    if user_message in ("show me date",):
        return Resorts[0].weather.date
    return "I don't understand"
