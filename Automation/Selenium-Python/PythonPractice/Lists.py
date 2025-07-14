fruits=["apple","banana","orange","mango"]
print(fruits)
print(fruits[-1])
fruits.append("pineapple")
print(fruits)
print(type(fruits))

mixed_list=["apple",2,"banana",4,"orange",6,"mango"]
print(mixed_list)
mixed_list.append("potato")
print(mixed_list)
mixed_list.remove ("banana")
print(mixed_list)
print("*"*50 )
print(f"the length of my list is {len(mixed_list)}")
mixed_list.remove(mixed_list[len(mixed_list)-3])
print(mixed_list)


score=[10, 50, 30, 1, 100, 4]
print(score)
print(f"the max is: {max(score)}")
print(f"the min is: {min(score)}")
