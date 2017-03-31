import urllib
from urllib import request


class Store:
    def __init__(self, url):
        self._url = url

    def get_html(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        con = urllib.request.urlopen(req)
        return con.read().decode('utf-8')

    def check_items(self):
        for url in self.url():
            if self.in_stock(url):
                print("In stock at: "+url)

    # This function is just for show and should always be overloaded
    def in_stock(self, url):
        print("Error: did not run in_stock function from subclass")

    def url(self):
        return self._url

class Amazon(Store):
    def in_stock(self, url):
        str = self.get_html(url)
        if "Add to Cart" in str:
            return True
        return False

class BestBuy(Store):
    def get_html(self, url):
        con = urllib.request.urlopen(url)
        return con.read().decode('utf-8')

    def in_stock(self, url):
        str = self.get_html(url)
        if "Add to Cart" in str:
            return True
        return False

class GameStop(Store):
    def in_stock(self, url):
        str = self.get_html(url)
        if "AddToCartClicked(this);" in str:
            return True
        return False

class Target(Store):
    def in_stock(self, url):
        str = self.get_html(url)
        if "add to cart" in str:
            return True
        return False

class Walmart(Store):
    def in_stock(self, url):
        str = self.get_html(url)
        if "Add to Cart" in str:
            return True
        return False

class ToysRUs(Store):
    def in_stock(self, url):
        str = self.get_html(url)
        if "class=\"truAddToCart  \"" in str:
            return True
        return False