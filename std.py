class Student:
  def __init__(self,name,marks,admission_no):
    self.name = name
    self.marks = marks
    self.admission_no = admission_no

  def states(self):
    return self.marks >= 60

  def show(self):
    print(f"student name is ")
  