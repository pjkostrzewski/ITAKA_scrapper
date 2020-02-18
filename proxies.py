import requests
from bs4 import BeautifulSoup
from random import choice


class Proxy(object):
    proxies_url = "https://free-proxy-list.net/"
    httpbin_url = "https://httpbin.org/ip"

    def __init__(self):
        self.attempts = 20
        self.proxies = self._get_possible_proxies_from_website()

    def get(self):
        print("looking for proxy connection. attempts {}".format(self.attempts))
        for _ in range(self.attempts):
            proxy = choice(tuple(self.proxies))
            try:
                requests.get(
                    url=self.httpbin_url, 
                    proxies={"http": f"http://{proxy}","https": f"http://{proxy}"},
                    timeout=3
                    )
                return proxy
            except: pass
        raise Exception("proxy connection not established.")

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
