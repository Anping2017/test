
import requests        #导入requests包
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)

print(strhtml.text)