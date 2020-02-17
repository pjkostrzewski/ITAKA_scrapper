from proxies import Proxy
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re


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
print(url)
# proxy = Proxy().get()
# print("connected", proxy)
# response = requests.get(url=url, proxies={"http": f"http://{proxy}","https": f"http://{proxy}"}).text
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

headers = { 'User-Agent' : user_agent }
response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
article = soup.find_all('article', {'class': "offer clearfix"})
for offer in article:
    try:
        tag = offer.find('span', class_='old-price_value').get_text()
    except:
        tag = None
    current_price_value = offer.find('span', class_='current-price_value').get_text()
    hotel_rank = offer.find('span', class_='hotel-rank').get_text()
    link = offer.find('a', {'class': 'offer_link pull-right'}).get('href')
    print(tag, current_price_value, hotel_rank)
    print(link)
    print(get_offer_id_from_url(link))
    print()

# gen2 = (x.get_text() for x in soup.find_all('span', class_='old-price_value')[::2])  # more pythonic way to generate all current offers

# <img src="https://i.content4travel.com/cms/img/u/desktop/seres/rktvile_0.jpg" class="figure_main-photo" alt="Hotel The Village by Rotana">
# to get picture ^^
