# Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.

class Employee:
    def __init__(self, first, last, annual_salary_pa):
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary_pa
    def give_raise(self, fw_raise= 5000):
        
        self.annual_salary = self.annual_salary + fw_raise
        return self.annual_salary
        


