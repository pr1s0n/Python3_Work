# import requests
# from bs4 import BeautifulSoup
# import re

# headers = {
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	'Accept-Encoding': 'gzip, deflate, br',
# 	'Accept-Language': 'zh-CN,zh;q=0.9',
# 	'Cache-Control': 'max-age=0',
# 	'Connection': 'keep-alive',
# 	'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWM5M2VlMjM5NzJkNzdjODA3MWI4ZTgyNmJiNTI5NTkwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVZoeHRZVlhCVHVMTE1yMitoYUZDRFlZK3ZXeXhCT2Q4ZkpDU3lMeXk4Rkk9BjsARg%3D%3D--72df03ebec6b210db1f65964211f03f434050a8e; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1584453613; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1584455776',
# 	'Host': 'www.xicidaili.com',
# 	'If-None-Match': 'W/"1c01f45e78f603462a6fb7f86381c0a0"',
# 	'Sec-Fetch-Dest': 'document',
# 	'Sec-Fetch-Mode': 'navigate',
# 	'Sec-Fetch-Site': 'none',
# 	'Sec-Fetch-User': '?1',
# 	'Upgrade-Insecure-Requests': '1',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',

# }

# #代理存活验证
# def proxy_alive(proxy):
# 	try:
# 	    requests.get('http://baidu.com/robots.txt',proxies={"http":'{proxy}}'},timeout=6)
# 	except:
# 	    pass
# 	else:
# 	    print('{proxy} is success')

# for page in range(1,100):
# 	url = 'https://www.kuaidaili.com/free/intr/{}/'.format(page)
# 	html = requests.get(url,headers=headers).text
# 	soup = BeautifulSoup(html,'html.parser')
# 	res = soup.find_all('td')

# 	ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',str(res))
# 	port = re.findall(r'"PORT">(\d{3,5})',str(res))
# 	proxy = []
# 	for i in range(0,len(ips)):
# 		proxy.append(ips[i]+':'+port[i])
# 	for num in proxy: 

# 		with open('ip.txt','a+') as f:
# 			f.write(num+'\n')

		
# import base64
# font_face = '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'
# b = base64.b64decode(font_face)
# with open('font.ttf','wb') as f:
# 	f.write(b)

import requests
from bs4 import BeautifulSoup
import re
headers = {
	'cookie':'ZYM=k1dqqf7a6adr76nsdvj6k9jlh2'
}
url = 'https://d.chinacycc.com/index.php?m=Project&a=ym&id=18'
html = requests.get(url).text
print(html)