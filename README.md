# store_bot

The store bot is inteded to to be used as a way to detect when a item is on stock.

# Stores
Can be used with Amazon, BestBuy, Walmart, ToysRUs, and Target.

# Usage
The script currently runs with python 3.  The script takes a single parameter to specify the filepath the contains urls.  The html
from these urls will be pulled on a consecitve loop that the user can specify in the script driver.py file.  Each time the html is
pulled, the script will parse the html searching for specific keywords to indicate that the item is in stock.  If a url is detected
as in stock, the script will send the user a notification via email.

Example: python3 driver.py urls.txt

# urls
A file should be provided to the script that contains all the urls that the user wishes to monitor.  In the file containing the url
'#' can be used as comment and lines starting with '#' will be ignored.  Most urls can be obtained by simply navigating a item of a
supported store and simply copying the url with the exception of Target.  The standard url found for a Target item does not
contain the information of whether the item is in stock or not in the html code.  Instead a second url must be obtained, however
this url can be found in the Target item url html.

Example:

#This is a commanet

#This is a url to monitor

http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-neon-blue-and-neon-red-joy-con/141887

Features:
1. Detect when a url from a store contains a item.
2. Email notifications.

Future Features:
1. Twitter notifications.
2. Search system to search stores inventory to detect items.
3. Purchase item feature.
4. Add support for standard Target url
5. Parse html code using bs4 instead
