from resort import Resort
from data_weather import *


"""
    Populate resort objects with all data
"""
# create 5 Resort objects
kirkwood = Resort("Kirkwood")
aspen = Resort("Aspen Snowmass")
crystal = Resort("Crystal Mountain")
gore = Resort("Gore Mountain")
heavenly = Resort("Heavenly")

# append all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]


set_weather(Resorts)

# print(type(Resorts[0].weather[0].date))
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"
    if user_message in ("show me date",):
        return Resorts[0].weather[0].__str__()
    return "I don't understand"
