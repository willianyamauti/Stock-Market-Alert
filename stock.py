import requests
import pandas as pd

AA_KEY = ''
AA_ENDPOINT = 'https://www.alphavantage.co/query'

# Change the amount of days to fetch data from
TIME_INTERVAL = 2
DESIRED_PERCENTAGE = 0.01


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

class Stock:
    parameters = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': '',
        'apikey': AA_KEY,
    }

    def __init__(self):
        self.data = ''
        self.closing_prices = ''
        self.symbol = ''
        self.up_down = ''
        self.price_change = 0

    def get_stock_data(self):
        self.parameters['symbol'] = self.symbol
        response = requests.get(AA_ENDPOINT, self.parameters)
        response.raise_for_status()
        stock_data = response.json()["Time Series (Daily)"]
        return stock_data
            

    def analise_stock_prices(self):
        self.initialize_stock()
        stock_prices_series = pd.Series(self.closing_prices)
        price_diference = (stock_prices_series.pct_change())
        # access the percentage diference in the pd series, if needed can be further changed to address more data
        self.price_change = round(abs(price_diference[1])*100)
        if price_diference[1] >= DESIRED_PERCENTAGE:
            self.up_down = '▲'
            return True
        elif price_diference[1] <= DESIRED_PERCENTAGE * -1:
            self.up_down = '▼'
            return True
        else:
            return False

    def fetch_closing_prices(self):
        data_list = [value for key, value in self.data.items()]
        prices_data = []
        for day in range(TIME_INTERVAL):
            prices_data.append(float(data_list[day]["4. close"]))
        return prices_data

    def initialize_stock(self):
        self.data = self.get_stock_data()
        self.closing_prices = self.fetch_closing_prices()
