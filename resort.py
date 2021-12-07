from weather import Weather

class Resort:
    # each resort shares the same api key
    APP_ID = "39eba088"
    APP_KEY = "fe507959f9cfd3f54af726fc36e63d9a"

    def __init__(self, name, resort_id):
        self.name = name
        self.resort_id = resort_id
        self.location = ""
        self.rating = ""

        # forecasted weather (7 days)
        self.weather = [Weather(), Weather(), Weather(),
                        Weather(), Weather(),
                        Weather(), Weather()]

        self.tickets = None
        self.hotels = None
        self.restaurants = None


    # set location and rating
    def set_base(self, location, rating):
        self.location = location
        self.rating = rating

    # set weather
    def set_weather(self):
        seven_day = []
        for i in range(7):
            seven_day.append(one_day)
        self.weather = seven_day


    # tickets is a Python dictionary
    def set_tickets(self, tickets):
        self.tickets = tickets

    # hotel
    def set_hotels(self, hotels):
        self.hotels = hotels

    # restaurants
    def set_restaurants(self, restaurants):
        self.restaurants = restaurants
