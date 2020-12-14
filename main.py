#!/usr/bin/env python
"""
Step 1. Open up any website in chrome and set it to the size you want on the screen.
Step 2. Run the script
Step 3. Use the GUI to open up links
Step 4. Wait until the end of time to find a PS5
Step 5. Hopefully spend too much money on a PS5 (so the opposite of profit)
"""
from functools import partial
import tkinter as tk
import webbrowser


PS5_URLS = {
    'Sony Direct': 'https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816',
    'Target': 'https://www.target.com/p/playstation-5-console/-/A-81114595',
    'BestBuy': 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
    'Best Buy (bundles)': 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&fs=saas&id=pcat17071&iht=y&keys=keys&ks=960&list=n&nrp=15&saas=saas&sc=Global&sp=-currentprice%20skuidsaas&st=ps5%20bundle&type=page&usc=All%20Categories',
    'GameStop': 'https://www.gamestop.com/video-games/playstation-5/consoles',
    'Walmart': 'https://www.walmart.com/ip/Sony-PlayStation-5/363472942',
    'Amazon': 'https://www.amazon.com/dp/B08FC5L3RG',
    'NewEgg': 'https://www.newegg.com/PlayStation-PS5-Systems/BrandSubCat/ID-1541-3762',
    'Ant Online (bundle)': 'https://www.antonline.com/Sony/Electronics/Gaming_Devices/Gaming_Consoles/1409261',
    'Fred Meyer': 'https://www.fredmeyer.com/pr/playstation-5',
    'Costco': 'https://www.costco.com/sony-playstation-5-gaming-console-bundle.product.100691489.html',
    'Now In Stock': 'https://www.nowinstock.net/videogaming/consoles/sonyps5/',
}
HELPER_URLS = {
    'Spieltimes YT': 'https://www.youtube.com/c/SpielTimes/videos',
    'Tweet Deck': 'https://tweetdeck.twitter.com/',
    'Now In Stock': 'https://www.nowinstock.net/videogaming/consoles/sonyps5/',
}

INCOGNITO_PATH = f'"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --args --new-window --incognito %s'

def open_normal(url):
    webbrowser.get('chrome').open(url)

def open_incognito(url):
    webbrowser.get(INCOGNITO_PATH).open_new(url)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('PS5 Links')

    reg_label = tk.Label(window, text="Regular websites").grid(row=0, column=0)
    for i, (desc, url) in enumerate(HELPER_URLS.items(), start=1):
            go_to_website = partial(open_normal, url)

            button = tk.Button(
                master=window,
                text=desc,
                width=16,
                height=2,
                bg="blue",
                fg="yellow",
                command=go_to_website
            ).grid(row=i, column=0)

    incog_label = tk.Label(window, text="Incognito").grid(row=0, column=1)
    for i, (desc, url) in enumerate(PS5_URLS.items(), start=1):
        go_to_website = partial(open_incognito, url)

        button = tk.Button(
            master=window,
            text=desc,
            width=16,
            height=2,
            bg="blue",
            fg="yellow",
            command=go_to_website
        ).grid(row=i, column=1)

    window.mainloop()
