import os
import re

import requests

url = 'https://616pic.com/tupian/fanye.html'

# 发
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers)
# 获取页面数据
page_text = response.text
print(page_text)

# ex = '<LI>.*?<IMG.*?src="(.*?)" style.*?</LI>'
# img_src_list = re.findall(ex,page_text,re.S)
# 问题：提取到的图片地址都是一样的。如何解决？继续查看抓包工具的源码
# 发现：真正的图片地址是有js动态加载出来的
# ex = '<script.*?src = "(.*?)"; </script>'
# img_src_list = re.findall(ex,page_text,re.S)
# #发现解析出的图片地址，是不完整的，缺少http:
# for img_src in img_src_list:
#     img_src = 'http:'+img_src
#     # print(img_src)
#     img_name = img_src.split('/')[-1]
#     request.urlretrieve(img_src,img_name)
#     print(img_name,'下载成功！')

ex = r'<div class="box two grid-v"><a class="img img-ys"><img data-original="(.*?)".*?</div>'
img_src_list = re.findall(ex, page_text, re.S)
print(img_src_list)

# 数据解析(该列表中存储的就是当前页面源码中所有的图片链接)
# img_list = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', page_text, re.S)
# 创建一个存储图片数据的文件夹
if not os.path.exists('./imgs'):
    os.mkdir('imgs')
for url in img_src_list:
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
