import requests

url='http://music.baidu.com/playmv/554869244'
s=requests.session()
headers={'referer':'http://music.baidu.com/mv',
         'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
         }

r=s.get(url,headers=headers)
a=r.content.decode('UTF-8')

file_mp4=a.split('data.push')[1].split('file_link":"')[1].replace('"});','').replace(r"\\",r'').replace('\/','/').replace("\n",'').strip()

get_file=s.get(file_mp4)
f=open('data.mp4','wb')
f.write(get_file.content)
f.close()
