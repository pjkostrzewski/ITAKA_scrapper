import re
from datetime import datetime, timedelta


url = 'https://www.itaka.pl/last-minute/?departureDate={departure_date}&view=offerList&package-type=wczasy&adults=2&date-from={date_from}&promo=lastMinute&order=dateFromAsc&total-price=0&page=1&transport=bus%2Cflight&currency=PLN'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'


def get_today_date():
    date = datetime.now()
    return date.strftime("%Y-%m-%d")


def get_date_with_timedelta(days):
    assert 0 <= days < 4 
    if days == 0:
        return get_today_date()
    date = datetime.now() + timedelta(days=days)
    return date.strftime("%Y-%m-%d")


def get_offer_id_from_url(url):
    return re.findall(pattern=r".*ofr_id=(.{64})&.*", 
                      string=url)[0]
