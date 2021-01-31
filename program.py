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

best_buy_website_name = "Best Buy"
best_buy_keyword = "Sold Out"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',best_buy_website_name,'',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/ps5-consoles/96be4c49-d98e-47c6-9a68-291c646d0e47',best_buy_website_name,'Spiderman',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/ps5-consoles/8f146095-0a5f-4993-b123-711a1d34745b',best_buy_website_name,'Extra Controller',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/ps5-consoles/c471fae2-1d2c-4870-ad3d-d39bffa39af2',best_buy_website_name,'Spider Man, COD, Demon Souls',best_buy_keyword,headers,))

gamestop_website_name = "Game Stop"
gamestop_keyword = "Not Available"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New',gamestop_website_name,'',gamestop_keyword,headers,))

walmart_website_name = "Walmart"
wlmart_keyword = "out of stock"
#s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.walmart.com/ip/PlayStation-5-Console/363472942',walmart_website_name,'',wlmart_keyword,headers,))

# Do not remove
s.run()

#-------------------------------------------------------------------------------------