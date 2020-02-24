class Offer(object):
    
    def __init__(self, offer_id: int, old_price: int, current_value: int, rank: float, link: str):
        self.id = offer_id
        self.old_price = old_price
        self.current_value = current_value
        self.rank = rank
        self.link = link
        self.reduction = self._calculate_reduction()
    
    def _calculate_reduction(self):
        return self.old_price - self.current_value if self.old_price else 0
    
