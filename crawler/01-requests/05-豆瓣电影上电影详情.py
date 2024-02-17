import requests

url = 'https://movie.douban.com/j/chart/top_list?'

# 封装ajax的get请求中携带的参数
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '100',
    'limit': '20'
}
# 自定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

response = requests.get(url=url, params=params, headers=headers)

print(response.text)
