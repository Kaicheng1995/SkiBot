# SkiBot

<!-- ABOUT THE PROJECT -->
## About The Project

For snowboarders, we always hope to know some data about ski resorts, such as the amount of snowfall, the opening date, the ticket prices.
For our convenience, I created a chatbot named **`SkiBot`** for querying those data with user messages in real-time. As you can see as follows:

<p align="middle">
  <img src="https://github.com/Kaicheng1995/SkiBot/blob/main/Note/demo2.png" width="350">
  <img src="https://github.com/Kaicheng1995/SkiBot/blob/main/Note/demo1.png" width="350"> 
</p>

Here's the functionality that SkiBot has:
* Query the real-time forecast weather data in a particular ski resort on a particular date. The forecast data supports the future five days from now on. The weather feature includes:
```
* weather - (desciption)
* snowfall - (inch)
* rainfall - (inch)
* visibility - (mile)
* Humidity Level - (%)
* Temperature - (F)
* Wind Speed - (mph)
```
* Quering the real-time operating data in a particular ski resort. The operating feature includes: 
```
* status - (currently open / closed)
* open date - (open date)
* close date - (closed date)
* number of lifts - (number of lifts)
* ticket price - (including adult, youth and child prices)
* rating - (the rating of the resort)
* location
```     



### Built With

* [Telegram Bot API](https://core.telegram.org/bots/api)
* [Weather Unlocked API](https://developer.weatherunlocked.com/documentation/skiresort)
* [Python Request Library](https://docs.python-requests.org/en/latest/)
* [Python Datetime Library](https://docs.python.org/3/library/datetime.html)
* [Python Urllib.request Library](https://docs.python.org/3/library/urllib.request.html)
* [Python Dateutil.parser Library](https://dateutil.readthedocs.io/en/stable/parser.html)
* [Python Web Scraping](https://realpython.com/python-web-scraping-practical-introduction)



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
**`Python @3.10`** **`requests`** **`telegram bot api`** **`urllib`** **`dateutil`**
```
pip install requests
pip install python-telegram-bot
pip install urllib3
pip install dateutils
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/Kaicheng1995/SkiBot
```
2. Run the program
```
python main.py
```
3. Open SkiBot
```
open Telegram App and search the account "@proj_skibot", add it
```
4. Start to talk
```
type "/help" to get instructions and start to talk
```



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [SkiResort.info](https://www.skiresort.info/)
* [Python Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)
* [Python API Tutorial](https://www.dataquest.io/blog/python-api-tutorial/)
