"""
   - cookie 概念：当用户通过浏览器首次访问一个域名时，访问的 web 服务器会给客户端发送数据，以保持 web 服务器与客户端之间的状态保持，这些数据就是 cookie。

        - cookie 作用：我们在浏览器中，经常涉及到数据的交换，比如你登录邮箱，登录一个页面。我们经常会在此时设置 30 天内记住我，或者自动登录选项。那么它们是怎么记录信息的呢，答案就是今天的主角 cookie 了，Cookie 是由 HTTP 服务器设置的，保存在浏览器中，但 HTTP 协议是一种无状态协议，在数据交换完毕后，服务器端和客户端的链接就会关闭，每次交换数据都需要建立新的链接。就像我们去超市买东西，没有积分卡的情况下，我们买完东西之后，超市没有我们的任何消费信息，但我们办了积分卡之后，超市就有了我们的消费信息。cookie 就像是积分卡，可以保存积分，商品就是我们的信息，超市的系统就像服务器后台，http 协议就是交易的过程。

        - 经过 cookie 的相关介绍，其实你已经知道了为什么上述案例中爬取到的不是张三个人信息页，而是登录页面。那应该如何抓取到张三的个人信息页呢？

　　思路：

　　　　1. 我们需要使用爬虫程序对人人网的登录时的请求进行一次抓取，获取请求中的 cookie 数据

　　　　2. 在使用个人信息页的 url 进行请求时，该请求需要携带 1 中的 cookie，只有携带了 cookie 后，服务器才可识别这次请求的用户信息，方可响应回指定的用户信息页数据

cookiejar对象：
    - 作用：自动保存请求中的cookie数据信息
    - 注意：必须和handler和opener一起使用
cookiejar使用流程：
    - 创建一个cookiejar对象
      import http.cookiejar
      cj = http.cookiejar.CookieJar()
    - 通过cookiejar创建一个handler
      handler = urllib.request.HTTPCookieProcessor(cj)
    - 根据handler创建一个opener
      opener = urllib.request.build_opener(handler)
    - 使用opener.open方法去发送请求，且将响应中的cookie存储到openner对象中，后续的请求如果使用openner发起，则请求中就会携带了cookie
"""

import http.cookiejar
import urllib.parse
# 使用cookiejar实现人人网的登陆
import urllib.request

cj = http.cookiejar.CookieJar()  # 请求中的cookie会自动存储到cj对象中
# 创建处理器对象(携带cookiejar对象的)
handler = urllib.request.HTTPCookieProcessor(cj)
# 创建opener对象 （携带cookiejar对象）
opener = urllib.request.build_opener(handler)

# 要让cookiejar获取请求中的cookie数据值
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201873958471'
# 自定义一个请求对象，让该对象作为opener的open函数中的参数
data = {
    "email": "www.zhangbowudi@qq.com",
    "icode": "",
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": "1",
    "captcha_type": "web_login",
    "password": "40dc65b82edd06d064b54a0fc6d202d8a58c4cb3d2942062f0f7dd128511fb9b",
    "rkey": "41b44b0d062d3ca23119bc8b58983104",

    'f': "https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DpPKf2680yRLbbZMVdntJpyPGwrSk2BtpKlEaAuKFTsW%26wd%3D%26eqid%3Deee20f380002988c000000025b7cbb80"
}
data = urllib.parse.urlencode(data).encode()
request = urllib.request.Request(url, data=data)
opener.open(request)

# 获取当前用户的二级子页面
s_url = 'http://www.renren.com/289676607/profile'
# 该次请求中就携带了cookie
resonse = opener.open(s_url)

with open('./renren.html', 'wb') as fp:
    fp.write(resonse.read())
