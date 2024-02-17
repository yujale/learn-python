"""
### urllib
- python中自带的一个基于爬虫的模块。
- 作用：可以使用代码模拟浏览器发起请求。request  parse
- 使用流程：
    - 指定url
    - 发起请求
    - 获取页面数据
    - 持久化存储
"""

# 需求：爬取搜狗首页的页面数据

import urllib.request

#1.指定url
url = 'https://www.sogou.com/'

#2.发起请求:urlopen可以根据指定的url发起请求，切返回一个响应对象
response = urllib.request.urlopen(url=url)

#3.获取页面数据:read函数返回的就是响应对象中存储的页面数据(byte)
page_text = response.read()

#4.持久化存储
with open('./sougou.html','wb') as fp:
    fp.write(page_text)
    print('写入数据成功')
