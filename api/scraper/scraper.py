import requests
from bs4 import BeautifulSoup
from functools import wraps
from api.scraper.proxies import Proxy
from api.scraper.Offer import Offer
from api.scraper.OfferParser import OfferParser
from api.scraper.helpers import get_today_date, get_date_with_timedelta
from api.scraper.images import get_photos_urls, get_offers, dupa
from api.scraper.config import chromedriver_path, user_agent, url


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


def scrap(_days: int = 1) -> list:
    _url = url.format(departure_date=get_date_with_timedelta(days=_days), date_from=get_today_date())
    headers = {'User-Agent': user_agent}
    # response = get_data_from_url(url=_url, headers=headers)
    response = dupa(chromedriver_path=chromedriver_path, url=_url)
    soup = BeautifulSoup(response, "html.parser")
    articles = soup.find_all('article', {'class': "offer clearfix"})
    assert len(articles) > 0, "no offers found."
    offers = []
    photos = get_photos_urls(chromedriver_path=chromedriver_path, url=_url)
    assert len(articles) == len(photos), "numbers of offers and pictures are not equal. {} - {}".format(len(articles), len(photos))
    for offer, photo in zip(articles, photos):
        parsed = OfferParser(offer).get_as_dict()
        parsed["picture"] = photo
        offers.append(Offer(**parsed))
    print(f"FOUND {Offer.number_of_offers} OFFERS")
    return [vars(offer) for offer in offers]

print(scrap())
