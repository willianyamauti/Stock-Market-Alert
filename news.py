import requests
import datetime as dt
import html

NEWS_API = ''
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
# the number of news articles you want to fetch
NUMBER_OF_ARTICLES = 3


class News:
    parameters = {
        'qInTitle': '',
        'from': dt.datetime.utcnow().date(),
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': NEWS_API,
    }

    def __init__(self):
        self.data = ''
        self.headlines = ''

    def get_news_api_call(self):
        response = requests.get(NEWS_ENDPOINT, self.parameters)
        response.raise_for_status()
        news_data = response.json()['articles']
        return news_data

    def fetch_news(self):
        headlines = self.data[:NUMBER_OF_ARTICLES]
        return headlines

    def format_headline(self):
        raw_data = self.fetch_news()
        formatted_data = [f"Source: {data['source']['name']}.\n"
                          f"Headline: {data['title']}.\n"
                          f"Brief: {data['description']}.\n"
                          for data in raw_data]

        return formatted_data

    def display_news(self):
        for article in self.headlines:
            print(article)

    def initialize_news(self):
        self.data = self.get_news_api_call()
        self.headlines = self.format_headline()

