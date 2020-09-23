import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup
import re
from api.scraper.proxies import Proxy
from api.scraper.Offer import Offer
from api.scraper.OfferParser import OfferParser
from api.scraper.helpers import (url, user_agent,
                     get_today_date, get_date_with_timedelta,
                     get_offer_id_from_url)
from time import sleep
from api.scraper.images import get_photos_urls


chromedriver_path = "/Users/patrykkostrzewski/Downloads/chromedriver"


def scrap():
    use_proxy = False
    _url = url.format(departure_date=get_date_with_timedelta(days=1),
                     date_from=get_today_date())
    headers = {'User-Agent': user_agent}

    if use_proxy:
        proxy = Proxy().get()
        print("connected", proxy)
        try:
            response = requests.get(url=_url,
                                    headers=headers,
                                    proxies={"http": f"http://{proxy}","https": f"http://{proxy}"}
                                    ).text
        except ProxyError as e:
            print(e)
            response = requests.get(url=_url,
                                    headers=headers).text
    else:
        response = requests.get(url=_url,
                                headers=headers
                                ).text

    soup = BeautifulSoup(response, "html.parser")
    article = soup.find_all('article', {'class': "offer clearfix"})
    assert len(article) > 0, "no offers found."

    offers = list()
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
