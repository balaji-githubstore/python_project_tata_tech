class Employee1:
    company_name = None  # static variable or class variable
    __company_location = None
    __emp_id = None  #accessible within the class

    # non static variable or instance variable
    def __init__(o,id):
        o.__emp_id = None
        o.emp_name = None
        o.emp_salary = None

    # non-static methods
    def print_employee_details(self):
        print("Employee Id " + str(self.__emp_id))
        print("Employee Name " + self.emp_name)
        print("Employee Salary " + str(self.emp_salary))
        print("Company Name: " + Employee1.company_name)
        print("Company Location: " + Employee1.company_location)

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
