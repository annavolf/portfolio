#Tuple
test_result=("test login", "passed", "failed")
print(test_result[0])
print(f"test: {test_result[0]} has result {test_result[1]}")

#Set
data={"123","222","456","789","123","222","456","789"}
print(data)
data.add("999")
data.add(None)
print(data)
valid_data=set(filter(None, data))
print(valid_data)

salaries=(1000,100,5000,4000,2000,4567,12345,4566788,123,4567,12345,98765)
print("Salaries for the whole year:", salaries)
print("salary per year:", sum(salaries))
print("Salary for the fifth month:", salaries[4])
print("The biggest salary:", max(salaries))
print("The average salary:", sum(salaries)/len(salaries))

print("*"*50)

# Set operations
set1={'A','B','C','D'}
set2={'A','B','W','Z'}
print("Union of sets:", set1|set2)
print("Difference of set 1 to set 2:", set1-set2)
print("Difference of set 2 to set 1:", set2-set1)
print("Intersection of set 1 to set 2:", set1&set2)
from PythonPractice.functions import greeting, personal_greeting, return_greeting, tax

greeting()
personal_greeting("Anna")
print(return_greeting("Vanna"))
salary=456789
result=tax(salary)
print("The tax is", result)