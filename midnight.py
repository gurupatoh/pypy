import abc
class paidEmployee(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def get_salary(self):
      pass
   def get_staff_info(self):
       pass
class TeachingStaff (paidEmployee):
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
class AdministrativeStaff(paidEmployee):
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



