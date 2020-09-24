import re
import bs4


class OfferParser(object):
    
    def __init__(self, offer: bs4.element.Tag):
        self.offer = offer
    
    def get_old_price(self):
        try:
            price = self.offer.find('span', 
                                    class_='old-price_value').get_text()
            return int(re.findall(r'(.*) PLN\/os', price)[0].replace(" ", ""))
        except Exception as e:
            return None
        
    def get_current_price(self):
        try:
            price = self.offer.find('span', 
                                    class_='current-price_value').get_text()
            return int(re.findall(r'(.*)PLN \/ os', price)[0].replace(" ", ""))
        except Exception as e:
            print(e)
            return None
    
    def get_hotel_rank(self):
        try:
            return float(self.offer.find('span', 
                                        class_='hotel-rank').get_text())
        except AttributeError:
            return 0
    
    def get_url(self):
        return self.offer.find('a', 
                               {'class': 'offer_link pull-right'}).get('href')
    
    def get_offer_id(self):
        url = self.get_url()
        return re.findall(pattern=r".*ofr_id=(.{64})&.*", string=url)[0]

    @staticmethod
    def get_picture():
        return None

    def get_as_dict(self):
        result = {
            "old_price": self.get_old_price(),
            "current_price": self.get_current_price(),
            "rank": self.get_hotel_rank(),
            "link": self.get_url(),
            "offer_id": self.get_offer_id(),
            "picture": self.get_picture()
        }
        return result
