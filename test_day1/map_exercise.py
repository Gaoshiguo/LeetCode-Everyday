#使用map函数对字符串首字母大写，其余字母小写
def upper_first(s):
    return s[0].upper()+s[1:].lower()#使用切片操作符将字符串第一个大写，所有的都变成小写
print(map(upper_first,['jax','lin','hsah']))#由于map函数返回的类型是iterators，不是list所以需要在前面加一个list强制转换类型
print(list(map(upper_first,['jax','lin','hsah'])))
#方法二：
def upper_first2(s):
    return s.capitalize()#使用现有的首字母大写函数
print(list(map(upper_first2,['his','hsh','jason'])))