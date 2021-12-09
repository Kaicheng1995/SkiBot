from urllib.request import urlopen
from dateutil.parser import parse
from resort import Resort

from datetime import datetime
import re

"""
    takes an url and return html string
    :param url: the link used for web scraping
"""


def get_html(url):
    # pass url to open the web page, return an HTTPResponse object
    page = urlopen(url)

    # extract the HTML from the page
    # 1/ use HTTPResponse object’s .read() method, returns a sequence of bytes.
    # 2/ use .decode() to decode the bytes to a string using UTF-8:
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


"""
    takes the Resorts list and set each Resort's url and html
    :param Resorts: the Resorts list
"""


def set_url_and_html(Resorts):
    # the suffix of each resorts' url
    url_suffix = ["kirkwood", "aspen-mountain", "crystal-mountain-wa",
                  "gore-mountain", "heavenly"]
    # set url and html used for web scraping
    for i in range(len(Resorts)):
        url = "https://www.skiresort.info/ski-resort/{0}/".format(url_suffix[i])
        Resorts[i].operation.set_source(url, get_html(url))


"""
   ***************************
   SUMMARY: set operating data into Resort objects list
   
   1/ SET URL & HTML
   2/ SET OPEN & CLOSE DATES
   ***************************
"""


def set_operation(Resorts):
    set_url_and_html(Resorts)
    set_operating_dates(Resorts)


"""
   ***************************
   1/ GET OPEN & CLOSE DATES
   ***************************
"""
"""
    takes a resort html string and return operating dates
    :param html: the html string used for web scraping
"""


def get_operating_dates(html):
    # find string in html and return its index
    # find open_date
    open_index = html.find('<td id="selSeason">') + len('<td id="selSeason">') + 1
    open_index_end = open_index + 10
    open_date = html[open_index: open_index_end]
    # check no data available
    if not is_date(open_date):
        open_date = "Not Available"

    # find close_date
    close_index = open_index_end + 3
    close_index_end = close_index + 10
    close_date = html[close_index: close_index_end]
    if not is_date(close_date):
        close_date = "Not Available"

    # return operating dates
    return open_date, close_date


"""
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
"""


def is_date(string, fuzzy=False):
    try:
        # parse date string formats to a datetime object.
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False


"""
    Takes in the Resorts list and set open and close dates
    :param Resorts: the Resorts list
"""
def set_operating_dates(Resorts):
    # set open and close dates into objects
    for resort in Resorts:
        html = resort.operation.html
        open_date, close_date = get_operating_dates(html)
        resort.operation.set_operating_dates(open_date, close_date)
        print(resort.operation.open_date)


"""
   ***************************
   2/ GET LIFTS & PRICES
   ***************************
"""
"""
    takes a resort html string and return #lifts and prices
    :param html: the html string used for web scraping
"""
def get_lifts(html):
    # find number of lifts
    prefix = '<strong id="selLiftstot">Total:'
    start_index = html.find(prefix) + len(prefix) + 1
    end_index = start_index + 2
    lifts = html[start_index: end_index]
    # handle different number of digits
    if not lifts[-1:].isdigit():
        return int(lifts[:-1])
    return int(lifts)

def get_prices(html):
    # find prices - adults
    price_a = get_prices_helper(html, '<td id="selTicketA">')
    # find prices - youth
    price_y = get_prices_helper(html, '<td id="selTicketY">')
    # find prices - children
    price_c = get_prices_helper(html, '<td id="selTicketC">')
    return price_a, price_y, price_c

def get_prices_helper(html, prefix):
    start_index = html.find(prefix) + len(prefix)
    price = html[start_index: start_index + 7]
    if not price[-1:].isdigit():
        return price[:-1]
    return price


"""
    Takes in the Resorts list and set open and close dates
    :param Resorts: the Resorts list
"""
def set_lifts_and_prices(Resorts):
    # set number of lifts and prices into objects
    for resort in Resorts:
        html = resort.operation.html
        lifts = get_lifts(html)
        price_a, price_y, price_c = get_prices(html)
        resort.operation.set_lifts_tickets(lifts, price_a, price_y, price_c)
        print(resort.operation.adult_price)


# create 5 Resort objects
kirkwood = Resort("Kirkwood")
aspen = Resort("Aspen Snowmass")
crystal = Resort("Crystal Mountain")
gore = Resort("Gore Mountain")
heavenly = Resort("Heavenly")

# append all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]
set_url_and_html(Resorts)

set_lifts_and_prices(Resorts)
