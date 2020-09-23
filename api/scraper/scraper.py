import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup
import re
from functools import wraps
from api.scraper.proxies import Proxy
from api.scraper.Offer import Offer
from api.scraper.OfferParser import OfferParser
from api.scraper.helpers import (url, user_agent,
                     get_today_date, get_date_with_timedelta)
from api.scraper.images import get_photos_urls


chromedriver_path = "/Users/patrykkostrzewski/Downloads/chromedriver"

# TODO  add some options file
# TODO  add some logging using Logger


def use_proxy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        proxy = Proxy().get()
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        return func(*args, proxies=proxies, **kwargs)
    return wrapper


# @use_proxy
def get_data_from_url(*args, **kwargs):
    return requests.get(*args, **kwargs).text


_url = url.format(departure_date=get_date_with_timedelta(days=1), date_from=get_today_date())
headers = {'User-Agent': user_agent}


def scrap():
    response = get_data_from_url(url=_url, headers=headers)
    soup = BeautifulSoup(response, "html.parser")
    article = soup.find_all('article', {'class': "offer clearfix"})
    assert len(article) > 0, "no offers found."
    offers = []
    photos = get_photos_urls(chromedriver_path=chromedriver_path, url=_url)
    assert len(article) == len(photos), "numbers of offers and pictures are not equal."
    for offer, photo in zip(article, photos):
        parsed = OfferParser(offer).get_as_dict()
        parsed["picture"] = photo
        offers.append(Offer(**parsed))
    for offer in offers:
        print(offer)
    print(f"FOUND {Offer.number_of_offers} OFFERS")
    return [vars(offer) for offer in offers]


print(scrap())

