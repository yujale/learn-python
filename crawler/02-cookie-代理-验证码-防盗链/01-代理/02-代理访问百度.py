import requests

url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

# 将代理ip封装到字典
proxy = {
    'http': '77.73.69.120:3128'
}
# 更换网路IP
response = requests.get(url=url, proxies=proxy, headers=headers)

with open('./daili.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
