from database import Resorts
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.skiresort.info/ski-resort/heavenly/')

soup = BeautifulSoup(response.text, 'html.parser')


