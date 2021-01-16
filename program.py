import requests
import sched, time
import datetime
import webbrowser

sleep_time = 60*5
priority = 1
s = sched.scheduler(time.time, time.sleep)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}

def printResults(stock_label):
    # Print whether the item is out of stock or not along with the date and time
    date_and_time = str(datetime.datetime.today())
    print(stock_label + " - " + date_and_time)

def checkOnWebsite(sc, website, website_name, extraInfo: str, out_of_stock_keyword):
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
    s.enter(sleep_time, priority, checkOnWebsite, (sc,website,website_name,extraInfo,out_of_stock_keyword,))

microsoft_website_name = "Microsoft"
microsoft_keyword = "Out of stock"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.xbox.com/en-us/configure/8wj714n3rbtl?ranMID=24542&ranEAID=AKGBlS8SPlM&ranSiteID=AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ&epi=AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__limegwwdae31f62e0ptnsl31bn2xpxqtuttdjhss00%29%287593%29%281243925%29%28AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ%29%28%29&irclickid=_limegwwdae31f62e0ptnsl31bn2xpxqtuttdjhss00',microsoft_website_name,'',microsoft_keyword,))

best_buy_website_name = "Best Buy"
best_buy_keyword = "Sold Out"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324',best_buy_website_name,'',best_buy_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/35009727-f7d1-47df-8219-d68c6e83990c',best_buy_website_name,'ac valhalla',best_buy_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/f2914681-c213-4542-8293-7376bfc10f61',best_buy_website_name,'game pass',best_buy_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/7298b293-4d51-43fd-adb4-ad00cfa76c4f',best_buy_website_name,'extra controller',best_buy_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/907d28df-4262-40d3-8926-8d556f264857',best_buy_website_name,'game pass, extra controller',best_buy_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/7d2eb376-760d-4806-b239-668dcd0fe376',best_buy_website_name,'halo, game pass, extra controller',best_buy_keyword,))

gamestop_website_name = "Game Stop"
gamestop_keyword = "Not Available"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744Y.html',gamestop_website_name,'',gamestop_keyword,))

adorama_website_name = "Adorama"
adorama_keyword = "Temporarily not available"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001.html',adorama_website_name,'',adorama_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001a.html',adorama_website_name,'extra controller white',adorama_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001b.html',adorama_website_name,'extra controller black',adorama_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001c.html',adorama_website_name,'extra controller blue',adorama_keyword,))

costco_website_name = "Costco"
costco_keyword = "Out of Stock"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html',costco_website_name,'extra controller',costco_keyword,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html?langId=-1&krypto=v1iTKzfakYu7ufaGHAJhD7PIUL3dEtzLuxKt%2BP%2B0brN3S31Qw7B3uQAfXdihfLNEPm8Mz4sg1pi71Zyg463g0gzJJ8mfhcDfCTaFe8sL2QdRxcFqlWou4Jsfs2Ois3vokyb5RhfTIw%2FE6PS9AyRVMS86UaiD%2FQjo7EEOPs4TRmIYRqmGcB%2Fzl%2BqlI24vJLsYiEO5v1dAJXGJC0q8q8UpUMk%2F0gLWYfNntUBsGZaJ6ZVYA3Dj4LIV0nY7DlS0Wvna',costco_website_name,'extra controller (signed in)',costco_keyword,))


s.run()