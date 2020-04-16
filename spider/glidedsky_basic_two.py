import requests
from bs4 import BeautifulSoup
import re
from lxml import etree
headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ga=GA1.2.1047866447.1584279043; _gid=GA1.2.997957767.1584279043; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1584279042,1584279080,1584351280,1584434850; footprints=eyJpdiI6Ill4ZXg5RU9ZNXBkWXd1WjRyVVRKYnc9PSIsInZhbHVlIjoiMCtUbFZWRGhPZWF6MElGOW9PV3c1Qk5RdjVwTU1DU1Nwa0RDSmRxZEhNTzU5NWZQb3U3Ynk0NkZBSWlTSDQwMSIsIm1hYyI6IjA1NDIyOWJlYWM3NjBjNjMyOGY3YThmZTJlMmMyZjhhZTcwZGJmNWJlNWQ2YzFjODJjODlhMTJmNjNiNzNjMzgifQ%3D%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjB4eUdHeUVXYWs0TGhKWlRXZ05ia1E9PSIsInZhbHVlIjoidHU0TjdKXC90TjQyMmMwMzBBbWJhR01qRkV0WDd3Q0F1TFNkdk9QeGt3ZG9DT2g5Y2JFbGkzZUh3V3M5Q3pcL3hXS1M2U2lGa3dxcmNkNlVHUEE3dXI4Z0VNMmhcLzczOTJtNWRialNnbHRDbjU2dzNNVUNcL3dNbG00MmdtSlpWYzFQOHhiNU93SHMweWtRcWtIXC9MSDJaXC9WWkdCRDRsc0ltYlhKM2h2ckpHRlRZPSIsIm1hYyI6IjhhNjUxNDQ2ZmEyNzI5NWEyYTRhYTllMzc3OTdmYzIzYWQ1ODMwMTc0MGUwNjk0ODAwZDY2YmQwN2MwNmE2ZjYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6InFjaUVKUHVhakdiQWlPbGVQdkVqUmc9PSIsInZhbHVlIjoia2tKUFNGOHMyVGpiNFJTZnd2YnFXeEpXWThnbzRBUnNkWnA2OVV4ZVZvbDhHNjZheTk5RENrNnVRNkhzczVQTCIsIm1hYyI6ImVmZWE5MjI4MTY5YmFjNjY5OThkYzkxM2RlYzlmYjBlMzM5OWU0Zjk5M2FlYmI3M2JiNmQzMDg0Y2NkYTE4MGYifQ%3D%3D; glidedsky_session=eyJpdiI6IlF6bTdpTnJqMmM5TnEybURnMUlhdEE9PSIsInZhbHVlIjoiUGV0XC9ndk00bnVIYU50eFNscmhqWEdCdERDM3dXSkg0aEE5MXpFQ25qb2JEeHg4UXY5MTF0YjBEbWdGbTdmOWQiLCJtYWMiOiI1M2MxMjMzMzY1MDk1NjdmNTJhNTY1ZDIzOWU4MGVmZTkzZGE1Zjg3YjA1MGQ1ZjFhZjVkZjUyNzdiNjQ5NDMzIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1584435986',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
# numberList=[]
# for i in range(1,1001,1):
# 	response = requests.get('http://www.glidedsky.com/level/web/crawler-basic-2?page={}'.format(i),headers=headers)
# 	responseEtree = etree.HTML(response.content)
# 	content = [int(x.replace('\n','').replace(' ','')) for x in responseEtree.xpath('//*[@id="app"]/main/div/div/div/div/div/text()')]
# 	print(content)
# 	numberList.append(sum(content))
# a = 0
# for number in numberList:
# 	a += number
# 	number+=1
# print(a)
a = 0
def connect(): 	
	url = 'http://www.glidedsky.com/level/web/crawler-basic-2?page={}'.format(page)
	html = requests.get(url,headers=headers).text
	response = BeautifulSoup(html,'html.parser')
	nums = response.find_all('div',class_='col-md-1')

	x = re.findall(r'\d\d+',str(nums))
	return x

for page in range(1,1001):
	x = connect()
	
	for i in x:
		a += int(i)

	print(page,x,a)
	
	page += 1
# print(connect())
print('采集完毕，最终数值为：%s' % a)