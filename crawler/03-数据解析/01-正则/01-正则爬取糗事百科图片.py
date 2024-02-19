import os
import re

import requests

"""
已关闭
"""
# 指定url
url = 'https://www.qiushibaike.com/pic/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
# 发起请求
response = requests.get(url=url, headers=headers)

# 获取页面数据
page_text = response.text
print(page_text)

# 数据解析(该列表中存储的就是当前页面源码中所有的图片链接)
img_list = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', page_text, re.S)

# 创建一个存储图片数据的文件夹
if not os.path.exists('./imgs'):
    os.mkdir('imgs')
for url in img_list:
    # 将图片的url进行拼接，拼接成一个完成的url
    img_url = 'https:' + url
    # 持久化存储：存储的是图片的数据，并不是url。
    # 获取图片二进制的数据值
    img_data = requests.get(url=img_url, headers=headers).content
    imgName = url.split('/')[-1]
    imgPath = 'imgs/' + imgName
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
        print(imgName + '写入成功')
