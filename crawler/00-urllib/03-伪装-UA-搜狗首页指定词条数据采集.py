"""
- 反爬机制：网站检查请求的UA，如果发现UA是爬虫程序，则拒绝提供网站数据。
- User-Agent(UA)：请求载体的身份标识.
- 反反爬机制：伪装爬虫程序请求的UA
"""

import urllib.parse
import urllib.request

# 指定url
url = 'https://www.sogou.com/web?query='
# url特性：url不可以存在非ASCII编码的字符数据
word = urllib.parse.quote("人民币")
url += word  # 有效的url

# UA伪装
# 1.子制定一个请求对象
headers = {
    # 存储任意的请求头信息
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

}
# 该请求对象的UA进行了成功的伪装
request = urllib.request.Request(url=url, headers=headers)

# 2.针对自制定的请求对象发起请求
response = urllib.request.urlopen(request)

# 获取页面数据
page_text = response.read()

with open('renminbi.html', 'wb') as fp:
    fp.write(page_text)
