#格式化输出
print('小刚说我今年%s岁' % '15')
print('圆周率的值是%s'%'3.1415926')
print('班级的平均分是%s'%'85.96321')
#字符串格式化元组
print('今年是%s年，%s开打了，今年的冠军队伍极有可能是%s队，他们夺冠的概率是%f'%('2018','NBA','spurs',75.263))
#符号、对齐和0填充
print('圆周率的值是%010.2f'%3.1415926)#010.2f代表的意思是输出十位数，结果保留两位
print('圆周率的值是%05.2f'%3.1415926)#05.2f代表的意思是输出五位数，结果保留两位
print('圆周率的值是%010.5f'%3.1415926)
print('圆周率的值是%-5.2f'%3.1415926)#-号代表左对齐，不写代表右对齐
print('%5d'%10+'\n'+'%5d'%-10)
print('%+5d'%10+'\n'+'%5d'%-10)
#字符串各种方法的使用
#1.find（）方法
s = 'I am a super man'
print(s.find('am'))
print(s.find('python'))#没有该字符返回-1
print(s.find('am',0,5))#后面两个参数代表提供起点和终点
#2.join（）方法
#num = [1,2,3,4,5,6]
#mark = "+"
#print(mark.join(num))
#print(num.join(mark))
#这两句都出错，是因为num定义list中的每一个参数都是整型的，而Mark定义的是字符串类型的
#不能直接将不同类型的参数连接
L = ['1','2','3','4','5']
print('+'.join(L))
#3.replace()方法
ini = 'just do it now, do right now'
print(ini.replace('do','just do'))
print(ini.replace('o','xxx',1))
print(ini.replace('o','xxx',2))
print(ini.replace('o','xxx',3))


