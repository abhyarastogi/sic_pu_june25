name = input('Enter name :')
emp_id = input('Enter employee ID :')
monthly_salary = float(input('Enter monthly salary :'))
monthly_special_allowance = float(input('Enter monthly special allowances :'))
bonus_percentage_annual = float(input('Enter annual bonnus percentage :'))
monthly_gross_salary = monthly_salary + monthly_special_allowance
annual_gross_salary = (monthly_gross_salary * 12)+((bonus_percentage_annual/100)*(monthly_gross_salary * 12))
print(('Name:{}\nEmployee ID:{}\nMonthly gross salary:{}\nAnnual gross salary:{}').format(name,emp_id,monthly_gross_salary,annual_gross_salary))