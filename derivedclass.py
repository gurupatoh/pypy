class Person:
    def __init__(self,first_name,last_name,address):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
    # def print_name(self):
    #        print(f'{self.first_name} {self.last_name}{self.address}')
class Worker:
    def __init__(self,employment_date,employee_id,department,job_group):
       
        self.employee_id=employee_id
        self.department=department
        self.employment_date=employment_date
        self.job_group=job_group
    # def print_worker(self):
    #            print(f'{self.employment_date} {self.employee_id}{self.department}{self.job_group}')

class Employee2(Person,Worker):
    def __init__(self,first_name,last_name,address,employment_date,employee_id,department,job_group):
        super().__init__(first_name,last_name,address)
        self.employee_id=employee_id
        self.department=department
        self.employment_date=employment_date
        self.job_group=job_group
    def get_details(self):
        print(f'{self.first_name}{self.last_name}{self.employment_date} {self.employee_id} {self.address}{self.job_group}{self.department}')
          


    
kim = Employee2('Kim', 'White', '12/08/2020', 4556655, 567, 1121, 'Developer')
print(kim.get_details())


date=Date("december")
print(date.)