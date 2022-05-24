from bs4 import BeautifulSoup as bs
import cloudscraper as cs
import requests as rq
import shutil

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
O = a[:12]
location = "#enter location"
scr = cs.create_scraper()
for i in O:
    for j in O:
        for k in O:
            for l in O:
                for m in O:
                    for n in O:
                        combo = i + j + k + l + m + n
                        lnk = "https://prnt.sc/" + combo
                        link = scr.get(lnk).text
                        soup = bs(link, features="html.parser")

                        for img in soup.findAll('img'):
                            image = (img.get('src'))
                            break
                        print(image)
                        try:
                            r = rq.get(image, stream=True)
                        except:
                            continue
                        r.raw.decode_content = True
                        filete = location + combo + '.jpg'
                        f = open(filete, 'wb')

                        shutil.copyfileobj(r.raw, f)

