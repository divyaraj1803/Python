class Car:
  brand = "BMW"
  speed = "300 km/hr"

  @classmethod
  def display_class(cls):
    print(f"The brand of the car is {cls.brand} and its top speed is {cls.speed}.")

  def display(self):
    print(f"The brand of the car is {self.brand} and its top speed is {self.speed}.")


  
Car.display_class()
a = Car()
a.brand = "merced"
a.speed = "350 km/hr"
a.display()