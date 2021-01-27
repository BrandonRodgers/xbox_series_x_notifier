import requests
import sched, time
import datetime
import webbrowser

#-------------------------------------------------------------------------------------

sleep_time = 60*5
priority = 1
s = sched.scheduler(time.time, time.sleep)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}

#-------------------------------------------------------------------------------------

def printResults(stock_label):
    # Print whether the item is out of stock or not along with the date and time
    date_and_time = str(datetime.datetime.today())
    print(stock_label + " - " + date_and_time)

#-------------------------------------------------------------------------------------

def checkOnWebsite(sc, website, website_name, extraInfo: str, out_of_stock_keyword, headers):
    try:
        res = requests.get(website,headers=headers)

        stock_label = ""
        siteInfo = ""
        if (len(extraInfo)):
            # extraInfo contains text
            siteInfo = website_name + " - " + extraInfo
        else:
            siteInfo = website_name

        if (out_of_stock_keyword in res.text):
            stock_label = "Out of stock - " + siteInfo
        else:
            stock_label = "In stock - " + siteInfo
            # Open the link in the browser if in stock
            webbrowser.open(website)

        printResults(stock_label)
    except:
        print("Exception occured with website: " + website + "\nextraInfo: " + extraInfo)

    s.enter(sleep_time, priority, checkOnWebsite, (sc,website,website_name,extraInfo,out_of_stock_keyword,headers))

#-------------------------------------------------------------------------------------

# Use this as an example
# best_buy_website_name = "Best Buy"
# best_buy_keyword = "Sold Out"
# s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324',best_buy_website_name,'',best_buy_keyword,headers,))

# Do not remove
s.run()

#-------------------------------------------------------------------------------------