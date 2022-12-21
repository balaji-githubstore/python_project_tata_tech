from employee_package.employee_module import Employee

Employee.company_name = "Tata Tech"
Employee.company_location = "Pune"

Employee.print_author_name()

emp1=Employee()

emp1.emp_id=101;
emp1.emp_name='john'


emp2=Employee(102,'peter',5000.2)

emp3=Employee(103,'balaji dinakaran','5000.2')

print(type(emp1))

print(emp2.emp_id)
print(emp2.emp_salary)
print(emp3.emp_id)

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()


name=emp2.get_employee_name()
print(name)

name=emp3.get_capitalize_employee_name
print(name)

print(emp3.get_capitalize_employee_name)

print(emp3.get_name)

emp1.print_employee_details()

print(emp1.get_name)
