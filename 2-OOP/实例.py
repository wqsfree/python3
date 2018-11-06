class A():
    name = "dana"
    age = 18

    #注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaaa"
        self,age = 200
# 此时，A称之为类实例
print(A.name)
print(A.age)

print("*" * 20)

# id可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))

print("*" * 20)
a = A()
print(A.__dict__)
print(a.__dict__)

a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

