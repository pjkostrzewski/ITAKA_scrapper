from proxies import Proxy
import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from Offer import Offer
from OfferParser import OfferParser


def get_today_date():
    date = datetime.now()
    return date.strftime("%Y-%m-%d")

def get_date_with_timedelta(days):
    assert 0 <= days < 4 
    if days == 0:
        return get_today_date()
    date = datetime.now() + timedelta(days=days)
    return date.strftime("%Y-%m-%d")

def get_offer_id_from_url(url):
    return re.findall(pattern=r".*ofr_id=(.{64})&.*", string=url)[0]
    
'''
https://www.itaka.pl/last-minute/
?departureDate=2020-02-13
&view=offerList
&package-type=wczasy
&adults=2
&date-from=2020-02-12
&promo=lastMinute
&order=dateFromAsc
&total-price=0
&page=1
&transport=bus%2Cflight
&currency=PLN
'''
url = 'https://www.itaka.pl/last-minute/?departureDate={departure_date}&view=offerList&package-type=wczasy&adults=2&date-from={date_from}&promo=lastMinute&order=dateFromAsc&total-price=0&page=1&transport=bus%2Cflight&currency=PLN'
url = url.format(departure_date=get_date_with_timedelta(days=1), date_from=get_today_date())

proxy = Proxy().get()
print("connected", proxy)

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
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

offers = list()  # offers container
for offer in article:
    parsed = OfferParser(offer).get_as_dict()
    offers.append(Offer(**parsed))

for offer in offers:
    print(offer)

print(f"FOUND {Offer.number_of_offers} OFFERS")
# <img src="https://i.content4travel.com/cms/img/u/desktop/seres/rktvile_0.jpg" class="figure_main-photo" alt="Hotel The Village by Rotana">
# to get picture ^^
