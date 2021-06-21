class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_salary(self):
        salary = (((self.category * 10) + 100)/100) * self.base_salary
        return salary
    def get_job(self):
        return 'job' + self.job
class Teacher(Employee):
    def __init__(self,name,subject,salary):
        super().__init__(name,salary)
        self.subject=subject
    def teach(self,student):
        self.student=student
    def get_subject(self):
        return 'subject' + self.subject

class FireFighter(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def driveTruck(self,truck):
        self.truck=truck
    def useExtinguisher(self,extiguisher):
        self.exiguisher=extiguisher
    def sprayHose(self,hose):
        self.hose=hose
workers = [Teacher('Martha', 'Architecture', 105000), FireFighter('Pauly', 75000), FireFighter('Joe', 84000), Teacher('Linus', 'Programming', 105400)]
for t in workers:
    print(t)