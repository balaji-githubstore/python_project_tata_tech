class Employee:
    company_name = None  # static variable or class variable
    company_location = None

    def __init__(self,id=None,name=None,salary=None):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary

    # def __init__(self,a=None,b=None,c=None):
    #     self.emp_id = a
    #     self.emp_name = b
    #     self.emp_salary = c

    # non-static methods
    def print_employee_details(self):
        print("Employee Id " + str(self.emp_id))
        print("Employee Name " + self.emp_name)
        print("Employee Salary " + str(self.emp_salary))
        print("Company Name: " + Employee.company_name)
        print("Company Location: " + Employee.company_location)

    @staticmethod
    def print_author_name():
        print("Balaji Dinakaran")

    def get_employee_name(self):
        return str(self.emp_name).upper()

    @property
    def get_capitalize_employee_name(self):
        return str(self.emp_name).capitalize()

    @property
    def get_capitalize_employee_name(self):
        return str(self.emp_name).capitalize()

    @property
    def get_name(self):
        list = self.emp_name.split(" ")
        return list[0].title() + list[1].title()