import requests
from bs4 import BeautifulSoup

import pytest
from proxies import Proxy

def test_proxy_3_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(3)
    assert proxy.get_proxy()

def test_proxy_5_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(5)
    assert proxy.get_proxy()

def test_proxy_10_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(10)
    assert proxy.get_proxy()

def test_proxy_20_attempts():
    proxy = Proxy()
    proxy.set_number_of_attempts(20)
    assert proxy.get_proxy()