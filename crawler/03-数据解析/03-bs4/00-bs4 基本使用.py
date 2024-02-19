"""
- 环境安装：
- 需要将pip源设置为国内源，阿里源、豆瓣源、网易源等
   - windows
    （1）打开文件资源管理器(文件夹地址栏中)
    （2）地址栏上面输入 %appdata%
    （3）在这里面新建一个文件夹  pip
    （4）在pip文件夹里面新建一个文件叫做  pip.ini ,内容写如下即可
        [global]
        timeout = 6000
        index-url = https://mirrors.aliyun.com/pypi/simple/
        trusted-host = mirrors.aliyun.com
   - linux
    （1）cd ~
    （2）mkdir ~/.pip
    （3）vi ~/.pip/pip.conf
    （4）编辑内容，和windows一模一样
- 需要安装：pip install bs4
     bs4在使用时候需要一个第三方库，把这个库也安装一下
     pip install lxml

     - 代码的使用流程：
    核心思想：将html文档转换成Beautiful对象，然后调用该对象中的属性和方法进行html文档指定内容的定位查找。
    导包：from bs4 import BeautifulSoup
    创建Beautiful对象：
        - 如果html文档的来源是来源于本地：
        Beautiful（'open('本地的html文件')','lxml'）
        - 如果html是来源于网络
        Beautiful（‘网络请求到的页面数据’，‘lxml’）

- 属性和方法：
（1）根据标签名查找
        - soup.a   只能找到第一个符合要求的标签
    （2）获取属性
        - soup.a.attrs  获取a所有的属性和属性值，返回一个字典
        - soup.a.attrs['href']   获取href属性
        - soup.a['href']   也可简写为这种形式
    （3）获取内容
        - soup.a.string   /text()
        - soup.a.text   //text()
        - soup.a.get_text()  //text()
       【注意】如果标签还有标签，那么string获取到的结果为None，而其它两个，可以获取文本内容
    （4）find：找到第一个符合要求的标签
        - soup.find('a')  找到第一个符合要求的
        - soup.find('a', title="xxx")
        - soup.find('a', alt="xxx")
        - soup.find('a', class_="xxx")
        - soup.find('a', id="xxx")
    （5）find_All：找到所有符合要求的标签
        - soup.find_All('a')
        - soup.find_All(['a','b']) 找到所有的a和b标签
        - soup.find_All('a', limit=2)  限制前两个
    （6）根据选择器选择指定的内容
               select:soup.select('#feng')
        - 常见的选择器：标签选择器(a)、类选择器(.)、id选择器(#)、层级选择器
            - 层级选择器：
                div .dudu #lala .meme .xixi  下面好多级  div//img
                div > p > a > .lala          只能是下面一级  div/img
        【注意】select选择器返回永远是列表，需要通过下标提取指定的对象
"""

from bs4 import BeautifulSoup

fp = open('text.html')
soup = BeautifulSoup(fp, 'lxml')
# 根据标签名进行查找
# soup.div

# 获取标签属性值
# soup.a['href']

# 获取内容
# soup.p.string

# soup.find('div',class_="tang")
# soup.findAll('a',limit=2)

# select函数的层级选择器：
soup.select('div li')
