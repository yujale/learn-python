import requests
from lxml import etree

"""
### 代理操作：
    - 1.代理：第三方代理本体执行相关的事物。生活：代购，微商，中介
    - 2.为什么要使用代理？
        - 反爬操作。
        - 反反爬手段
    - 3.分类：
        - 正向代理：代替客户端获取数据
        - 反向代理：代理服务器端提供数据
    - 4.免费代理ip的网站提供商：
        - www.goubanjia.com
        - 快代理
        - 西祠代理
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
url = "https://ip.900cha.com/"

# proxies = {"代理类型": "ip:port"}
proxies = {"https": "49.89.126.72:4231"}
result = requests.get(url=url, headers=headers, proxies=proxies).text
tree = etree.HTML(result)
li = tree.xpath('//*[@class="list-unstyled"]/li[1]/text()')[0]
print(li)
