import re

# 提取出python
key = "javapythonc++php"
key_ = re.findall('python', key)[0]
print(key_)

print("=====================================")

# 提取出hello world
key = "<html><h1>hello world<h1></html>"
h_key_ = re.findall('<h1>hello world<h1>', key)[0]
print(h_key_)

print("=====================================")

# 提取170
string = '我喜欢身高为170的女孩'
findall = re.findall('\d+', string)
print(findall)

print("=====================================")

# 提取出http://和https://
key = 'http://www.baidu.com and https://boob.com'
re_findall = re.findall('https{0,1}', key)
print(re_findall)

print("=====================================")

# 提取出hit.
key = 'bobo@hit.edu.com'
re_findalls = re.findall('h.*?\.', key)  # 贪婪模式：根据正则表达式尽可能多的提取出数据
print(re_findalls)

print("=====================================")

# 匹配sas和saas
key = 'saas and sas and saaas'
l = re.findall('sa{1,2}s', key)
print(l)

print("=====================================")

# 匹配出i开头的行   re.S(基于单行)  re.M（基于多行）
string = '''fall in love with you
i love you very much
i love she
i love her'''
findall1 = re.findall('^i.*', string, re.M)
print(findall1)

print("=====================================")

# 匹配全部行
string = """<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>"""
findall2 = re.findall('<div>.*</div>', string, re.S)

print(findall2)
