class Weather:

    # initialize an empty object
    def __init__(self):
        self.date = ""      # Date
        self.wx_desc = ""   # Weather Description
        self.snow_in = 0.0  # Snowfall (inches)
        self.rain_in = 0.0  # Rainfall (inches)
        self.vis_mi = 0.0   # Visibility (miles)
        self.slp_in = 0.0   # Humidity Level (%)
        self.temp_f = 0.0   # Temperature (F)
        self.windspd_mph = 0.0  # Wind Speed (mph)

    # set value to weather object
    def set_weather(self,
                    date,
                    wx_desc,
                    snow_in,
                    rain_in,
                    vis_mi,
                    slp_in,
                    temp_f,
                    windspd_mph):
        self.date = date
        self.wx_desc = wx_desc
        self.snow_in = snow_in
        self.rain_in = rain_in
        self.vis_mi = vis_mi
        self.slp_in = slp_in
        self.temp_f = temp_f
        self.windspd_mph = windspd_mph

    def __str__(self):
        out = "Date: " + str(self.date) + "\n" + \
              "Weather: " + str(self.wx_desc) + "\n" + \
              "Snowfall (inch): " + str(self.snow_in) + "\n" + \
              "Rainfall (inch): " + str(self.rain_in) + "\n" + \
              "Visibility (inch): " + str(self.vis_mi) + "\n" + \
              "Humidity Level (miles): " + str(self.slp_in) + "\n" + \
              "Temperature (F): " + str(self.temp_f) + "\n" + \
              "Wind Speed: (mhp): " + str(self.windspd_mph)
        return out

    def print_snowfall(self):
        out = "Date: " + str(self.date) + "\n" + \
              "Snowfall (inch): " + str(self.snow_in)
        return out

    def print_rainfall(self):
        out = "Date: " + str(self.date) + "\n" + \
              "Rainfall (inch): " + str(self.rain_in)
        return out

    def print_visibility(self):
        out = "Date: " + str(self.date) + "\n" + \
              "Visibility (inch): " + str(self.vis_mi)
        return out

    def print_temperature(self):
        out = "Date: " + str(self.date) + "\n" + \
              "Temperature (F): " + str(self.temp_f)
        return out
