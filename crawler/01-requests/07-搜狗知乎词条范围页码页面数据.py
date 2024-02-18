# 前三页页面数据（1，2，3）
import os

import requests

# 创建一个文件夹
if not os.path.exists('./pages'):
    os.mkdir('./pages')

word = input('enter a word:')

# 动态指定页码的范围
start_pageNum = int(input('enter a start pageNum:'))
end_pageNum = int(input('enter a end pageNum:'))
# 自定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
# 1.指定url:设计成一个具有通用的url
url = 'https://zhihu.sogou.com/zhihu'
for page in range(start_pageNum, end_pageNum + 1):
    param = {
        'query': word,
        'page': page,
        'ie': 'utf-8'
    }
    response = requests.get(url=url, params=param, headers=headers)

    # 获取响应中的页面数据（指定页码（page））
    page_text = response.text

    # 进行持久化存储
    fileName = word + str(page) + '.html'
    filePath = 'pages/' + fileName
    with open(filePath, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
        print('第%d页数据写入成功' % page)
