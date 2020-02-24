import re
import bs4


class OfferParser(object):
    
    def __init__(self, offer: bs4.element.Tag):
        self.offer = offer

    def _get_parsed_price(self, price: str):
        return int(re.findall(r'(\d \d\d\d) PLN\/os', price)[0].replace(" ", ""))
    
    def get_old_price(self):
        try:
            price = self.offer.find('span', class_='old-price_value').get_text()
        except:
            return None
        finally:
            return self._get_parsed_price(price)
    
    def get_current_price(self):
        price = self.offer.find('span', class_='current-price_value').get_text()
        return self._get_parsed_price(price)
    
    def get_hotel_rank(self):
        return self.offer.find('span', class_='hotel-rank').get_text()
    
    def get_url(self):
        return self.offer.find('a', {'class': 'offer_link pull-right'}).get('href')
    
    def get_offer_id(self):
        url = self.get_url()
        return re.findall(pattern=r".*ofr_id=(.{64})&.*", string=url)[0]
    
    def get_as_dict(self):
        result = {
            "old_price": self.get_old_price(),
            "current_price": self.get_current_price(),
            "ank": self.get_hotel_rank(),
            "link": self.get_url(),
            "offer_id": self.get_offer_id()
        }
        return result