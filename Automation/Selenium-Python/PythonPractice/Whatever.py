print("Hello World!")

name="Anna"
age=29
print(f"Hello {name}!")
print(f"My name is {name} {age} years old.")

# Variable types
#1 integer
x=10
#2 float number
pi=3.14
#3 string
name="Anna"
restaurant_name="Bear"
#4 boolean

print(x,pi,name)
print(f"My fav restaurant is '{restaurant_name}'")

counter=0
print("counter right now is", counter)
counter+=1
print("counter right now is", counter)
counter= counter +1
print("counter right now is", counter)
print(type(counter))
print(type(x),type(pi),type(name))

# calculating different variables

price_of_item=10
quantity_of_item=5
total_cost=price_of_item*quantity_of_item
print(f"The total cost is: ${total_cost}")
customer_name="Ivan"
result_of_purchase=customer_name+" paid for "+str(total_cost)+" apples "
print(result_of_purchase)

number=10
is_positive=number>0
less_than_hundred=number<100
if is_positive:
    print("I'm a positive number")
else:
    print("I'm a negative number")

if number>0:
    print("I'm a great number")
else:
    print("I'm a negative number")

if is_positive and less_than_hundred:
    print("I'm a positive number and less than 100")
else:
    print("I'm a negative number either more than 100")

# Test results: A - 100%; B - 90-99%; C - 80-89%; D - less than 80%

score=99
if score==100:
    print("Grade A")
elif score >= 90 and score <= 99:
    print("Grade B")
elif score>=80 and score <=89:
    print("Grade C")
else:
    print("Grade D")

# Input

print("Test results: A - 100%; B - 90-99%; C - 80-89%; D - less than 80%")
score=int(input("What is your score?"))
print (f'Your score is {score}')
if score==100:
    print("Grade A")
elif score >= 90 and score <= 99:
    print("Grade B")
elif score>=80 and score <=89:
    print("Grade C")
else:
    print("Grade D")

word="Hurray! "
print(word*3)

# Length of the string - verification method
new_string=input("Enter a string ")
length_of_string=len(new_string)
print("the length of the string is "+str(length_of_string))
if length_of_string<10 and length_of_string>0:
    print("The password is less than 10 characters")
elif length_of_string>=10:
    print("The password is accepted")
else:
    print("Provide the password")




