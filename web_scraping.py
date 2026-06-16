import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Check status
if response.status_code == 200:
    print("Website accessed successfully!")
else:
    print("Failed to access website.")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Lists to store data
titles = []
prices = []
ratings = []

# Extract data
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    rating = book.find("p", class_="star-rating")
    rating = rating["class"][1]

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

# Display extracted data
print("\nExtracted Data:\n")
print(df)

# Save CSV in Downloads folder
output_file = r"C:\Users\Vignesh\Downloads\books_dataset.csv"

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("\nDataset saved successfully!")
print("File Location:", output_file)

# Project Summary
print("\nProject Summary")
print("----------------")
print("Total Books Scraped:", len(df))
print("Columns:", list(df.columns))