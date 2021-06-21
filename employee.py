class Employee:
      def __init__(self, first_name, last_name, employee_id):
    self.first_name = first_name
    self.last_name = last_name
    self.employee_id = employee_id
    self.base_salary = 0
  def set_base_salary(self, salary):
    self.base_salary = salary
class TeachingStaff (Employee):
  def __init__(self, first_name, last_name, employee_id, teaching_area, category):
    super().__init__(first_name, last_name, employee_id)
    self.teaching_area = teaching_area
    self.category = category
  def get_salary(self):
    salary = (((self.category * 10) + 100)/100) * self.base_salary
    return salary
  def get_staff_info(self):
    return 'First name: ' + self.first_name + \
    '\nLast name: ' + self.last_name + \
    '\nEmployee ID: ' + str(self.employee_id) + \
    '\nArea of Expertise: ' + self.teaching_area + \
    '\nCategory: ' + str(self.category) + \
    '\nSalary: ' + str(self.get_salary())
class AdministrativeStaff(Employee):
  def __init__(self, first_name, last_name, employee_id, level):
    super().__init__(first_name, last_name, employee_id)
    self.level = level

def get_salary(self):
  salary = (((self.level * 15) + 100)/100) * self.base_salary
  return salary
def get_staff_info(self):
  return 'First name: ' + self.first_name + \
  '\nLast name: ' + self.last_name + \
  '\nEmployee ID: ' + str(self.employee_id) + \
  '\nLevel: ' + str(self.level) + \
  '\nSalary: ' + str(self.get_salary())

