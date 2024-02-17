import requests

# 指定url
url = 'https://www.sogou.com/'

# 发起get请求:get方法会返回请求成功的相应对象
response = requests.get(url=url)

# 获取响应中的数据值:text可以获取响应对象中字符串形式的页面数据
page_data = response.text

print(page_data)

# 持久化操作
with open('./sougou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_data)
