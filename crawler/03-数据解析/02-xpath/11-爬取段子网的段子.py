import os

import requests
from lxml import etree

dirName = 'duanzi'
# 如果文件夹不存在，则新建，否则不新建
if not os.path.exists(dirName):
    os.mkdir(dirName)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
# 创建一个通用的url:除了第一页其他页码的通用url
url = 'https://www.xiaohua.com/duanzi?page=%d'
fp = open('./duanzi.txt', 'w', encoding='utf-8')

for page in range(1, 6):
    new_url = format(url % page)

    print('----------正在请求下载第%d页的段子数据----------' % page)
    response = requests.get(url=new_url, headers=headers)
    response.encoding = 'utf-8'
    result = response.text
    tree = etree.HTML(result)  # HTML()专门用来解析网络请求到的页面源码数据
    div_list = tree.xpath('//div[@class="content-left"]/div')
    # 注意：Element类型的对象可以继续调用xpath函数，对该对象表示的局部内容进行指定内容的解析
    for div in div_list:
        div_content = div.xpath('./p/a/text()')
        if len(div_content) == 0:
            continue
        div_content = div_content[0]
        fp.write(div_content + "\n\n")
        print('数据写入成功')
