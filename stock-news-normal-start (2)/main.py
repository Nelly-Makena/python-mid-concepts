import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params= {
    "function" :"TIME_SERIES_WEEKLY",
    "symbol" : "TSLA",
    "apikey" : " JOOP5DD7CJ0UGLIF"

}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_params={
    "apiKey" : "0e1361db35bf4ddd99cef9eabd678815",
    "q": "COMPANY_NAME"
}



response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()

data =response.json()
print(data)
# Extract the weekly time series data
weekly_data = data["Weekly Time Series"]

# Get the closing prices for the last two days
closing_prices = [float(value["4. close"]) for (key, value) in sorted(weekly_data.items(), reverse=True)[:2]]

# Calculate the percentage change
percentage_change = ((closing_prices[0] - closing_prices[1]) / closing_prices[1]) * 100

# Check if the change is greater than 5%
if abs(percentage_change) > -5:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()

    news = response.json()
    #Extract articles from the response

    articles = data.get("articles", [])

    # Slice to get the first three articles
    first_three_articles = articles[:3]

    # Print or process the first three articles
    for index, article in enumerate(first_three_articles, start=1):
        print(f"Article {index}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("\n" + "-" * 50 + "\n")
else:
    print(f"Percentage change is {percentage_change:.2f}%, no significant movement.")


