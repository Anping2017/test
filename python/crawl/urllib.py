from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve


html = urlopen("https://www.baidu.com")
obj = bf(html.read(),'html.parser')

logo_pic_info = obj.find_all('img', class_="index-logo-src")
logo_url = "https:"+logo_pic_info[0]['src']
urlretrieve(logo_url,'logo.png')