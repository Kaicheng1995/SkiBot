from database import *
from datetime import date, datetime

# get real time Resorts data
Resorts = populate_data()

"""
    takes in user message and return a tuple of responses
"""


def sample_responses(input_text):
    user_message = str(input_text).lower()

    # greeting
    if user_message in ("hello", "hi", "hola", "hey",):
        return "Hey! What can I do to help you today?",

    # ask recommendation
    if user_message in ("resorts",
                        "ski resorts",
                        "go ski",
                        "i want to go ski",
                        "please show me some ski resorts",
                        "can you recommend to me some ski resorts?",
                        "can you tell me some recently opened ski resorts?",):
        head = "Okay. Five ski resorts are currently or about to open:"
        info = print_resorts(Resorts)
        tail = "Where do you want to go?"
        return head + "\n" * 2 + info, tail

    # ask resort
    if user_message in ("kirkwood",
                        "i want to go to kirkwood",
                        "i prefer kirkwood",):
        head = "Here are some operating information of the kirkwood resort:"
        info = print_operation(Resorts[0])
        tail = "When do you plan to go?"
        return head + "\n" * 2 + info, tail

    # ask weather (single day)
    ask_weather_helper(user_message, "kirkwood", 1, 0)
    ask_weather_helper(user_message, "aspen snowmass", 1, 1)
    ask_weather_helper(user_message, "crystal mountain", 1, 2)
    ask_weather_helper(user_message, "gore mountain", 1, 3)
    ask_weather_helper(user_message, "heavenly", 1, 4)

    ask_weather_helper(user_message, "kirkwood", 2, 0)
    ask_weather_helper(user_message, "aspen snowmass", 2, 1)
    ask_weather_helper(user_message, "crystal mountain", 2, 2)
    ask_weather_helper(user_message, "gore mountain", 2, 3)
    ask_weather_helper(user_message, "heavenly", 2, 4)

    ask_weather_helper(user_message, "kirkwood", 3, 0)
    ask_weather_helper(user_message, "aspen snowmass", 3, 1)
    ask_weather_helper(user_message, "crystal mountain", 3, 2)
    ask_weather_helper(user_message, "gore mountain", 3, 3)
    ask_weather_helper(user_message, "heavenly", 3, 4)

    ask_weather_helper(user_message, "kirkwood", 4, 0)
    ask_weather_helper(user_message, "aspen snowmass", 4, 1)
    ask_weather_helper(user_message, "crystal mountain", 4, 2)
    ask_weather_helper(user_message, "gore mountain", 4, 3)
    ask_weather_helper(user_message, "heavenly", 4, 4)

    ask_weather_helper(user_message, "kirkwood", 5, 0)
    ask_weather_helper(user_message, "aspen snowmass", 5, 1)
    ask_weather_helper(user_message, "crystal mountain", 5, 2)
    ask_weather_helper(user_message, "gore mountain", 5, 3)
    ask_weather_helper(user_message, "heavenly", 5, 4)

    return "Sorry, I don't understand",

"""
    :user_message: the user's input
    :resort_name: the name of a resort
    :after_days: the number of days after today
    :index: the list index of each resort in Resorts
"""
def ask_weather_helper(user_message, resort_name, after_days, index):
    if user_message in ("I wanna go to {0} on {1}".format(resort_name, after_days),
                        "I wanna go to {0} after one day".format(resort_name),
                        "I wanna go to {0} tomorrow".format(resort_name),):
        head = "Okay, here's the forecast weather in {0}:".format(resort_name)
        info = Resorts[index].weather[after_days].__str__()
        tail = "Do you have any other questions?"
        return head + "\n" * 2 + info, tail

# search pattern: "factor" in "resort" on "date"
def search_info(user_message, factor_name, resort_name, after_days, index):
    if user_message in ("{0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "can you tell me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "show me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "what is the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "what is the {0} in {1}"
                                .format(factor_name, resort_name)):
        head = "Okay, here's what I've found:"
        info = ""

        # search objects in class weather

        if factor_name == "weather":
            # return forecast weather in a week
            if after_days == 8:
                for i in range(after_days - 1):
                    info += Resorts[index].weather[i].__str__() + "\n"
            # return forecast weather in a single day
            else:
                info = Resorts[index].weather[after_days].__str__()
        elif factor_name == "snowfall":
            if after_days == 8:
                for i in range(after_days - 1):
                    info += Resorts[index].weather[i].print_snowfall() + "\n"
            else:
                info = Resorts[index].weather[after_days].snow_in
        elif factor_name == "rainfall":
            if after_days == 8:
                for i in range(after_days - 1):
                    info += Resorts[index].weather[i].print_rainfall() + "\n"
            else:
                info = Resorts[index].weather[after_days].rain_in
        elif factor_name == "visibility":
            if after_days == 8:
                for i in range(after_days - 1):
                    info += Resorts[index].weather[i].print_visibility() + "\n"
            else:
                info = Resorts[index].weather[after_days].vis_mi
        elif factor_name == "temperature":
            if after_days == 8:
                for i in range(after_days - 1):
                    info += Resorts[index].weather[i].print_temperature() + "\n"
            else:
                info = Resorts[index].weather[after_days].temp_f

        # search objects in class operation
        elif factor_name == "ticket price":
            info = Resorts[index].operation.print_price()




    # 看能否返回给定日期以后的天气
    if user_message in ("I wanna go to {0} on {1}".format(resort_name, after_days),
                        "I wanna go to {0} after one day".format(resort_name),
                        "I wanna go to {0} tomorrow".format(resort_name),):
        head = "Okay, here's the forecast weather in {0}:".format(resort_name)
        info = Resorts[index].weather[after_days].__str__()
        tail = "Do you have any other questions?"
        return head + "\n" * 2 + info, tail




def after_today(num):
    today = date.today()
    future = today + timedelta(days=num)
    future_str = future.strftime("/%m/%d/%Y")
    return future_str
