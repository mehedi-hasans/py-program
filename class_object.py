# class MyClass:
#   x = 5
# print(MyClass)


# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)


# class MyClass:
#     x = 10
# print(MyClass.x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
