import time
from search_store import *
from smtp import *

print("Starting Program")

amazon_urls = ["https://www.amazon.com/Nintendo-Switch/dp/B01LTHP2ZK/ref=sr_tnr_p_1_videogames_1?s=videogames&ie=UTF8&qid=1484346353&sr=1-1&keywords=nintendo+switch",
               "https://www.amazon.com/Nintendo-Switch/dp/B01MUAGZ49/ref=sr_tnr_p_1_videogames_1?s=videogames&ie=UTF8&qid=1484346353&sr=1-1&keywords=nintendo%2Bswitch&th=1"]

bestybuy_urls = ["http://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/5670003.p?skuId=5670003",
                 "http://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/5670100.p?skuId=5670100"]

gamestop_urls = ["http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-gray-joy-con/141820",
                 "http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-neon-blue-and-neon-red-joy-con/141887"]

target_urls = ["http://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-52052007",
               "http://www.target.com/p/-/A-52189185",
               "http://www.target.com/p/the-legend-of-zelda-153-breath-of-the-wild-153-nintendo-switch/-/A-52161264"]

walmart_urls = ["https://www.walmart.com/co/47217353"]

toysrus_urls = ["http://www.toysrus.com/product/index.jsp?productId=119513636&cp=2255974.119659196&parentPage=family",
                "http://www.toysrus.com/product/index.jsp?productId=119513666&cp=2255974.119659196&parentPage=family"]

ama = Amazon(amazon_urls)
bes = BestBuy(bestybuy_urls)
gam = GameStop(gamestop_urls)
# target not working
#tar = Target(target_urls)
wal = Walmart(walmart_urls)
toy = ToysRUs(toysrus_urls)

# Measured in seconds
SLEEP_DELAY = 300

while True:
    ama.check_items()
    bes.check_items()
    gam.check_items()
    # tar.check_items()
    wal.check_items()
    toy.check_items()
    time.sleep(SLEEP_DELAY)
	
print("Program Finished")