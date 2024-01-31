# 常见的bug
# NameError: name 'a' is not defined (一般只变量名错误)
# 如果遇到此类错误,查看变量名是否被定义或者变量名是否书写错误
# print(a)

# ZeroDivisionError: division by zero (零不能做分母)
# a = 10
# print(a / 0)

# IndentationError: unexpected indent  (缩进错误)
# 修改缩进,或者去调整函数关系
# a = 5
#     b = 10

# SyntaxError: unexpected EOF while parsing (语法错误)
# 找到报错位置,查看语法是否存在问题,最好的办法就是将其进行格式化
# print(123

# TypeError: can only concatenate str (not "int") to str (数据类型错误)
# a = '123'
# print(a + 12)

# Process finished with exit code 0 程序结束后 正常退出 code 为 0
# print('hello world')

# Process finished with exit code 1  程序异常结束 code 为 1
# print(a)

