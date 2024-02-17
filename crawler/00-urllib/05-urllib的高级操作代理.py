"""
1. 代理

      - 什么是代理：代理就是第三方代替本体处理相关事务。例如：生活中的代理：代购，中介，微商......

　　- 爬虫中为什么需要使用代理？

　　　  一些网站会有相应的反爬虫措施，例如很多网站会检测某一段时间某个 IP 的访问次数，如果访问频率太快以至于看起来不像正常访客，它可能就会会禁止这个 IP 的访问。所以我们需要设置一些代理 IP，每隔一段时间换一个代理 IP，就算 IP 被禁止，依然可以换个 IP 继续爬取。

　  - 代理的分类：

　　　　正向代理：代理客户端获取数据。正向代理是为了保护客户端防止被追究责任。

　　　　反向代理：代理服务器提供数据。反向代理是为了保护服务器或负责负载均衡。
"""

import urllib.parse
import urllib.request

# 1.创建处理器对象，在其内部封装代理ip和端口
handler = urllib.request.ProxyHandler(proxies={'http': '95.172.58.224:52608'})
# 2.创建opener对象，然后使用该对象发起一个请求
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)

# 使用opener对象发起请求，该请求对应的ip即为我们设置的代理ip
response = opener.open(request)

with open('./daili.html', 'wb') as fp:
    fp.write(response.read())
