class Operation:

    # initialize an empty object
    def __init__(self):
        # source for web scraping
        self.url = None
        self.html = None
        # the data collected from the url
        self.status = ""  # currently open / closed
        self.open_date = ""  # open date
        self.close_date = ""  # closed date
        self.lifts = 0  # number of lifts
        self.adult_price = 0  # lift tickets price - adult
        self.youth_price = 0  # lift tickets price - youth
        self.child_price = 0  # lift tickets price - child
        self.rating = ""  # rating score
        self.location = ""  # location

    # set the url and html used for web scraping
    def set_source(self, url, html):
        self.url = url
        self.html = html

    # set open and close dates
    def set_operating_dates(self, open, close):
        self.open_date = open
        self.close_date = close

    # set operating status
    def set_status(self, status):
        self.status = status

    # set lifts and prices
    def set_lifts_tickets(self, lifts, adult_price,
                          youth_price, child_price):
        self.lifts = lifts
        self.adult_price = adult_price
        self.youth_price = youth_price
        self.child_price = child_price

    # set rating and location
    def set_rating_location(self, rating, location):
        self.rating = rating
        self.location = location

    # print operating info
    def __str__(self):
        out = "Rating: " + str(self.rating) + "\n" + \
              "Status: " + str(self.status) + "\n" + \
              "Open Date: " + str(self.open_date)[3:6] \
              + str(self.open_date)[0:3] \
              + str(self.open_date)[6:] + "\n" + \
              "Close Date: " + str(self.close_date)[3:6] \
              + str(self.close_date)[0:3] \
              + str(self.close_date)[6:] + "\n" + \
              "Price for Adult: " + str(self.adult_price) + "\n" + \
              "Price for Youth: " + str(self.youth_price) + "\n" + \
              "Price for Child: " + str(self.child_price) + "\n" + \
              "Number of Lifts: " + str(self.lifts)
        return out

    def print_price(self):
        out = "Price for Adult: " + str(self.adult_price) + "\n" + \
              "Price for Youth: " + str(self.youth_price) + "\n" + \
              "Price for Child: " + str(self.child_price)
        return out
