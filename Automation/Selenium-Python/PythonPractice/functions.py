def greeting():
    print(f"Hello World!")

def personal_greeting(name):
    print("Hello ", name)

def return_greeting(name):
    return f"Hello {name}"

def tax(salary):
    if salary<=100000:
        return salary * 0.1
    else:
        return salary * 0.2
def experience_check(experience):
    if experience>=5:
        print("You are eligible for a senior position")
    else:
        print("You are not eligible for a senior position")
