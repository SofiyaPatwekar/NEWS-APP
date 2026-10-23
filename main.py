import requests

topic=input("What topic would you like to read today?")
api=""

url=f"https://newsapi.org/v2/everything?q={topic}&from=2026-09-23&sortBy=publishedAt&apiKey={api}"
print(url)
response=requests.get(url)
data=response.json()
for index,article in enumerate(data["articles"]):
    print(f"{index+1}- Title: {article["title"]}\nNews: {article["description"]}")
    print("***********************************************************")