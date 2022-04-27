# this is a  project fot school
# we create a emploee class and we do a lot of inheritance


class Company():
  def __init__(self, employee_name, id):
    self.employee_name = employee_name
    self.id = id
  def display(self):
    return ("Name: " + self.employee_name+ " ID: " + str(self.id))
emp1 = Employee("John Smith", 124451421)
print(emp1.display())
class Engineer(Company):
  def __init__(self, emp, salary):
    super().__init__(emp.employee_name, emp.id)
    self.salary = salary
  def display(self):
    
    print(super().display() + "Salary: " + str(self.salary))
Engineer_Department = 
