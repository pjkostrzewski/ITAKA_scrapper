import re
from datetime import datetime, timedelta


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
