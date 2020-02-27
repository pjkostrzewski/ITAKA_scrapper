class Offer(object):
    
    number_of_offers = 0
    
    def __init__(self, offer_id: int, old_price: int, current_price: int, rank: float, link: str, picture):
        self.offer_id = offer_id
        self.old_price = old_price
        self.current_price = current_price
        self.rank = rank
        self.link = link
        self.picture = picture
        self.reduction = self._calculate_reduction()
        self.percentage = self._calculate_percentage()
        self.destination = self._get_destination()
        Offer.number_of_offers += 1
    
    def __str__(self):
        if self.old_price:
            return "{}zł -> {}zł  ({}%)  |  {}  |  {}".format(self.old_price, self.current_price, self.percentage, self.rank, self.destination)
        else:
            return "{}zł  |  {}  |  {}".format(self.current_price, self.rank, self.destination)
        
    
    def _calculate_reduction(self) -> int:
        return self.old_price - self.current_price if self.old_price else 0

    def _calculate_percentage(self) -> int:
        if not self.old_price:
            return 0
        ratio = self.current_price / self.old_price
        return -int((1 - ratio) * 100)
    
    def _get_destination(self) -> str:
        return self.link.split("/")[2].replace("-", " ").title()