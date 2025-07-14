from PythonPractice.functions import experience_check

salaries=(3000, 3200, 3100, 3050, 3400, 3300, 3000, 3250, 3100, 3300, 3400, 3500)
print("Salaries for the year:",salaries)
print("Salary for the 5th month:", salaries[4])
print("Total salary for the year:",sum(salaries))
print("*"*50)
employees=(('John', 5000), ('Jane', 5500), ('Jack', 6000))
print("Employee names and salary:",employees)
# Access and print Jane's salary
for employee in employees:
    if employee[0] == 'Jane':
        print(f"Jane's Salary: {employee[1]}")
# Find the employee with the highest salary
highest_salary = max(employees, key=lambda x: x[1])
print(f"Employee with the highest salary: {highest_salary[0]}, Salary: {highest_salary[1]}")
print("*"*50)
skills = {'Python', 'SQL', 'Java', 'Python', 'C++', 'SQL'}
print("Set of skills:", skills)
skills.add('Postman')
print("The updated set of skills:", skills)
print("*"*50)
sales = {2000, 3000, 2500, 4500, 3000}
print("Sales are:", sales)
print("Total sales:", sum(sales))
print("*"*50)
wages=(3500, 4000, 4500, 3200, 3800)
print("all the wages:", wages)
print("Minimum wage:", min(wages), "Maximum wage:", max(wages))
print("*"*50)

experience_check(5)
