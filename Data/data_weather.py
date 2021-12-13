import requests
from datetime import date, timedelta


'''
***************************
    GET WEATHER DATA
***************************
'''

APP_ID = "39eba088"
APP_KEY = "fe507959f9cfd3f54af726fc36e63d9a"


# takes in a Resorts list and set their matching ids
def set_resort_id(Resorts):
    resort_ids = ["209004", "303020", "414002", "518005", "916004"]
    for i in range(len(Resorts)):
        Resorts[i].set_id(resort_ids[i])


# get JSON object
def request(r_id, app_id, app_key):
    return requests.get("https://api.weatherunlocked.com/api/resortforecast/"
                        "{0}?app_id={1}&app_key={2}"
                        .format(r_id, app_id, app_key))


# take in a Resorts list and get raw weather data of each Resort
def get_raw_weather(Resorts):
    raw_data = []
    for resort in Resorts:
        raw_data.append(request(resort.resort_id, APP_ID, APP_KEY).json())
    return raw_data


# return the list of incoming 7 days' dates based on current dates
def get_forecast_week():
    today = date.today()
    seven_days = []
    for i in range(1, 8):
        next_day = today + timedelta(days=i)
        seven_days.append(next_day.strftime("%d/%m/%Y"))
    return seven_days


'''
    :Resorts: the list of Resorts objects
'''
#  set core weather data into Resorts objects
def set_weather(Resorts):
    set_resort_id(Resorts)
    raw_data = get_raw_weather(Resorts)
    seven_days = get_forecast_week()
    set_weather_helper2(Resorts, raw_data, seven_days)


'''
    :Resorts: the list of Resorts objects
    :raw_data: the list of full weather data without processed
    :seven_days: the list of the forecasting week from now
'''
# extract the core weather data from raw data on a future week, and populate them into all resort objects
def set_weather_helper2(Resorts, raw_data, seven_days):
    for d in range(len(seven_days)):
        for r in range(len(Resorts)):
            set_weather_helper1(seven_days[d], raw_data[r], Resorts[r], d)


'''
    :forecast_date: the date of which weather to be forecasted
    :raw_data: the full weather data of each Resort without processed
    :resort: the particular resort which weather to be forecasted
    :kth_day: the Kth day need to be forecasted from now
'''
# abstract real-time core weather data on a single day and update in a single Resort object
def set_weather_helper1(forecast_date, each_raw_data, each_resort, kth_day):
    for day in each_raw_data["forecast"]:
        if forecast_date in day.values():
            # choose date between 10am - 12am
            if "10:00" in day.values() \
                    or "11:00" in day.values() \
                    or "12:00" in day.values():
                # update core weather info on Kth day
                each_resort.weather[kth_day].set_weather(
                    day["date"],
                    day["base"]["wx_desc"],
                    day["snow_in"],
                    day["rain_in"],
                    day["vis_mi"],
                    day["slp_in"],
                    day["base"]["temp_f"],
                    day["base"]["windspd_mph"]
                )
