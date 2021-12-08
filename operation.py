class Operation:

    # initialize an empty object
    def __init__(self):
        # source for web scraping
        self.url = None
        self.html = None
        # the data collected from the url
        self.status = ""       # currently open / closed
        self.open_date = ""    # open date
        self.close_date = ""   # closed date
        self.lifts = 0         # number of lifts
        self.adult_price = 0   # lift tickets price - adult
        self.youth_price = 0   # lift tickets price - youth
        self.child_price = 0   # lift tickets price - child
        self.rating = ""       # rating score
        self.location = ""     # location

    # set the url and html used for web scraping
    def set_source(self, url, html):
        self.url = url
        self.html = html

    # set open and close dates
    def set_operating_dates(self, open, close):
        self.open_date = open
        self.close_date = close

    # set lifts and prices
    def set_lifts_tickets(self, lifts, adult_price,
                          youth_price, child_price):
        self.lifts = lifts
        self.adult_price = adult_price
        self.youth_price = youth_price
        self.child_price = child_price

