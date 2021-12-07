from resort import Resort
import requests
import json

APP_ID = "39eba088"
APP_KEY = "fe507959f9cfd3f54af726fc36e63d9a"

# create 5 Resort objects
kirkwood = Resort("Kirkwood", "209004")
aspen = Resort("Aspen Snowmass", "303020")
crystal = Resort("Crystal Mountain", "414002")
gore = Resort("Gore Mountain", "518005")
heavenly = Resort("Heavenly", "916004")
# combine all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]


# get JSON object
def request(r_id, app_id, app_key):
    return requests.get("https://api.weatherunlocked.com/api/resortforecast/"
                        "{0}?app_id={1}&app_key={2}"
                        .format(r_id, app_id, app_key))


# get raw weather data
Raw_Data = []
for resort in Resorts:
    Raw_Data.append(request(resort.resort_id, APP_ID, APP_KEY).json())


#





# take a raw data formatted in dict and return the core data
# update the "weather" template in real time
def set_weather(raw_data, resort):
    for day in raw_data["forecast"]:
        if "07/12/2021" in day.values():
            if "10:00" in day.values() \
                    or "11:00" in day.values()\
                    or "12:00" in day.values():
                for key in resort.weather:
                    if key in day:
                        resort.weather[key] = day[key]
                    else:
                        resort.weather[key] = day["base"][key]


# populate the core weather data into resort object
for i in range(5):
    set_weather(Raw_Data[i], Resorts[i])
