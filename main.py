import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

# 1. get the price of the product
amazon_url = URL_OF_PRODUCT

headers= {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(amazon_url, headers=headers)
html_page = response.text

soup = BeautifulSoup(html_page, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText().strip("$")
price_as_float = float(price)
print(price_as_float)

product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)

# 2. if the price is below the prefered price, send me an email

#EMAIL INFO
SENDER_EMAIL = YOUR_EMAIL
PASSWORD = YOUR_EMAIL_PASSWORD
RECIPIENT_EMAIL = RECIPIENT_EMAIL
PREFERED_PRICE = PREFERED PRICE

if price_as_float < PREFERED_PRICE:

    message = f"{product_title} is now {price} only !"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:AMAZON PRICE ALERT!\n\n{message}\n{amazon_url}".encode('utf-8')
        )