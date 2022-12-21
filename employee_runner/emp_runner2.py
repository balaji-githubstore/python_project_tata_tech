from employee_package import employee_module

employee_module.Employee.company_name="CCC"
employee_module.Employee.company_location="ch"

e1=employee_module.Employee(1001,"balaji dinakaran",5600)

e1.print_employee_details()

print(e1.get_name)

