import requests
from bs4 import BeautifulSoup
import csv
import send_mail
from datetime import date

today = str(date.today()) + '.csv'
# URL of the Yahoo Finance page
urls = ["https://finance.yahoo.com/quote/AMZN/" , 'https://finance.yahoo.com/quote/GOOG/']

# Creating a csv file
csv_file = open(today , "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name' , 'Current Price' , 'Previous Close' , 'Open' , 'Bid' , 'Ask' , "Day's Range" , '52 Week Range' , 'Volume' , 'Average Volume', 'Market Cap(Intraday)' , 'Beta (5Y Monthly)', 'PE Ratio (TTM)','EPS (TTM)' ,'Earnings Date','Forward Dividend & Yield' , 'Ex-Dividend Date' , '1y Target Est'])

# Mimic a browser with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

for url in urls :
    stock = []
    
    # Fetch the page content
    response = requests.get(url, headers=headers)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")

    # Locate the section containing the <h1> tag
    section = soup.find("section", class_="container yf-xxbei9 paddingRight")
    h1_tag = section.find("h1", class_="yf-xxbei9").get_text()
    stock.append(h1_tag)
    
    # Locate the div tag for money
    current_price = soup.find("div" , class_= 'container yf-aay0dk')
    span_tag = current_price.find("span").get_text()
    stock.append(span_tag)
    
    # Extracting data from the list
    div_container = soup.find('div' , class_ = "container yf-dudngy").find_all("li")
    for li in div_container:
        spans = li.find_all("span")
        if len(spans) >= 2:  # Ensure there are at least two <span> elements
            second_span_text = spans[1].get_text(strip=True)  # Text from the second <span>
            stock.append(second_span_text)
    csv_writer.writerow(stock)
csv_file.close()
send_mail.send(filename = today)