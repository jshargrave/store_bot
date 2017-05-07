from urllib import request
from urllib import error
from smtp import *
import urllib
import json
import datetime
import time

# How long to timeout a url when it is found in stock, measured in sec
TIME_OUT_DELAY = 86400


class Store:
    def __init__(self, url):
        self._url = url
        self._email = hotmail()
        self._time_out = {}

    def check_item(self):
        self.check_time_out()
        try:
            if self.url() not in self.time_out() and self.in_stock():
                        print(self.get_msg())
                        self.email().send_email(self.get_msg())
                        self.set_time_out(self.now_date_plus_sec(TIME_OUT_DELAY))
        except urllib.error.HTTPError as e:
            print(e)
            print("Error Retrieving " + self.url())
        except urllib.error.URLError as e:
            print(e)

    def set_time_out(self, date):
        self.time_out()[self.url()] = date

    def now_date_plus_sec(self, sec):
        return datetime.datetime.now() + datetime.timedelta(seconds=sec)

    def check_time_out(self):
        now = datetime.datetime.now()
        if self.url() in self.time_out():
            if now > self.time_out()[self.url()]:
                del self.time_out()[self.url()]

    # This function is just for show and should always be overloaded
    def in_stock(self):
        raise Exception("Error: did not run in_stock function from subclass")

    def get_html(self):
        req = urllib.request.Request(self.url(), headers={'User-Agent': "Magic Browser"})
        con = urllib.request.urlopen(req)
        html = con.read().decode('utf-8')
        con.close()
        return html

    def get_msg(self):
        return "\nIn Stock: " + self.url()

    def url(self):
        return self._url

    def email(self):
        return self._email

    def time_out(self):
        return self._time_out


class Amazon(Store):
    def in_stock(self):
        html = self.get_html()
        if "Add to Cart" in html:
            return True
        return False

    def get_msg(self):
        return "\nAmazon: " + self.url()


class BestBuy(Store):
    def get_html(self):
        con = urllib.request.urlopen(self.url())
        return con

    def in_stock(self):
        html = self.get_html()
        if "Add to Cart" in html:
            return True
        return False

    def get_msg(self):
        return "\nBestBuy: " + self.url()


class GameStop(Store):
    def in_stock(self):
        html = self.get_html()
        if "AddToCartClicked(this);" in html:
            return True
        return False

    def get_msg(self):
        return "\nGameStop: " + self.url()


class Target(Store):
    def in_stock(self):
        html = self.get_html()
        j = json.loads(html)
        if (j["product"]["available_to_promise_network"]["availability"]) == "AVAILABLE":
            return True
        return False

    def get_msg(self):
        html = self.get_html()
        j = json.loads(html)
        return "\nTarget: " + j["product"]["item"]["buy_url"]


class Walmart(Store):
    def in_stock(self):
        html = self.get_html()
        if "Add to Cart" in html:
            return True
        return False

    def get_msg(self):
        return "\nWalmart: " + self.url()


class ToysRUs(Store):
    def in_stock(self):
        html = self.get_html()
        if "class=\"truAddToCart  \"" in html:
            return True
        return False

    def get_msg(self):
        return "\nToysRUS: " + self.url()


class Newegg(Store):
    def in_stock(self):
        html = self.get_html()
        if "product_instock:['1']," in html:
            return True
        return False

    def get_msg(self):
        return "\nNewEgg: " + self.url()
