'''
Project 6
Problem Statement:
The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

Question:
What is the process to extract data from the wikipedia website using Beautiful Soup in Python? Specifically,
 how can we extract the rank, name of the company, Industry, Revenue, Revenue growth, Headquarters for the top US companies by Revenue?
'''


#pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

headers = {
    "User-Agent": "Mozilla/5.0"
}
# Send request
response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the main table with details
#table = soup.find("table", class_="wikitable sortable")

# Find all wikitable tables
tables = soup.find_all("table", class_="wikitable")
print("Total tables found:", len(tables))
#print(soup.prettify()[:1000])
# Select the correct table
table = tables[0]

# Extract table rows
rows = table.find_all("tr")

# Lists to store data
data = []

# Loop through rows (skip header)
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 6:
        rank = cols[0].text.strip()
        companyName = cols[1].text.strip()
        industry = cols[2].text.strip()
        revenue = cols[3].text.strip()
        revenue_growth = cols[4].text.strip()
        headquarters = cols[5].text.strip()

        data.append([
            rank,
            companyName,
            industry,
            revenue,
            revenue_growth,
            headquarters
        ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Rank",
        "Company Name",
        "Industry",
        "Revenue",
        "Revenue Growth",
        "Headquarters"
    ]
)

# Display first few rows
print(df.head(10))
