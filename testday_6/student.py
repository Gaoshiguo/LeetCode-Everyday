class Student(object):
    def __init__(self,name,score):#定义一个构造方法，_init_,该方法可以在实例化时
        #传入参数
        self.name = name
        self.score = score
    def print(self):
        print(f'学生：{self.name};\n分数：{self.score}')
student = Student("詹姆斯","98")#实例化，并传入两个参数
print("更改前的数据为：")
student.print()#调用方法print，打印输出第一次初始赋值的参数值
student.score = 88#重新为参数赋值
print("更改后的数据为：")
student.print()#打印输出更改后的参数值