

def add_two_numbers():
    first_num = 44839
    second_num = 67389
    total = first_num+second_num
    return total

print(add_two_numbers())

def greetings(name):
    welcome_note = name + ",Welcome to the world of python!"
    return welcome_note

print(greetings('Girish'))

def add_ten(num):
    ten = 10
    return num+ten
    
print(add_ten(100))

def square_of_number(x):
    return x**2

print(square_of_number(3))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)

print(sum_of_numbers(5))

def weight_of_object(weight,gravity):
    mass = str(weight*gravity) +"N"
    return mass
print("Weight of object in newtons is:", weight_of_object(233,9.8))

def age(current_year,birth_year):
    current_age = current_year-birth_year
    return current_age
print("Your age is:",age(2026,2004))

def state_name(firstname,lastname):
    space = ''
    full_name = firstname + space + lastname
    return full_name
print(state_name(firstname = 'Tamil',lastname = 'Nadu'))
def is_even(n):
    if n % 2 == 0:
        print("even")
        return True
    return False
print(is_even(7766483))
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))    

def greetings (fname = 'Peter', lname = 'Andrew'):
    message = fname + ', welcome to Python for Everyone!'+' '+ lname + ', Welcome him'
    return message
print(greetings('David','Beckham'))

def sum (*nums):
    total = 0
    for i in nums:
        total+=i
    return total
print(sum(3,4,5))
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
