import requests
import xlwt
from bs4 import BeautifulSoup
import re
url = 'https://book.douban.com/top250?start='
headers = {
	'cookie':'bid=hcpZmNQ6ThI; gr_user_id=fce124de-1523-4c74-98b8-65298282f0a8; _vwo_uuid_v2=D6D0D7E645A043EEB278B6496C6718951|9b4f5cf03b7df965b0e2ce4c87ac459b; ll="118250"; __utmz=81379588.1584849225.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="34938311"; __utmz=30149280.1584888840.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1585230477%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJG896dwklO5zMj6N80xxtXA7CPKZJ4zpFPes4YD3TcY3rgNqVeQ-WwWW-X6EO41fvsVskDbDcIfnEzv3BJk24K%26wd%3D%26eqid%3Dcaca8138000251e0000000035e76e142%22%5D; ap_v=0,6.0; __utma=30149280.737193083.1584849225.1584888840.1585230477.3; __utmc=30149280; __utma=81379588.1201485312.1584849225.1584849225.1585230477.2; __utmc=81379588; _pk_id.100001.3ac3=16f29b49a1467d21.1584849225.2.1585230480.1584849234.',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet')
ws.write(0,0,'书名')
ws.write(0,1,'出版信息')
ws.write(0,2,'评价人数')
ws.write(0,3,'评级')


response = requests.get(url,headers=headers).text
bs4 = BeautifulSoup(response,'html.parser')
bookName = bs4.find_all('div',class_='pl2')
i = 1
j = 1
k = 1
l = 1
for book in bookName:
	name = book.find('a')
	name = name.text.strip()
	name = name.replace(' ','')
	ws.write(i,0,name)
	i+=1
	print(name)

authors = bs4.find_all('p',class_='pl')
for author in authors:
	author = author.text
	ws.write(j,1,author)
	j+=1
	print(author)

rating_nums = bs4.find_all('div',class_='star clearfix')
for rating in rating_nums:
	star = rating.find_all('span')
	reg = '\d+'
	vote = re.findall(reg,star[2].text)
	ws.write(k,2,vote)
	# print(vote)
	# print(star[1].text)
	ws.write(l,3,star[1].text)
	k+=1
	l+=1
wb.save('doubanTest.xls')