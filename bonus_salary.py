import sys

if len(sys.argv)==2:
    name=sys.argv[0]
    salary=sys.argv[1]

else:
    salary=100000


bonus=0.1*float(salary)

total_salary=float(salary)+bonus





print("Base Salary: ", salary)  
print("Bonus: ", bonus)
print("Total Salary: ", total_salary)
