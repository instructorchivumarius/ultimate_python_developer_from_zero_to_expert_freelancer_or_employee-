# Project: Net Salary Calculator 

# (1) DEFINE VARIABLES
gross_salary = 5000
tax_rate = 0.20  # 20%

# (2) BASIC TAX CALCULATION
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount

# (3) ADD DEDUCTIONS
health_deduction = 200
pension_deduction = 300
net_salary = net_salary - health_deduction - pension_deduction

# (4) FORMAT AND DISPLAY FINAL RESULT (ASCII safe separators)
print("-------------")
print("NET SALARY CALCULATOR")
print("Gross Salary:        ", gross_salary)
print("Tax Rate:            ", tax_rate * 100, "%")
print("Tax Amount:          ", tax_amount)
print("Health Deduction:    ", health_deduction)
print("Pension Deduction:   ", pension_deduction)
print("-------------")
print("Final Net Salary:    ", net_salary, "RON")
print("-------------")
