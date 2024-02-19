import re

import requests
from bs4 import BeautifulSoup

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}


# 根据url获取页面内容中指定的标题所对应的文章内容
def get_content(url):
    content_page = requests.get(url=url, headers=headers)
    content_page.encoding = 'utf-8'
    content_page = content_page.text
    soup = BeautifulSoup(content_page, 'lxml')
    div = soup.find('div', class_='chapter_content')
    return div.text


page_text = requests.get(url=url, headers=headers)
page_text.encoding = 'utf-8'
page_text = page_text.text

# 数据解析
soup = BeautifulSoup(page_text, 'lxml')
# a_list列表中存储的是一系列的a标签对象
a_list = soup.select('.book-mulu > ul > li > a')
# type(a_list[0])
# 注意：Tag类型的对象可以继续调用响应的解析属性和方法进行局部数据的解析

fp = open('./sanguo.txt', 'w', encoding='utf-8')
for a in a_list:
    # 获取了章节的标题
    title = a.string
    content_url = 'http://www.shicimingju.com' + a['href']
    print(content_url)
    # 获取章节的内容
    content = get_content(content_url)
    ## 清理前置 nbsp
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)
    fp.write(title + ':' + "\n" + content + "\n\n\n")
    print('写入一个章节内容')
