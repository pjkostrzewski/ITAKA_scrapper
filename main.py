from proxies import Proxy
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_today_date():
    date = datetime.now()
    return date.strftime("%Y-%m-%d")

def get_date_with_timedelta(days):
    assert 0 <= days < 4 
    if days == 0:
        return get_today_date()
    date = datetime.now() + timedelta(days=days)
    return date.strftime("%Y-%m-%d")

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
url = url.format(departure_date=get_date_with_timedelta(days=2), date_from=get_today_date())
print(url)
response = requests.get(url=url).text
soup = BeautifulSoup(response, "html.parser")
# tag = soup.find('span', class_='old-price_value')
# current_price_value = soup.find('span', class_='current-price_value').get_text()
# hotel_rank = soup.find('span', class_='hotel-rank').get_text()
# link = soup.find('a', {'class': 'offer_link pull-right'}).get('href')
def find_iter():
    tag = soup.find('span', class_='old-price_value')
    while tag is not None:
        yield tag.get_text()
        tag = tag.find_next('span', class_='current-price_value')

gen = find_iter()
running = True
while running:
    try:
        print(next(gen))
    except StopIteration:
        running = False
# current_price_value = soup.find('span', class_='current-price_value').get_text()
# hotel_rank = soup.find('span', class_='hotel-rank').get_text()
# link = soup.find('a', {'class': 'offer_link pull-right'}).get('href')
# # print(response.status_code)
# print(old_price_value, current_price_value, hotel_rank, "https://itaka.pl{link}".format(link=link))
