# Input and output

# first_name=input("Enter your first name: ")
# last_name=input("Enter your last name: ")
# age=int(input("Enter your age: "))
# eye_color=input("Enter your eye color: ")
# hair_color=input("Enter your hair color: ")
# height=float(input("Enter your height: "))
# weight=float(input("Enter your weight: "))
# shoe_size=float(input("Enter your shoe size: "))
# address=input("Enter your address: ")
#
# print(f'First Name: {first_name}')
# print(f'Last Name: {last_name}')
# print(f'Age: {age}')
# print(f'Eye Color: {eye_color}')
# print(f'Hair Color: {hair_color}')
# print(f'Height: {height}')
# print(f'Weight: {weight}')
# print(f'Shoe Size: {shoe_size}')
# print(f'Address: {address}')

# Calculate the price
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
age=int(input("Enter your age: "))
price=10
if 16<=age>0:
    discount=price*0.9
    print(f"Regular price is {price}")
    print(f"Your price is: ${discount}")
elif age>=65:
    discount=price*0.1
    print(f"Regular price is {price}")
    print(f"Your price is: ${discount}")
elif age<=0:
    print(f"Goodbye!")
else:
    print(f"Your price is {price}")


amount_of_hours=float(input("Enter amount of hours: "))

if amount_of_hours>=35:
    print(f"This is a full-time job!")
elif amount_of_hours<=0:
    print(f"You gotta work more!")
else:
    print(f"This is a part-time job!")