from database import *


# get real time Resorts data
Resorts = populate_data()

# conversation logic
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"
    if user_message in ("show me date",):
        return Resorts[0].weather[0].__str__()
    return "I don't understand"
