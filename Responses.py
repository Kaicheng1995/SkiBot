import sys
sys.path.append('/Users/kai/PycharmProjects/pythonProject1/SkiBot/Data')
from database import *
from datetime import date, timedelta

# get real time Resorts data (not real real-time)
Resorts = populate_data()

# however, if we want real real-time, we should update data each time user query anything
# def get_real_time_resorts():
#     return populate_data()


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
                        "go skiing",
                        "i want to go skiing",
                        "please show me some ski resorts",
                        "can you recommend to me some ski resorts?",
                        "can you tell me some recently opened ski resorts?",):
        head = "Okay. Five ski resorts are currently or about to open:"
        info = print_resorts(Resorts)
        tail = "Where do you want to go?"
        return head + "\n" * 2 + info, tail

    # 3/ask resort
    head, tail = show_resort(user_message, "kirkwood", 0)
    if head is not None and tail is not None:
        return head, tail
    head, tail = show_resort(user_message, "aspen snowmass", 0)
    if head is not None and tail is not None:
        return head, tail
    head, tail = show_resort(user_message, "crystal mountain", 0)
    if head is not None and tail is not None:
        return head, tail
    head, tail = show_resort(user_message, "gore mountain", 0)
    if head is not None and tail is not None:
        return head, tail
    head, tail = show_resort(user_message, "heavenly", 0)
    if head is not None and tail is not None:
        return head, tail

    # 4/ask plan (on a single day)
    for after_days in range(1, 6):
        head, tail = show_weather(user_message, "kirkwood", after_days, 0)
        if head is not None and tail is not None:
            return head, tail
        head, tail = show_weather(user_message, "aspen snowmass", after_days, 1)
        if head is not None and tail is not None:
            return head, tail
        head, tail = show_weather(user_message, "crystal mountain", after_days, 2)
        if head is not None and tail is not None:
            return head, tail
        head, tail = show_weather(user_message, "gore mountain", after_days, 3)
        if head is not None and tail is not None:
            return head, tail
        head, tail = show_weather(user_message, "heavenly", after_days, 4)
        if head is not None and tail is not None:
            return head, tail

    # 5/search info (any day, unlimited to a single day)
    factors = ["weather", "snowfall", "rainfall", "visibility", "temperature",
               "ticket price", "open date", "close date", "number of lifts", "rating"]
    for after_days in range(1, 6):
        for factor in factors:
            head, tail = search_info(user_message, factor, "kirkwood", after_days, 0)
            if head is not None and tail is not None:
                return head, tail
            head, tail = search_info(user_message, factor, "aspen snowmass", after_days, 1)
            if head is not None and tail is not None:
                return head, tail
            head, tail = search_info(user_message, factor, "crystal mountain", after_days, 2)
            if head is not None and tail is not None:
                return head, tail
            head, tail = search_info(user_message, factor, "gore mountain", after_days, 3)
            if head is not None and tail is not None:
                return head, tail
            head, tail = search_info(user_message, factor, "heavenly", after_days, 4)
            if head is not None and tail is not None:
                return head, tail

    # 6/exit
    if user_message in ("bye", "goodbye",):
        tail = "Have a nice day!"
        return tail,

    # 7/return sorry if it can't match user message
    return "Sorry, I don't understand." + "\n" + \
           'Type or click /help to get instructions',


# helper functions:
# 1/ show_resort: print resort's operating informaton
# 2/ show_weather: print weather information
# 3/ search_info: print any information
# 4/ after_today: calculate the date after some days
"""
    :user_message: the user's input
    :resort_name: the name of a resort
    :index: the list index of each resort in Resorts
"""


def show_resort(user_message, resort_name, index):
    if user_message in ("{0}".format(resort_name),
                        "i want to go to {0}".format(resort_name),
                        "i prefer {0}".format(resort_name),):
        head = "Here are some operating information of the {0} resort:".format(resort_name)
        info = print_operation(Resorts[index])
        tail = "When do you plan to go?"
        return head + "\n" * 2 + info, tail
    # if don't match anything, return two None
    return None, None


"""
    :user_message: the user's input
    :resort_name: the name of a resort
    :after_days: the number of days after today
    :index: the list index of each resort in Resorts
"""


def show_weather(user_message, resort_name, after_days, index):
    if user_message in ("i wanna go to {0} on {1}"
                                .format(resort_name, after_today(after_days)),
                        "i wanna go to {0} after {1} days"
                                .format(resort_name, after_days),
                        "i wanna go to {0} after {1} day"
                                .format(resort_name, after_days)):
        head = "Okay, here's the forecast weather on that date:".format(resort_name)
        info = Resorts[index].weather[after_days - 1].__str__()
        tail = "Do you have any other questions?"
        return head + "\n" * 2 + info, tail
    # if don't match anything, return two None
    return None, None


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
                                .format(factor_name, resort_name, after_today(after_days)),
                        "can you tell me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_today(after_days)),
                        "show me the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_today(after_days)),
                        "what is the {0} in {1} on {2}"
                                .format(factor_name, resort_name, after_today(after_days)),
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
            # return forecast weather in a week if no date specified
            if user_message[-13:-11] != "on":
                for i in range(5):
                    info += Resorts[index].weather[i].__str__() + "\n" + "\n"
            # return forecast weather in a single day
            else:
                info = Resorts[index].weather[after_days - 1].__str__()
        elif factor_name == "snowfall":
            if user_message[-13:-11] != "on":
                for i in range(5):
                    info += Resorts[index].weather[i].print_snowfall() + "\n" + "\n"
            else:
                info = str(Resorts[index].weather[after_days - 1].snow_in) + "(inch)"
        elif factor_name == "rainfall":
            if user_message[-13:-11] != "on":
                for i in range(5):
                    info += Resorts[index].weather[i].print_rainfall() + "\n" + "\n"
            else:
                info = str(Resorts[index].weather[after_days - 1].rain_in) + "(inch)"
        elif factor_name == "visibility":
            if user_message[-13:-11] != "on":
                for i in range(5):
                    info += Resorts[index].weather[i].print_visibility() + "\n" + "\n"
            else:
                info = str(Resorts[index].weather[after_days - 1].vis_mi) + "(inch)"
        elif factor_name == "temperature":
            if user_message[-13:-11] != "on":
                for i in range(5):
                    info += Resorts[index].weather[i].print_temperature() + "\n" + "\n"
            else:
                info = str(Resorts[index].weather[after_days - 1].temp_f) + "(F)"

        # search objects in class operation
        elif factor_name == "ticket price":
            info = Resorts[index].operation.print_price()
        elif factor_name == "open date":
            info = Resorts[index].operation.print_open()
        elif factor_name == "close date":
            info = Resorts[index].operation.print_close()
        elif factor_name == "number of lifts":
            info = str(Resorts[index].operation.lifts)
        elif factor_name == "rating":
            info = Resorts[index].operation.rating

        # return search results
        return head + "\n" * 2 + info, tail
    # if don't match anything, return two None
    return None, None


# helper function, used to return the string of future dates
def after_today(num):
    today = date.today()
    future = today + timedelta(days=num)
    future_str = future.strftime("%m/%d/%Y")
    return future_str
