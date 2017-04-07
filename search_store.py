from urllib import request
from smtp import *
import urllib
import json
import datetime

# How long to timeout a url when it is found in stock, measured in sec
TIME_OUT_DELAY = 8640

class Store:
    def __init__(self, url):
        self._url = url
        self._hotmail = hotmail()
        self._time_out = {}

    def check_item(self):
        self.check_time_out()
        if self.url() not in self.time_out() and self.in_stock():
            print(self.get_msg())
            self.hotmail().send_email(self.get_msg())
            self.set_time_out()

    def set_time_out(self):
        self.time_out()[self.url()] = datetime.datetime.now() + datetime.timedelta(seconds=TIME_OUT_DELAY)

    def check_time_out(self):
        now = datetime.datetime.now()
        if self.url() in self.time_out():
            if now > self.time_out()[self.url()]:
                del self.time_out()[self.url()]

    # This function is just for show and should always be overloaded
    def in_stock(self):
        print("Error: did not run in_stock function from subclass")

    def get_html(self):
        req = urllib.request.Request(self.url(), headers={'User-Agent': "Magic Browser"})
        con = urllib.request.urlopen(req)
        return con

    def html_to_string(self, con):
        return con.read().decode('utf-8')

    def get_msg(self):
        return "In Stock: " + self.url()

    def url(self):
        return self._url

    def msg(self):
        return self._msg

    def hotmail(self):
        return self._hotmail

    def time_out(self):
        return self._time_out

class Amazon(Store):
    def in_stock(self):
        con = self.get_html()
        if "Add to Cart" in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "Amazon: " + self.url()

class BestBuy(Store):
    def get_html(self):
        con = urllib.request.urlopen(self.url())
        return con

    def in_stock(self):
        con = self.get_html()
        if "Add to Cart" in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "BestBuy: " + self.url()

class GameStop(Store):
    def in_stock(self):
        con = self.get_html()
        if "AddToCartClicked(this);" in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "GameStop: " + self.url()

class Target(Store):
    def in_stock(self):
        con = self.get_html()
        j = json.loads(self.html_to_string(con))
        if (j["product"]["available_to_promise_network"]["availability"]) == "AVAILABLE":
            return True
        return False

    def get_msg(self):
        con = self.get_html()
        j = json.loads(self.html_to_string(con))
        return "Target: " + j["product"]["item"]["buy_url"]

class Walmart(Store):
    def in_stock(self):
        con = self.get_html()
        if "Add to Cart" in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "Walmart: " + self.url()

class ToysRUs(Store):
    def in_stock(self):
        con = self.get_html()
        if "class=\"truAddToCart  \"" in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "ToysRUS: " + self.url()

class Newegg(Store):
    def in_stock(self):
        con = self.get_html()
        if "product_instock:['1']," in self.html_to_string(con):
            return True
        return False

    def get_msg(self):
        return "NewEgg: " + self.url()