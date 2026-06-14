class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age
    print(name,age)

# a = Person("Divyaa",19)
# b = Person ("Viraj",13)

num = int(input("Enter the number of people you want to enter:"))

for i in range(num):
  name = input("Enter the name:")
  age = int(input("Enter age:"))
  f"a{i}" = Person(name,age)