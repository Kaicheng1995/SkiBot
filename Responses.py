from database import *
from datetime import date, datetime

# get real time Resorts data
Resorts = populate_data()

"""
    takes in user message and return a tuple of responses
"""


def sample_responses(input_text):
    user_message = str(input_text).lower()

    # 1/greeting
    if user_message in ("hello", "hi", "hola", "hey",):
        return "Hey! What can I do to help you today?",

    # 2/ask recommendation
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

    # 3/ask resort
    if user_message in ("kirkwood",
                        "i want to go to kirkwood",
                        "i prefer kirkwood",):
        head = "Here are some operating information of the kirkwood resort:"
        info = print_operation(Resorts[0])
        tail = "When do you plan to go?"
        return head + "\n" * 2 + info, tail

    # 4/ask plan (on a single day)


    # return sorry if it can't match user message
    return "Sorry, I don't understand." + "\n" +\
           'Type "/help" to get instructions',


"""
    :user_message: the user's input
    :resort_name: the name of a resort
    :after_days: the number of days after today
    :index: the list index of each resort in Resorts
"""


def show_weather(user_message, resort_name, after_days, index):
    if user_message in ("I wanna go to {0} on {1}".format(resort_name, after_days),
                        "I wanna go to {0} after one day".format(resort_name),
                        "I wanna go to {0} tomorrow".format(resort_name),):
        head = "Okay, here's the forecast weather in {0}:".format(resort_name)
        info = Resorts[index].weather[after_days].__str__()
        tail = "Do you have any other questions?"
        return head + "\n" * 2 + info, tail


"""
    search required data and response to user
    search pattern <1>: "factor" in "resort" on "date"
    search pattern <2>: "factor" in "resort"
    
    :user_message: the user's input
    :factor_name: the thing that user wants to know
    :resort_name: the name of a resort
    :after_days: the number of days after today
    :index: the list index of each resort in Resorts
"""
def search_info(user_message, factor_name, resort_name, after_days, index):
    if user_message in ("{0} in {1} on {2}"  # with specific day
                                .format(factor_name, resort_name, after_days),
                        "can you tell me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "show me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "what is the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_days),
                        "{0} in {1}"  # without specific day
                                .format(factor_name, resort_name),
                        "can you tell me the {0} in {1}"
                                .format(factor_name, resort_name),
                        "show me the {0} in {1}"
                                .format(factor_name, resort_name),
                        "what is the {0} in {1}"
                                .format(factor_name, resort_name)):
        head = "Okay, here's what I've found:"
        info = ""
        tail = "Do you have any other questions?"

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
        elif factor_name == "open date":
            info = Resorts[index].operation.print_open()
        elif factor_name == "close date":
            info = Resorts[index].operation.print_close()
        elif factor_name == "number of lifts":
            info = Resorts[index].operation.lifts
        elif factor_name == "rating":
            info = Resorts[index].operation.rating

        # return search results
        return head + "\n" * 2 + info, tail


# helper function, used to return the string of future dates
def after_today(num):
    today = date.today()
    future = today + timedelta(days=num)
    future_str = future.strftime("/%m/%d/%Y")
    return future_str
