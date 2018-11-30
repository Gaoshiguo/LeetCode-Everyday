class Animal(object):#定义一个类，类名为animal，类中有方法run,该方法打印输出我是动物
    def run(self):
        print('I am an animal')
    def __private(self):#定义animal类中的一个私有方法__private(),这是一个私有方法，不可以随便调用
        print("我是animal类中的私有方法")
class Dog(Animal):#定义另外一个类，类名为dog，类中有方法eat，该方法打印输出我可以吃
    def eat(self):
        print('I can eat')
class Cat(Animal):
    def Mew(self):
        print("I can Mew!!!")

cat = Cat()#为类dog提供实例化对象
cat.run()#调用Dog类中的run方法，该方法是继承来自Animal的run方法
cat.Mew()#调用Cat类中的Mew方法，该方法是Cat类本身自己定义的
#cat.__private()#由于调用了私有方法，这一句会报错