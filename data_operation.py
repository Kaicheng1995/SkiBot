from main import Resorts
from urllib.request import urlopen
from dateutil.parser import parse
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


# the suffix of each resorts' url
url_suffix = ["kirkwood", "aspen-mountain", "crystal-mountain-wa",
              "gore-mountain", "heavenly"]
# set url and html used for web scraping
for i in range(len(Resorts)):
    url = "https://www.skiresort.info/ski-resort/{0}/".format(url_suffix[i])
    Resorts[i].operation.set_source(url, get_html(url))

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

def
