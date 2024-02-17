import urllib.parse
import urllib.request

# 1.指定url
url = 'https://fanyi.baidu.com/sug'

# post请求携带的参数进行处理  流程：
# 1.将post请求参数封装到字典
data = {
    'kw': '西瓜'
}
headers = {
    # 存储任意的请求头信息
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
# 2.使用parse模块中的urlencode(返回值类型为str)进行编码处理
data = urllib.parse.urlencode(data)
# 3.将步骤2的编码结果转换成byte类型
data = data.encode()

request = urllib.request.Request(url=url, headers=headers, data=data)
# 2.发起post请求:urlopen函数的data参数表示的就是经过处理之后的post请求携带的参数
response = urllib.request.urlopen(request)

read = response.read()

print(read)
