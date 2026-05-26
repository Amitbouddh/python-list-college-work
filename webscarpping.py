import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print("Total books found:", len(books))

if len(books) > 0:
    print(books[0])

data = []

for book in books:
    title = book.find("h3").find("a").get("title")
    price = book.find("p", class_="price_color").text

    print(title, price)

    data.append({
        "title": title,
        "price": price
    })

df = pd.DataFrame(data)

print(df)