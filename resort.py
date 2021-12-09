from operation import Operation
from weather import Weather

class Resort:
    # each resort shares the same api key
    APP_ID = "39eba088"
    APP_KEY = "fe507959f9cfd3f54af726fc36e63d9a"

    def __init__(self, name):
        self.name = name
        self.resort_id = None
        # self.rating = self.operation.rating
        # self.location = self.operation.location


        # operation info
        self.operation = Operation()

        # forecasted weather (7 days)
        self.weather = [Weather(), Weather(), Weather(),
                        Weather(), Weather(),
                        Weather(), Weather()]

        self.tickets = None
        self.hotels = None
        self.restaurants = None

    # set unique api resort id
    def set_id(self, resort_id):
        self.resort_id = resort_id

    # hotel
    def set_hotels(self, hotels):
        self.hotels = hotels

    # restaurants
    def set_restaurants(self, restaurants):
        self.restaurants = restaurants
