import requests

from bs4 import BeautifulSoup
import re

url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
headers = {
	'cookie':'_ga=GA1.2.1047866447.1584279043; _gid=GA1.2.112214196.1584715175; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1584434850,1584532700,1584715175,1584761669; footprints=eyJpdiI6IlNLQXVQXC9jelIybFQ3UkorTURtNFV3PT0iLCJ2YWx1ZSI6InlnSm92R2VzRDJzUkxmXC9Gc0VhSnlYMEwyR1krbzBHT2VUdXJSOTdNMUxEWUYwaEZQT2trR1htMWR3bWxlQ1VQIiwibWFjIjoiMDhlNDBmMGM3MjAwY2JjOTY5ZWVhNmRmMTEyZjdiOTU0ZTZhN2NlZjEzNmJmOGYxODY4NzNmMGY1MzE2MWY0NCJ9; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IkRQamRcL2MyMWV0bHZoVUdKZytzRk5BPT0iLCJ2YWx1ZSI6ImpmMXRBSnlOMGpFVW9VR0VqbzRWWkI1QWZ1VnM3bW05YUllYXVkUFAzXC9HSjM2UXhtXC84bVJOY2hKQ3BiQUNUXC8iLCJtYWMiOiIyZTViZDY3NDk3MjZhZjE0NmY2MmE4OThhN2VlZWQ5OGEwNzY5ODQ4MzdmODYzOTE5ODBjYjBmYjkyNGU3ZTkyIn0%3D; glidedsky_session=eyJpdiI6IkRYd1l6aExjZnBuVGlKaHg4Z2FrZVE9PSIsInZhbHVlIjoiOGt3cmxqbDJuclpcL3ZCYzNBejNkQ3laNzI2clZkZ3BHc055c25MaFdnZHFQRFh3RlZyTGQwbmZVSEIyQWJuSlQiLCJtYWMiOiIzY2E3MTQ5N2I0NzQyZGIxM2MxYjA3MTdhODY2YThjYWQwYWE1YmMzNzMxOWY1OTczM2Q2NWYzY2I5ZmQwODE1In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1584776583'
}
html = requests.get(url,headers=headers,timeout=10).text
soup = BeautifulSoup(html,'html.parser')

nums = soup.find_all('div',class_='col-md-1')
x = re.findall(r'\d\d\d',str(nums),re.DOTALL)
print(x)
a = 0
for i in x:
	a += int(i.strip())


print('采集完毕，结果为：%s' % a)