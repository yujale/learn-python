import requests

# 1.指定post请求的url
url = 'https://accounts.douban.com/login'

# 封装post请求的参数
data = {
    "source": "movie",
    "redir": "https://movie.douban.com/",
    "form_email": "15027900535",
    "form_password": "bobo@15027900535",
    "login": "登录",
}
# 自定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
# 2.发起post请求
response = requests.post(url=url, data=data, headers=headers)

# 3.获取响应对象中的页面数据
page_text = response.text

# 4.持久化操作
with open('./douban.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
