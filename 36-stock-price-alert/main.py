"""Tesla Stock alert"""

import datetime
import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# api keys
ALPHAADVANTAGE_API_KEY = "SOME KEY"
NEWS_API = "SOME OTHER KEY"

# twillio account info
account_sid = "SOME SID"
auth_token = "SOME TOKEN"


# stock api params
alpha_advantage_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHAADVANTAGE_API_KEY,
}

# Get tesla stock info
response = requests.get(
    url="https://www.alphavantage.co/query", params=alpha_advantage_params
)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# get yesterday and 2 days before stock info
current_date = str(datetime.datetime.now() - datetime.timedelta(1)).split(" ")[0]
yesterday_date = str(datetime.datetime.now() - datetime.timedelta(2)).split(" ")[0]

# get the close price
current_date_close = float(data[current_date]["4. close"])
yesterday_date_close = float(data[yesterday_date]["4. close"])

difference = current_date_close - yesterday_date_close
difference_percent = (difference / current_date_close) * 100


if difference_percent > 2:
    newsapi = NewsApiClient(api_key=NEWS_API)

    sources = newsapi.get_sources()

    top_headlines = newsapi.get_top_headlines(q="Tesla")["articles"]

    titles = []
    descriptions = []
    for i in range(len(top_headlines)):
        titles.append(top_headlines[i]["title"])
        descriptions.append(top_headlines[i]["description"])

    news_list = list(zip(titles, descriptions))

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK}: 🔺{round(difference_percent,0)}\nHeadline: {news_list[0][0]}.\nBrief: {news_list[0][1]}",
        from_="+SOME NUMBER",
        to="+SOME NUMBER",
    )
    print(message.status)
