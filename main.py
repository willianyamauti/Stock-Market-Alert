from stock import Stock
from news import News
from twillo_sms import Twillo

# the Alpha Exchange API has a 5 api call limit and 500 call per day, so tou are limited to 5 stocks per run
# and 100 runs per day

stocks_dict = [
    {'symbol': "TSLA", 'Company Name': "Tesla"},
    {'ACT Symbol': "IBM", 'Company Name': "IBM"},
    {'ACT Symbol': "AAPL", 'Company Name': "Apple"},
]


stock = Stock()
news = News()
twillo = Twillo()

for company in stocks_dict:
    symbol, name = company.values()
    stock.symbol = symbol
    stock.name = name

    try:
        do_fetch_news = stock.analise_stock_prices()
        if do_fetch_news:
            news.parameters['qInTitle'] = name
            news.initialize_news()
            for articles in news.headlines:
                msg = (f"{stock.symbol}: {stock.up_down} {stock.price_change}%\n"
                       f"{articles}")
                print(msg)
                twillo.send_msg(msg)

    except Exception as err:
        print("The API call limit has probably been exceeded, try again at a latter time!")
        break
