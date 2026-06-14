class Rectangle:

  def area(self,height,width):
    self.height = height
    self.width = width
    area = height * width
    print(f"The height of the rectangle is {height} and the width is {width} and the area is {area}.")

a = Rectangle()
a.area(12,32)