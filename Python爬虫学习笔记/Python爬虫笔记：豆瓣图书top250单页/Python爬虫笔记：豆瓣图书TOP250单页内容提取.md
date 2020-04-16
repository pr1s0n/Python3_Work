##前言
上次我们通过glidedsky的第一关实现了获取到单页的数据，但是可能有些小伙伴会觉得只是获取到一些数字并不能直观的体现出Python爬虫的方便之处。
所以今天我跟大家分享一个小小的案例，这不是在家空闲时间比较多，又不想太过于颓废，于是我打算在豆瓣挑选一些评分比较高的书分享给大家。
当然手动筛选工作量太大了，所以我决定用python写一个爬虫，爬取豆瓣图书TOP250的简单数据，并整理成表格保存在本地。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-f22cdc084e6ca011.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###网页元素分析

因为上篇文章只讲了获取单页数据，所以这次我们的目标也是先获取一页数据。
这个页面本身比较干净，数据也很清晰，获取会比较方便一些。
还是先f12查看页面元素，确定所要获取的数据。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-14d6abc4e21bb812.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
通过审查元素可以看出所有数据特点：
```
书名包含在a标签中,
作者及出版社等信息保存在命名为pl的p标签中,并通过斜杠分割不同数据，
评分保存在class=allster_rums的span标签中，
评价人数在class='pl'的span标签中,
```
发现了吗?这些数据没有做任何加密，同时每一个数据标识各不相同，非常容易分辨。
这也是为什么很多人在初学爬虫时都会接触到爬取豆瓣top250例子的原因，因为数据内容有用，爬取难度相对较小。
这里还需要注意一个问题，就是这部分图书并不全是中文书籍，还有一部分是外文书，这就导致了他们之间有一个地方数据有差别：
![image.png](http://upload-images.jianshu.io/upload_images/7857598-4bd9f62527f51bbe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
外文书会多出一个译者名字，所以之后在保存数据到表格文件中时，需要特别注意。

####代码实现
在开始之前还是先明确一下程序执行流程：
- 访问网页
- 获取源代码
- 提取数据
- 分别保存到excel文件中
首先解决访问网页和获取源代码的问题：

```
import requests
from bs4 import BeautifulSoup
url = 'http://book.douban.com/top250?start='
headers = {
	'cookie':'你自己的cookie',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

response = requests.get(url,headers=headers).text
bs4 = BeautifulSoup(response,'html.parser')
print(bs4)
```
![image.png](http://upload-images.jianshu.io/upload_images/7857598-1d8a52ac92430301.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

获取到之后当然就是对数据进行提取
```
bookName = bs4.find_all('div',class_='pl2')
for book in bookName:
	name = book.find('a')
	name = name.text.strip()
	name = name.replace(' ','')
	print(name)
```
这段代码首先在获取到的html文本中寻找Class=pl2的div元素
![image.png](http://upload-images.jianshu.io/upload_images/7857598-9120fb303ce7d6e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这是没有提取a标签中书名时的原始数据
**find_all()**是BeautifulSoup模块提供的一个用来快速查询数据的方法，返回一个列表。
所以我们下面使用for循环遍历出所有找到的数据。
从上面的图片中可以看到，只匹配div元素的话会有很多干扰数据，我们此时只想要一个书名，也就是a标签的文本信息。
所以我们还需要在列表中使用find()方法匹配到a标签的内容，然后使用strip方法去除两边空格，使用replace方法将文本中多余的空格替换为空，最终可以得到：
![image.png](http://upload-images.jianshu.io/upload_images/7857598-8a459851932b241c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

获取到数据之后，我们希望能够把它存放到excel文件中的话需要用到一个外部库**xlwt**
![image.png](http://upload-images.jianshu.io/upload_images/7857598-db42ee00d32eb14a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
使用pip命令安装xlwt(因为我的电脑中同时安装了py2和py3，所以将pip的版本进行了区分，只有一个python的话直接用pip即可)
然后使用 `import xlwt`在程序中引入该模块。
```
wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet')
ws.write(0,0,'书名')
ws.write(0,1,'出版信息')
ws.write(0,2,'评价人数')
ws.write(0,3,'评级')
wb.save('doubanTest.xls')
```
首先实例化workbook()对象，然后调用了add_sheet()方法为这个excel文件新建一个表
![image.png](http://upload-images.jianshu.io/upload_images/7857598-d3073d9ba7b2898e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
关于这个add_sheet()方法，前面说过python调用的外部模块保存在**Python安装目录\Lib\site-packages\**下,所以我们可以在这个目录下找到Workbook类文件，从这里面查看add_sheet()的具体实现方法以及主要参数。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-1a617260dc64c984.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
注意这段代码中引入Worksheet这个文件，本文中主要用到的是Worksheet中的write()方法，即将数据保存到表格文件中。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-ce82465844fb88b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
在Worksheet.py中找到write函数，注释给的非常详细，r和c分别是row和column的缩写，表示从0开始的行和列。
label参数默认为空，表示数据。
这样一来上述代码就通了，表示在第一行从第一列开始分别添加标题。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-6773961c18193942.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
所有东西都设置好了之后就是保存这个文件，使用Workbook中的save()方法
![image.png](http://upload-images.jianshu.io/upload_images/7857598-148620dd56b61427.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
传入一个文件名即可。
这块啰嗦了一点，主要还是希望大家能够养成多看引入模块源文件的习惯。
其他数据的获取其实和获取书名类似
**获取作者及出版信息**
```
i = 1
j = 1
k = 1
l = 1
authors = bs4.find_all('p',class_='pl')
for author in authors:
	anthor = author.text
	ws.write(j,1,author)
	j+=1
	print(author)
```
**获取评分及评价人数**
```
rating_nums = bs4.find_all('div',class_='star clearfix')
for rating in rating_nums:
	star = rating.find_all('span')
	reg = '\d+'
	vote = re.findall(reg,star[2].text)
	ws.write(k,2,vote)
	ws.write(l,3,star[1].text)
	k+=1
	l+=1
wb.save('doubanTest.xls')
```
ijkl分别代表的是不同的行数，作用在于换行时使用。
这里还有一点需要注意的地方，在获取评分及评价人数时，因为两个数据在同一个div下保存，而且是同级别的span标签并列表示的。
所以使用find_all()方法获取到全部span标签内容后可以使用下标的方式查询到不同的数据。
![image.png](http://upload-images.jianshu.io/upload_images/7857598-d7e15ebe6b2b1f8b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
至此，我们的程序就大功告成了，运行后会在该目录下生成一个douban.xls文件
![](http://upload-images.jianshu.io/upload_images/7857598-3f7df9852e8270bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
如果出现这种错误
![image.png](http://upload-images.jianshu.io/upload_images/7857598-840ed738f4edf811.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
说明你之前已经生成了一个doubanTest.xls文件而且没有关闭它。
解决办法是更改生成的文件名或者将原文件关闭。
