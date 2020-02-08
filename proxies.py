import requests
from bs4 import BeautifulSoup
from random import choice


class Proxy(object):
    proxies_url = "https://free-proxy-list.net/"
    httpbin_url = "https://httpbin.org/ip"

    def __init__(self):
        self.proxies = self._get_possible_proxies_from_website()
        self.attempts = 10

    def get_proxy(self):
        for _ in range(self.attempts):
            proxy = choice(tuple(self.proxies))
            try:
                response = requests.get(
                    self.httpbin_url, 
                    proxies={"http": f"http://{proxy}","https": f"http://{proxy}"},
                    timeout=3
                    )
                return proxy
            except: 
                print(proxy, "not connected.")

    def set_number_of_attempts(self, attempts: int): 
        assert 0 < attempts <= 20
        self.attempts = attempts

    def _get_possible_proxies_from_website(self):
        proxies = set()
        request = requests.get(self.proxies_url).text
        soup = BeautifulSoup(request, "html.parser")
        proxies_table = soup.find(id='proxylisttable')
        for row in proxies_table.tbody.find_all("tr"):
            proxies.add(str(row.find_all('td')[0].string) + ':' + str(row.find_all('td')[1].string))
        return proxies
