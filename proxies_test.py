import requests
from bs4 import BeautifulSoup

import pytest
from proxies import Proxy

def test_proxy_10_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(10)
    assert proxy.get()

def test_proxy_20_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(20)
    assert proxy.get()