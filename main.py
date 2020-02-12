from proxies import Proxy
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_date(days=1):
    assert 0 <= days < 4 
    if days == 0:
        date = datetime.now()
        return date.strftime("%Y-%m-%d")
    date = datetime.now() + timedelta(days=days)
    return date.strftime("%Y-%m-%d")
#  request:
#  https://www.itaka.pl/last-minute/?departureDate=2020-02-13&view=offerList&package-type=wczasy&adults=2&date-from=2020-02-12&promo=lastMinute&order=dateFromAsc&total-price=0&page=1&transport=bus%2Cflight&currency=PLN

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
url = 'https://www.itaka.pl/last-minute/?departureDate=2020-02-13&view=offerList&package-type=wczasy&adults=2&date-from=2020-02-12&promo=lastMinute&order=dateFromAsc&total-price=0&page=1&transport=bus%2Cflight&currency=PLN'
response = requests.get(url=url)
print(response.status_code)
