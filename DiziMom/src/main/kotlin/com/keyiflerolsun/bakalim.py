# ! Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli    import konsol
from cloudscraper import CloudScraper
from parsel       import Selector
from re           import findall

oturum = CloudScraper()
istek  = oturum.get("https://www.dizimom.pro/kader-baglari-1-bolum-izle-fox-hd/")
secici = Selector(istek.text)
konsol.print(secici.css("div#vast iframe::attr(src)").get())

oturum.cookies.update({"wordpress_logged_in_94427965a200eb7dd292509ed2c7c018": "keyiflerolsun|1699733740|0JIZp47atdM5omDeHKtXggF9zuccfZvzTDiAowU7lmA|02b7bca0910b49d5d3d44ed24c2cf7181ecbd006ce747ddd7b824f07343a305f"})
istek  = oturum.get("https://www.dizimom.pro/kader-baglari-1-bolum-izle-fox-hd/")
secici = Selector(istek.text)
konsol.print(secici.css("div#vast iframe::attr(src)").get())

oturum.headers.update({"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"})
istek  = oturum.get("https://www.dizimom.pro/kader-baglari-1-bolum-izle-fox-hd/")
secici = Selector(istek.text)
konsol.print(secici.css("div#vast iframe::attr(src)").get())