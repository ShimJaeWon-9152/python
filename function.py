#예제 문제
"""
def f(x):
    return 2*x+7
def g(x):
    return x**2
x=2

print(f(x)+g(x)+f(g(x))+g(f(x)))

def print_something_2(my_name, your_name = "TEAM LAB"):
    print("Hello {0}, My name is {1}".format(my_name,your_name))

print_something_2("JaeWon","TEAM LAB")
print_something_2("JeeWon")

def asterisk_test(a,b,*arg):
    return a + b +sum(arg)

print(asterisk_test(1,2,3,4,5))


def asterisk_test_2(*args):
    x,y,*z = args
    return x,y,z

print(asterisk_test_2(3,4,5,10,20))


def kwargs_test(**kwargs):
    print(kwargs)
    print("First Value is {first}".format(**kwargs))
    print("Second Value is {second}".format(**kwargs))
    print("Third Value is {third}".format(**kwargs))

kwargs_test(first=3,second=2,third=3)


#연습문제

def test(t):
    t = 20
    print("In Function:",t)

x= 10 
print("Before:",x)
test(x)
print("After:",x)


def sotring_function(list_value):
    return list_value.soft()

print(sotring_function([5,4,3,2,1]))


number = "100"

def midtern(number):
    result = ""
    if number.isdigit() is True:
        if number == 100:
            if number / 10 == 1:
                result = True
    else:
        result = False
    
    return result


def is_yes(your_answer):
    if your_answer.upper() == "Yes" or your_answer.upper() == "Y":
        result = your_answer.lower()

print(is_yes("Yes"))

def add_and_mul(a,b,c):
    return b + a * c + b
print(add_and_mul(3,4,5)==63)
"""

def args_test_3(one,two,*args, three):
    print(one+two+sum(args))
    print(args)

args_test_3(3,4,5,6,7)
    