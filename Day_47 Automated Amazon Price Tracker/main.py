import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.com/dp/B097VJS3Y3?ref_=Oct_DLandingS_D_d6d12dad_NA"
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}
YOUR_EMAIL = "shetti1012@gmail.com"
YOUR_PASSWORD ="Shetti1000"

response = requests.get(url,headers=header)
data = response.text

soup = BeautifulSoup(response.content,"lxml")
print(soup.prettify())

soup = BeautifulSoup(data,"lxml")
price = soup.find(name="span",class_="a-offscreen")
price_text = price.get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
