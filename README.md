# Stock-Market-Alert

A python script that sends sms with news pieces if a choosen stock has recived a percentual change of your choice.<br><br>
To use the script you need a twillo account and api keys, a Alpha advantage api key and a News Api key, for now the script has  limitations : 5 stock names per run of the script and a maximum of 100 runs a day, so you can check 500 stocks at the moment. This limitations is a result of using free API keys, been easily fixed using the paid ones.

## USAGE
Replace all the keys and phone number in the files stock.py(Alpha Advantage key), news.py(News Api keys), and twillo_sms.py(Twillo keys and phone number), the stocks must be manually inserted in the main.py for now, in future updates reading this files from a json is a must.

### API KEYS
News API - https://newsapi.org/account<br>
Alpha Advantage - https://www.alphavantage.co/#about<br>
Twillio - https://www.twilio.com/<br>

#### MODULES USED IN THIS SCRIPT
- pandas
- requests


