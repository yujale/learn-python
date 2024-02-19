import os

import requests
from lxml import etree

dirName = 'girls'
# 如果文件夹不存在，则新建，否则不新建
if not os.path.exists(dirName):
    os.mkdir(dirName)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
# 创建一个通用的url:除了第一页其他页码的通用url
url = 'https://616pic.com/tupian/fanye_%d.html'
for page in range(1, 6):
    if page == 1:
        new_url = 'https://616pic.com/tupian/fanye.html'
    else:
        new_url = format(url % page)
    print('----------正在请求下载第%d页的图片数据----------' % page)
    response = requests.get(url=new_url, headers=headers)
    response.encoding = 'utf-8'
    result = response.text

    # 数据解析：图片地址+图片名称
    tree = etree.HTML(result)  # HTML()专门用来解析网络请求到的页面源码数据
    # 该列表中存储的是每一个 div 标签
    # 直接读取图片内容
    # img_list = tree.xpath('//img[@class="lazy"]')
    # for img in img_list:
    #     # 局部解析：将 标签中指定的内容解析出来
    #     xpath = img.xpath('./@data-original')
    #
    #     img_src ='https:'+xpath[0]
    #     img_data = requests.get(url=img_src, headers=headers).content
    #     jpg_ = random.choice('1234567890') + '.jpg'
    #     img_path = dirName + '/' + jpg_
    #     print(img_path)
    #     with open(img_path, 'wb') as fp:
    #         fp.write(img_data)
    #     print(jpg_, '下载保存成功！')

    # 通过读取图片上层的div标签，再读取img标签
    div_list = tree.xpath('//div[@class="box two grid-v"]')
    for div in div_list:
        img = div.xpath('./a[1]/img/@data-original')[0]
        img_src = 'https:' + img
        img_title = div.xpath('./a[2]/text()')[0] + '.jpg'

        img_data = requests.get(url=img_src, headers=headers).content
        img_path = dirName + '/' + img_title
        print(img_path)
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(img_title, '下载保存成功！')
