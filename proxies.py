import requests
from bs4 import BeautifulSoup
from random import shuffle


class Proxy(object):
    proxies_url = "https://free-proxy-list.net/"

    def __init__(self):
        self.proxies = self._get_possible_proxies_from_website()

    def get_proxy(self):
        for proxy in self.proxies:
            try:
                response = requests.get('https://httpbin.org/ip', proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=3)
                return proxy
            except: pass

    def _get_possible_proxies_from_website(self):
        proxies = set()
        request = requests.get(self.proxies_url).text
        soup = BeautifulSoup(request, "html.parser")
        proxies_table = soup.find(id='proxylisttable')
        for row in proxies_table.tbody.find_all("tr"):
            proxies.add(str(row.find_all('td')[0].string) + ':' + str(row.find_all('td')[1].string))
        return proxies
