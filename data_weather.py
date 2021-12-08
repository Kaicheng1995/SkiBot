from main import Resorts
import requests
from datetime import date, timedelta


'''
***************************
    GET WEATHER DATA
***************************
'''

APP_ID = "39eba088"
APP_KEY = "fe507959f9cfd3f54af726fc36e63d9a"

# set resort id from api
resort_ids = ["209004", "303020", "414002", "518005", "916004"]
for i in range(len(Resorts)):
    Resorts[i].set_id(resort_ids[i])

# get JSON object
def request(r_id, app_id, app_key):
    return requests.get("https://api.weatherunlocked.com/api/resortforecast/"
                        "{0}?app_id={1}&app_key={2}"
                        .format(r_id, app_id, app_key))


# get raw weather data
Raw_Data = []
for resort in Resorts:
    Raw_Data.append(request(resort.resort_id, APP_ID, APP_KEY).json())

# get current date and incoming 7 days' dates
today = date.today()
Seven_Days = []
for i in range(1, 8):
    next_day = today + timedelta(days=i)
    Seven_Days.append(next_day.strftime("%d/%m/%Y"))
print(Seven_Days)


# populate the core weather data into all resort objects
def set_weather():
    for d in range(len(Seven_Days)):
        for r in range(len(Resorts)):
            set_weather_helper(Seven_Days[d], Raw_Data[r], Resorts[r], d)


'''
@forecast_date: the date of which weather to be forecasted
@raw_data: the full weather data without processed
@resort: the particular resort which weather to be forecasted
@kth_day: the Kth day need to be forecasted from now
'''


# abstract real-time core weather data and update in objects
def set_weather_helper(forecast_date, raw_data, each_resort, kth_day):
    for day in raw_data["forecast"]:
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


# populate the core weather data into resort object
set_weather()
