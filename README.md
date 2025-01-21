# Stock Scraper and Email Notifier

This project scrapes stock data from Yahoo Finance and sends an automated email with the extracted data in a CSV file. It is implemented in Python using various libraries for web scraping, data storage, and email handling.

## Objective

1. Scrape real-time stock data from Yahoo Finance.
2. Store the extracted data in a CSV file.
3. Send an automated email containing the CSV file as an attachment.

## Packages Used

### Required Packages and Their Purpose:
- **`requests`**: To send HTTP requests and fetch HTML content from Yahoo Finance.
- **`BeautifulSoup`**: To parse and extract data from the HTML content.
- **`csv`**: To create and write stock data into a CSV file.
- **`smtplib`**: To handle the email sending process.
- **`email.mime`**: To format and attach files and body text in the email.
- **`datetime`**: To generate a dynamic file name based on the current date.

### Additional Information:
- **Headers**: A `User-Agent` is used to mimic browser requests to avoid being blocked by Yahoo Finance.
- **Authentication**: The email requires an authentication code for secure login.

---

## How to Use

### Step 1: Install the Required Libraries
To install the required packages, run:
```bash
pip install requests beautifulsoup4
```

### Step 2: Setup Email Authentication
- Open the `send_mail.py` file.
- Update the following placeholders:
  - `from_add`: The sender's email address.
  - `to_add`: The recipient's email address.
  - Add your email's **App Password** for secure authentication:
    ```python
    server.login(from_add, '<your_app_password>')
    ```

#### Generate an App Password for Gmail
1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification** if not already enabled.
3. Generate an **App Password** for the email application and use it in the `server.login()` function.

### Step 3: Customize the URLs
Update the `urls` list in the main script with the stock URLs you want to scrape:
```python
urls = ["https://finance.yahoo.com/quote/AMZN/", "https://finance.yahoo.com/quote/GOOG/"]
```

### Step 4: Run the Code
Execute the script:
```bash
python main_script.py
```

### Expected Data Fields in the CSV File
The script extracts the following data points for each stock:
- Stock Name
- Current Price
- Previous Close
- Open
- Bid
- Ask
- Day's Range
- 52-Week Range
- Volume
- Average Volume
- Market Cap (Intraday)
- Beta (5Y Monthly)
- PE Ratio (TTM)
- EPS (TTM)
- Earnings Date
- Forward Dividend & Yield
- Ex-Dividend Date
- 1-Year Target Estimate

### Sample Output
#### CSV File (`2024-01-21.csv`)
| Stock Name | Current Price | Previous Close | Open | Bid | ... |
|------------|---------------|----------------|------|-----|-----|
| Amazon.com | 123.45        | 120.00         | 122.50| ... | ... |

#### Email Content
- Subject: `Automated mail from Python`
- Body:
  ```
  This is a mail from Python, generated automatically from the scraper.
  Attached is a CSV file containing the trading data.
  ```

---

## Thank You

Thank you for visiting this repository! Feel free to contribute or raise issues to improve the functionality.

