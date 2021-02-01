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
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',best_buy_website_name,'NVIDIA',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196',best_buy_website_name,'EVGA FTW3 Ultra Gaming',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191',best_buy_website_name,'EVGA FTW3 Gaming',"Coming Soon",headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400',best_buy_website_name,'EVGA XC3 Ultra Gaming',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436194.p?skuId=6436194',best_buy_website_name,'EVGA XC3 Gaming',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175',best_buy_website_name,'MSI Ventus',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-gaming-oc-10g-gddr6x-pci-express-4-0-graphics-card-black/6430620.p?skuId=6430620',best_buy_website_name,'Gigabyte Gaming',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-vision-oc-10g-gddr6x-pci-express-4-0-graphics-card-white/6436219.p?skuId=6436219',best_buy_website_name,'Gigabyte Vision',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-aorus-master-10g-gddr6x-pci-express-4-0-graphics-card-black/6436223.p?skuId=6436223',best_buy_website_name,'Gigabyte Aorus Master',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?acampID=0&cmp=RMX&loc=Hatch&ref=198&skuId=6432445',best_buy_website_name,'Asus Strix',best_buy_keyword,headers,))

newegg_website_name = "Newegg"
newegg_keyword = "OUT OF STOCK"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?cm_mmc=vendor-nvidia&u1=s1611766491405ci1ca52439',newegg_website_name,'EVGA FTW3 Ultra Gaming',newegg_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519?cm_mmc=vendor-nvidia&u1=s1611766491405ci1ca52439',newegg_website_name,'EVGA FTW3 Gaming',newegg_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?cm_mmc=vendor-nvidia&u1=s1611766491405ci1ca52439',newegg_website_name,'EVGA XC3 Gaming',newegg_keyword,headers,))

bhphoto_website_name = "B&H Photo"
bhphoto_keyword = "Notify When Available"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bhphotovideo.com/c/product/1603617-REG/asus_rog_strix_rtx3080_o10g_gaming_rog_strix_geforce_rtx.html',bhphoto_website_name,'ASUS Strix OC',bhphoto_keyword,headers,))

# Do not remove
s.run()

#-------------------------------------------------------------------------------------