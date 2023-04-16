import telepot 
import requests 
from datetime import datetime
from timeloop import Timeloop
from datetime import timedelta

def getStockData(ticker):
    base_url = "https://financialmodelingprep.com/api/v3/quote/"
    key = "2aaa764e5195106c2970a9877aaa898a"
    full_url = base_url + ticker + "?apikey=" + key
    r = requests.get(full_url)
    stock_data= r.json()
    return stock_data

real_time_data = getStockData('AMZN')