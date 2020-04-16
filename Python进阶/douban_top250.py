
#多线程与多进程
import requests
import concurrent.futures
header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
def request_douban(url):
	try:
		response = requests.get(url,headers=header)
		if response.status_code == 200:

			print(f'爬取了{url},数据量：{len(response.content)}')
			return response.content
	except requests.RequestException:
		return None

def main(page):
	url = 'https://movie.douban.com/top250?start=' + str(page + 25) + '&filter='
	print(url)
	html = request_douban(url)
	print(f'通过{url} : 爬取了{len(html)} 数据量 ')

if __name__ == '__main__':
	urls = ['https://movie.douban.com/top250?start=' + str(i * 25) + '&filter=' for i in range(0,10)]
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
		executor.map(request_douban,urls)


