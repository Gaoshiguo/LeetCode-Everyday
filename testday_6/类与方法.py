class Animal():#定义一个类，类名为animal，类中有方法run,该方法打印输出我是动物
    def run(self):
        print('I am an animal')
class Dog(Animal):#定义另外一个类，类名为dog，类中有方法eat，该方法打印输出我可以吃
    def eat(self):
        print('I can eat')
class Cat(Animal):
    pass#定义第三个类，该类继承类animal，同时也会继承animal中的方法，pass没有为cat类提供任何方法
dog = Dog()#为类dog提供实例化对象
dog.run()#调用Dog类中的run方法，该方法是继承来自Animal的run方法
dog.eat()#调用Dog类中的run方法，该方法是dog 类本身自己定义的
cat = Cat()#为类cat提供实例化对象
cat.run()#调用Cat类中的run方法，该方法来自继承Animal的类中的方法