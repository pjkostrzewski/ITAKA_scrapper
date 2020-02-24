import re
import bs4


class OfferParser(object):
    
    def __init__(self, offer: bs4.element.Tag):
        self.offer = offer

    def get_tag(self):
        try:
            old_price = self.offer.find('span', class_='old-price_value').get_text()
        except:
            return None
        finally:
            return int(re.findall(r'(\d \d\d\d) PLN\/os', old_price)[0].replace(" ", ""))
    
    def get_actual_price(self):
        return self.offer.find('span', class_='current-price_value').get_text()
    
    def get_hotel_rank(self):
        return self.offer.find('span', class_='hotel-rank').get_text()
    
    def get_url(self):
        return self.offer.find('a', {'class': 'offer_link pull-right'}).get('href')
    
    def get_offer_id(self):
        url = self.get_url()
        return re.findall(pattern=r".*ofr_id=(.{64})&.*", string=url)[0]