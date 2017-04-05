import urllib
from urllib import request
from smtp import *
import datetime

# How long to timeout a url when it is found in stock, measured in sec
TIME_OUT_DELAY = 3600

class Store:
    def __init__(self, url):
        self._url = url
        self._hotmail = hotmail()
        self._time_out = {}

    def get_html(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        con = urllib.request.urlopen(req)
        return con.read().decode('utf-8')

    def check_items(self):
        for url in self.url():
            self.check_time_out(url)
            if url not in self.time_out() and self.in_stock(url):
                print("In stock at: "+url)
                self.hotmail().send_email("In stock at: "+url)
                self.set_time_out(url, TIME_OUT_DELAY)

    def set_time_out(self, url, time_limit):
        self.time_out()[url] = datetime.datetime.now() + datetime.timedelta(seconds=time_limit)

    def check_time_out(self, url):
        now = datetime.datetime.now()
        if url in self.time_out():
            if now > self.time_out()[url]:
                del self.time_out()[url]

    # This function is just for show and should always be overloaded
    def in_stock(self, url):
        print("Error: did not run in_stock function from subclass")

    def url(self):
        return self._url

    def hotmail(self):
        return self._hotmail

    def time_out(self):
        return self._time_out

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

# --------------------------DOES NOT WORK!--------------------------------------
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