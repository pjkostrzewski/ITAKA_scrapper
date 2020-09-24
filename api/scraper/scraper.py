import requests
from bs4 import BeautifulSoup
from functools import wraps
from api.scraper.proxies import Proxy
from api.scraper.Offer import Offer
from api.scraper.OfferParser import OfferParser
from api.scraper.helpers import get_today_date, get_date_with_timedelta
from api.scraper.images import get_photos_urls, get_html_source, _scroll_down_page
from api.scraper.config import chromedriver_path, user_agent, url
from selenium import webdriver


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

#
# def scrap(_days: int = 1) -> list:
#     _url = url.format(departure_date=get_date_with_timedelta(days=_days), date_from=get_today_date())
#     headers = {'User-Agent': user_agent}
#     # response = get_data_from_url(url=_url, headers=headers)
#     response = get_html_source(chromedriver_path=chromedriver_path, url=_url)
#     print(response)
#     soup = BeautifulSoup(response, "html.parser")
#     articles = soup.find_all('article', {'class': "offer clearfix"})
#     assert len(articles) > 0, "no offers found."
#     offers = []
#     photos = get_photos_urls(chromedriver_path=chromedriver_path, url=_url)
#     assert len(articles) == len(photos), "numbers of offers and pictures are not equal. {} - {}".format(len(articles), len(photos))
#     for offer, photo in zip(articles, photos):
#         parsed = OfferParser(offer).get_as_dict()
#         parsed["picture"] = photo
#         offers.append(Offer(**parsed))
#     print(f"FOUND {Offer.number_of_offers} OFFERS")
#     return [vars(offer) for offer in offers]

# print(scrap())


class Scraper:
    def __init__(self):
        self.options = self.get_options()
        self.browser = webdriver.Chrome(chromedriver_path, options=self.options)
        self.browser.get(url)

    @staticmethod
    def get_options():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return options

    def close(self):
        self.browser.close()
        self.browser.quit()

    def scroll_down_page(self, speed=8):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.browser.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.browser.execute_script("return document.body.scrollHeight")

    def get_html_page_source(self):
        return self.browser.page_source

    def get_photos(self) -> list:
        self.scroll_down_page(speed=8)
        self.browser.find_element_by_id("pushAd_disagree_button").click()
        offers_elements = self.browser.find_elements_by_class_name("offer_figure")
        print(f"FOUND {len(offers_elements)} PHOTOS")
        return [offer.find_element_by_class_name("figure_main-photo").get_attribute("src") for offer in offers_elements]

    def get_offers(self) -> list:
        response = self.get_html_page_source()
        soup = BeautifulSoup(response, "html.parser")
        articles = soup.find_all('article', {'class': "offer clearfix"})
        assert len(articles) > 0, "no offers found."
        offers = []
        for offer in articles:
            parsed = OfferParser(offer).get_as_dict()
            offers.append(parsed)
        print(f"FOUND {len(offers)} OFFERS")
        return offers

    def get_merged_data(self) -> list:
        offers = self.get_offers()
        photos = self.get_photos()
        assert len(offers) == len(photos)
        result = []
        for offer, photo in zip(offers, photos):
            offer['picture'] = photo
            result.append(offer)
        return result


scraper = Scraper()
print(scraper.get_merged_data())
