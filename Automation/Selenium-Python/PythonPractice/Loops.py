# For Loops

total=0
for i in range(0,10):
    total=total+i
    #total+=1
    print(f"the total for each step is: {total}")
print(f"the total is: {total}")

#While Loops

total=0
i=0
while i<10:
    total=total+i
    i=i+1
    print(f"the total for each step is: {total}")
print(f"the total is: {total}")

# For Loop with even numbers

total=0
for i in range(0,10,2):
    total=total+i
    #total+=1
    print(f"the total for each step is: {total}")
print(f"the total is: {total}")

for i in range(1,6):
    if i==3:
        print(f"stop and break when i=3")
        break
    print(i)

prices=[1,2,3,4,5,6,7,8,9,43,56,77,100]
# create a list with only even prices
even_prices=[]
odd_prices=[]

for item in prices:
    if item==78:
        break
    if item % 2 == 0:
        even_prices.append(item)
    else:
        odd_prices.append(item)

print(prices)
print(even_prices)
print(odd_prices)

