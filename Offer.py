class Offer(object):
    
    number_of_offers = 0
    
    def __init__(self, offer_id: int, old_price: int, current_price: int, rank: float, link: str):
        self.offer_id = offer_id
        self.old_price = old_price
        self.current_price = current_price
        self.rank = rank
        self.link = link
        self.reduction = self._calculate_reduction()
        self.number_of_offers += 1
    
    def _calculate_reduction(self):
        return self.old_price - self.current_price if self.old_price else 0
