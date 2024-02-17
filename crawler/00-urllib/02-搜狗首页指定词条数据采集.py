# 需求：爬取指定词条所对应的页面数据
"""
- 反爬机制：网站检查请求的UA，如果发现UA是爬虫程序，则拒绝提供网站数据。
- User-Agent(UA)：请求载体的身份标识.
- 反反爬机制：伪装爬虫程序请求的UA
"""

# 需求：爬取指定词条所对应的页面数据

import urllib.parse
import urllib.request

# 指定url
url = 'https://www.sogou.com/web?query='
# url特性：url不可以存在非ASCII编码的字符数据
word = urllib.parse.quote("人民币")
url += word  # 有效的url

# 发请求
response = urllib.request.urlopen(url=url)

# 获取页面数据
page_text = response.read()

with open('renminbi.html', 'wb') as fp:
    fp.write(page_text)
