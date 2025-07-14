#1
income=int(input("Enter your income: "))
credit_score=int(input("Enter your credit score: "))

if income>=40000 and credit_score>=700:
    print("You are eligible to get a loan")
else:
    print("You are not eligible to get a loan")

#2
salary=int(input("Enter your salary: "))
if salary>100000:
    tax=salary*0.3
    print(f"Your tax is:{tax}")
elif 50000<salary<=100000:
    tax=salary*0.2
    print(f"Your tax is:{tax}")
else:
    tax=salary*0.1
    print(f"Your tax is:{tax}")

#3
experience=int(input("How many years of experience do you have?: "))
skills=input("List your skills: ")
if experience>=5 and "python" in skills.lower():
    print("You are shortlisted for the interview")
else:
    print("Sorry, see you next time")

#4
for fruit in ["apple", "banana", "orange", "strawberry"]:
    if fruit == "banana":
        continue
    print(fruit)

#5
count=0
while count<5:
    print(f"Count: {count}")
    count+=1

#6
monthly_expences=[1200, 1500, 800, 950, 1100, 1300, 1500, 1200, 1600, 1100, 1000, 1400]
total_expences=0
for expence in monthly_expences:
    total_expences+=expence
print("Total expences for the year:", total_expences)

#7
# Dictionary of employees and their respective salaries
employees = {
    "John": 5000,
    "Jane": 5500,
    "Jack": 6000
}
# Use a for loop to print the paycheck for each employee
for employee, salary in employees.items():
    print(f"Paycheck for {employee}: ${salary}")

#8
# List of employee salaries for the year
employee_salaries = [40000, 45000, 60000, 55000]

# Use a for loop to calculate and print the annual bonus for each employee
for index, salary in enumerate(employee_salaries):
    bonus = salary * 0.10  # Calculate 10% of the salary
    print(f"Employee {index + 1}: Annual Bonus = ${bonus:.2f}")

#9
sales_figures=[2000, 3500, 2500, 4500, 3000]
# Use a for loop to calculate and print the commission for each salesperson
for index, sales in enumerate(sales_figures):
    commission = sales * 0.05  # Calculate 5% of the sales
    print(f"Salesperson {index + 1}: Commission = ${commission:.2f}")

