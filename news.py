import requests

query = input("What are type of news are you interested in today? ")
api = "2cfea9b9f2544b74aa75a2e98a6da863"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-10&sortBy=publishedAt&apiKey={api}"

print(url)
c = requests.get(url)

data = c.json()
articles = data["articles"]
for index, article in enumerate (articles):
    print(index + 1, article["title"], article["url"])
    print("\n***************************************************\n")



