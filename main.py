from proxies import Proxy
import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup

import re
from Offer import Offer
from OfferParser import OfferParser
from helpers import (url, user_agent,
                     get_today_date, get_date_with_timedelta,
                     get_offer_id_from_url)

  
url = url.format(departure_date=get_date_with_timedelta(days=1), 
                 date_from=get_today_date())

proxy = Proxy().get()
print("connected", proxy)

headers = {'User-Agent': user_agent}
try:
    response = requests.get(url=url,
                            headers=headers, 
                            proxies={"http": f"http://{proxy}","https": f"http://{proxy}"}).text
except ProxyError as e:
    print(e)
    response = requests.get(url=url,
                            headers=headers).text

soup = BeautifulSoup(response, "html.parser")
article = soup.find_all('article', {'class': "offer clearfix"})
assert len(article) > 0, "no offers found."

offers = list()
for offer in article:
    parsed = OfferParser(offer).get_as_dict()
    print(parsed["picture"])
    offers.append(Offer(**parsed))

for offer in offers:
    print(offer)

print(f"FOUND {Offer.number_of_offers} OFFERS")
