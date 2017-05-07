from search_store import *
import sys # command line args

URL_FILE = "urls.txt"

# Measured in seconds
# How long to delay the next loop iteration, measured in sec
SLEEP_DELAY = 120


# Def: Main function used to setup and run program
def main():
    print("Starting Program")
    if len(sys.argv) < 2:
        raise ValueError("Need to pass at least 1 argument for url file")

    # opening file in read mode
    f = open(str(sys.argv[1]), 'r')

    # Returns a list of Store object with urls from file passed by argument
    store_list = build_stores(f)
    f.close()

    # Main loop the checks items status
    print("Checking items")
    while True:
        for store in store_list:
            store.check_item()
        print('.', end='', flush=True)
        time.sleep(SLEEP_DELAY)


# Des: Takes a file path as a parameter, and builds a list of store objects from the urls in the file.
# Pre: None.
# Post: List of store objects returned.
def build_stores(f):
    store_list = []


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
            elif "target" in line:
                store_list.append(Target(line))
            elif "walmart" in line:
                store_list.append(Walmart(line))
            elif "toysrus" in line:
                store_list.append(ToysRUs(line))
            elif "newegg" in line:
                store_list.append(Newegg(line))
            else:
                print("Error: did not recognize line - " + line)
    return store_list

if __name__ == "__main__":
    main()
