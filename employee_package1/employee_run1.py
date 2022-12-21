from employee_package1.employee_module import Employee1

e=Employee1()
# e1=Employee1(101)
e.emp_name="s"
e.emp_id=1
e.emp_salary=33

Employee1.company_name="33"
Employee1.company_location="pp"

print(e)

e.print_employee_details()
# e1.print_employee_details()