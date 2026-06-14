class Student():
  def __init__(self, name, admission_no, cgpa):
    self.name = name
    self.admission_no = admission_no
    self.__cgpa = cgpa

  def get_cgpa(self):
    return self.__cgpa

  def set(self,cgpa):
    if cgpa < 0 or cgpa > 10:
      print("Invalid CGPA")
    else:
      self.__cgpa = cgpa

a1 = Student("assss",12345,6)
print(a1.__cgpa)