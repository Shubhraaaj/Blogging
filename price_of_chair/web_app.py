__author__ = 'Shubhraj'

import requests
from bs4 import BeautifulSoup

web_url = "https://www.flipkart.com/craftico-polypropylene-door-mat-artificial-grass-mat-soft-durable-plastic-turf-carpet/p/itmf4yb3463rrrew"

request = requests.get(web_url)

content = request.content
soup = BeautifulSoup(content, "html.parser")

#<div class="_1vC4OE _3qQ9m1">₹26,199</div>
element = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})

price = element.text.strip() #Rs.26,199

price_without_symbol = price[1:] #26,199

pricey = float(price_without_symbol) #Convert string to float, Won't work because of comma

if pricey<200:
    print("Buy the Door Mat")
else:
    print("Don't buy the Door Mat")

print("Current Price: {}".format(pricey))

#strip() - removes all leading and trailing spaces
