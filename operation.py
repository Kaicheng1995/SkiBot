class Operation:

    # initialize an empty object
    def __init__(self):
        # source for web scraping
        self.url = None
        self.html = None
        # the data collected from the url
        self.status = ""
        self.open_date = ""
        self.close_date = ""
        self.lifts = 0
        self.adults_price = 0
        self.youth_price = 0
        self.child_price = 0
        self.rating = ""
        self.location = ""

    # set the url and html used for web scraping
    def set_source(self, url, html):
        self.url = url
        self.html = html

    # set open and close dates
    def set_operating_dates(self, open, close):
        self.open_date = open
        self.close_date = close
