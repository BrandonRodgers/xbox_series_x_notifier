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

microsoft_website_name = "Microsoft"
microsoft_keyword = "Out of stock"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.xbox.com/en-us/configure/8wj714n3rbtl?ranMID=24542&ranEAID=AKGBlS8SPlM&ranSiteID=AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ&epi=AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__limegwwdae31f62e0ptnsl31bn2xpxqtuttdjhss00%29%287593%29%281243925%29%28AKGBlS8SPlM-dmcd7KM4SNoLZ26eW2KfdQ%29%28%29&irclickid=_limegwwdae31f62e0ptnsl31bn2xpxqtuttdjhss00',microsoft_website_name,'',microsoft_keyword,headers,))

best_buy_website_name = "Best Buy"
best_buy_keyword = "Sold Out"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324',best_buy_website_name,'',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/35009727-f7d1-47df-8219-d68c6e83990c',best_buy_website_name,'ac valhalla',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/f2914681-c213-4542-8293-7376bfc10f61',best_buy_website_name,'game pass',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/7298b293-4d51-43fd-adb4-ad00cfa76c4f',best_buy_website_name,'extra controller',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/907d28df-4262-40d3-8926-8d556f264857',best_buy_website_name,'game pass, extra controller',best_buy_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/7d2eb376-760d-4806-b239-668dcd0fe376',best_buy_website_name,'halo, game pass, extra controller',best_buy_keyword,headers,))

gamestop_website_name = "Game Stop"
gamestop_keyword = "Not Available"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744Y.html',gamestop_website_name,'',gamestop_keyword,headers,))

# adorama_website_name = "Adorama"
# adorama_keyword = "Temporarily not available"
# adorama_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
#                    'upgrade-insecure-requests': '1',
#                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                    'accept-encoding': 'gzip, deflate, br',
#                    'accept-language': 'en-US,en;q=0.9',
#                    'cookie': 'AJAXrefby=rflaid64367; refby=rflaid64367; header_refby=rflaid64367; SSSC=500.G6918489700386890293.1|51552.1814119:56174.2012220:58058.2095632:59339.2126234; akCountry=US; SSOD=AI1WAAAAEACZMg4AAgAAALppA2C6aQNgAAA; sid3=02feea0a-b703-4143-91ee-d42a48c7169e; js_sid=1; lastPrtcl=https%3A; PUID=02feea0a-b703-4143-91ee-d42a48c7169e; _gid=GA1.2.715541585.1610836409; Session_Refby=; Session_Refby_Processed=rflaid64367; _pxvid=dc5a7383-584a-11eb-b924-0242ac12000e; _evga_c81d={%22uuid%22:%22d7edad2c0ecd53c4%22}; _gcl_au=1.1.1270992284.1610836410; _fbp=fb.1.1610836410411.1886614699; IR_gbd=adorama.com; wpn_https={"last_shown":"Sat, 16 Jan 2021 22:33:30 GMT","shown_count":1}; _pin_unauth=dWlkPVptVXpaVEF4TWpFdFltSTBOeTAwTkdSaUxXRTFOelV0T1RRNU9EWTVaRFZqT0dGaQ; dtm_token=AQEDKk5QbupLbwE383F_AQHyQgE; __rutmb=113083348; __ruid=113083348-xa-ok-4y-1p-68k6uq18xdcutuxarl1i-1610836411262; __rcmp=0!bj1fZ2MsZj1nYyxzPTAsYz0xOTY5LHRyPTAscm49MzE5LHRzPTIwMjEwMTE2LjIyMzMsZD1wYztuPXNiMSxmPXNiLHM9MCxjPTEyOTYsdD0yMDE3MDczMS4xODM0; _vz=viz_600369bbdaa6c; _svsid=02ce66f9e60e095fc744122f25a82d84; visitor_id416222=955430632; visitor_id416222-hash=b9a700e110645690779221ede788818c84c9be20ca2d8ea7a2fd5328bfb87d1631b2dab4ab1c3f473a360cf2281dceb8821db114; SSID=CABP8B04AAAAAAC6aQNgNWLCDbppA2ABAAAAAAAAAAAAumkDYADo-MvnAAOacSAAumkDYAEAYMkAAWeuGwC6aQNgAQDK4gADEPofALppA2ABAG7bAAM8tB4AumkDYAEA; usi_prod_pic_1=https%253A%252F%252Fwww.adorama.com%252Fimages%252FLarge%252Fxbrrt00001b.jpg; usi_prod_name_1=Series%2520X%2520Bundle%2520with%2520Wireless%2520Controller%2520(Black); usi_prod_price_1=559.98; usi_prod_pic_2=https%253A%252F%252Fwww.adorama.com%252Fimages%252FLarge%252Fxbrrt00001c.jpg; usi_prod_name_2=Series%2520X%2520Bundle%2520with%2520Wireless%2520Controller%2520(Shock%2520Bl; usi_prod_price_2=564.98; g_state={"i_p":1610843651042,"i_l":1}; usi_launched=t1610836681915; SSRT=SWwDYAADAA; InvisibleParameter=priceMode%3D0%7C0%7C0%7C0%7C0%26pagePriceMode%3D0%7C0%7C0%7C0%7C0%26country%3DUS%26productVersion%3D1574%26perPage%3D25%26sort%3D%26descSort%3D%26isVip%3Dfalse%26isVip360%3Dfalse%26isLoggedIn%3Dfalse%26mode%3D%26isFreeShipPromo%3Dfalse%26clientUtcOffset%3D-6%26bankId%3D1; activeUser=1; viz_sent=1; InvisibleParameterChanger=ClientUtcOffset%3D-6; sub-website=; a=b; _uetsid=dbacf8e0584a11ebb0eb1fdc24ab243c; _uetvid=dbad1af0584a11eb9f5947b9d7acb6ce; sailthru_pageviews=13; _br_uid_2=uid%3D395575047657%3Av%3D15.0%3Ats%3D1610836410459%3Ahc%3D12; IR_1036=1610837079551%7C0%7C1610836410587%7C3KlWEkRa-UZC3hG0hOXsYQiDUkEUtfTtLVnvx00%7C; IR_PI=6bd5a610-9dfe-8c5f-645a-046ae834c5db%7C1610923479551; sailthru_content=64f8778b40d4ae3c56acd0df73a9aa961c4fba69e4317f1bb475b2acaccebeb854e0ae23f737cb86556857d26c7d8e270cf55aa5411b13ab7c8586cee5d4f41b767073888ba5625101f49ca888f12219; sailthru_visitor=78e44e0d-8e22-4fa3-8279-32ccadfd0c94; mp_adorama_mixpanel=%7B%22distinct_id%22%3A%20%221770d5500f66f6-07093a19decf2a-7d677965-5dc000-1770d5500f7758%22%2C%22bc_persist_updated%22%3A%201610836410617%7D; __rutma=113083348-xa-ok-4y-1p-68k6uq18xdcutuxarl1i-1610836411262.1610836411262.1610836411262.1.13.13; usi_prod_price_3=559.98; usi_prod_pic_3=https%253A%252F%252Fwww.adorama.com%252Fimages%252FLarge%252Fxbrrt00001b.jpg; usi_prod_name_3=Series%2520X%2520Bundle%2520with%2520Wireless%2520Controller%2520(Black); _ga=GA1.1.396206354.1610836409; __rpck=0!eyJwcm8iOiJodHRwczovL3d3dy5pZHJvcG5ld3MuY29tLyIsImJ0Ijp7IjAiOnRydWUsIjEiOjAsIjIiOm51bGwsIjMiOjF9LCJDIjp7IiR7aH0sJHtUfSwke2R9LGR0ODA6MTArIjoxfSwiTiI6e319; _ga_L14X51CYC0=GS1.1.1610836409.1.1.1610837087.0; needlepin=N190d16108364112483eeb00111d813b829bc813b829bc813b82c7b00000000000000000813b829bc00000000000000; _px2=eyJ1IjoiNjM1MjUxMzAtNTg0Yy0xMWViLTk3NDctNWZjNWVjYTRjYWQyIiwidiI6ImRjNWE3MzgzLTU4NGEtMTFlYi1iOTI0LTAyNDJhYzEyMDAwZSIsInQiOjE2MTA4MzczMTQ3MDksImgiOiJmYTQ0OGM5ZTM4NjNiZTEzMTZhYWY5YjZlYTIwOTk3MDAyMGIwODQ4MzUyNTdlYzkyYTNmZTYzZDA4ZjUxMDliIn0=; __rpckx=0!eyJ0NyI6eyIyIjoxNjEwODM2NDM1MDMxLCIzIjoxNjEwODM2NDM3OTk1LCI0IjoxNjEwODM2NDQwMDYxLCI2IjoxNjEwODM3MDY2MTMxLCI3IjoxNjEwODM3MDY4NTgyLCI4IjoxNjEwODM3MDY5MDQyfSwidDd2Ijp7IjIiOjE2MTA4MzY0MzUwMzEsIjMiOjE2MTA4MzY0Mzc5OTUsIjQiOjE2MTA4MzY0NDAwNjEsIjYiOjE2MTA4MzcwNjYxMzEsIjciOjE2MTA4MzcwNjg1ODIsIjgiOjE2MTA4MzcyNDk4Mzd9LCJpdGltZSI6IjIwMjEwMTE2LjIyNDQifQ~~'}
# s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001.html',adorama_website_name,'',adorama_keyword,adorama_headers,))
# s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001a.html',adorama_website_name,'extra controller white',adorama_keyword,adorama_headers,))
# s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001b.html',adorama_website_name,'extra controller black',adorama_keyword,adorama_headers,))
# s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.adorama.com/xbrrt00001c.html',adorama_website_name,'extra controller blue',adorama_keyword,adorama_headers,))

costco_website_name = "Costco"
costco_keyword = "Out of Stock"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html',costco_website_name,'extra controller',costco_keyword,headers,))
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.costco.com/xbox-series-x-1tb-console-with-additional-controller.product.100691493.html?langId=-1&krypto=v1iTKzfakYu7ufaGHAJhD7PIUL3dEtzLuxKt%2BP%2B0brN3S31Qw7B3uQAfXdihfLNEPm8Mz4sg1pi71Zyg463g0gzJJ8mfhcDfCTaFe8sL2QdRxcFqlWou4Jsfs2Ois3vokyb5RhfTIw%2FE6PS9AyRVMS86UaiD%2FQjo7EEOPs4TRmIYRqmGcB%2Fzl%2BqlI24vJLsYiEO5v1dAJXGJC0q8q8UpUMk%2F0gLWYfNntUBsGZaJ6ZVYA3Dj4LIV0nY7DlS0Wvna',costco_website_name,'extra controller (signed in)',costco_keyword,headers,))

ant_online_website_name = "Ant Online"
ant_online_keyword = "Sold Out"
s.enter(sleep_time, priority, checkOnWebsite, (s,'https://www.antonline.com/microsoft/xbox/xbox-series-x-s',ant_online_website_name,'',ant_online_keyword,headers,))

s.run()

#-------------------------------------------------------------------------------------