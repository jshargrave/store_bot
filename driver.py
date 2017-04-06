import sys # exceptions
import time # adding and comparing times
from search_store import *

URL_FILE = "urls.txt"

# Measured in seconds
# How long to delay the next loop iteration, measured in sec
SLEEP_DELAY = 300

print("Starting Program")

# Def: Main function used to setup and run program
def main():
    store_list = build_stores(URL_FILE)

    print("checking items")
    while True:
        for store in store_list:
            store.check_item()
        time.sleep(SLEEP_DELAY)


# Des: Takes a file path as a parameter, and builds a list of store objects from the urls in the file.
# Pre: None.
# Post: List of store objects returned.
def build_stores(file):
    store_list = []
    f = open(file, 'r')

    # looping through all lines in file and building the correct objects
    for line in f.readlines():
        if line is not '\n' and line[0] is not '#':
            line = line.rstrip()
            if "amazon" in line:
                store_list.append(Amazon(line))
            elif "bestbuy" in line:
                store_list.append(BestBuy(line))
            elif "gamestop" in line:
                store_list.append(GameStop(line))
            elif "walmart" in line:
                store_list.append(Walmart(line))
            elif "toysrus" in line:
                store_list.append(ToysRUs(line))
            else:
                print("Error: did not recognize line - " + line)
    return store_list

if __name__ == "__main__":
    main()


