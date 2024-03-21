'''
def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)
 def gracemark(object):
     print(object+4)
gracemark(obj)
gracemark(obj1)



def palindrome(n):
    print(n)


a=int(input("enter the value:"))
palindrome(a)




#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args

# * Positional args
# ? The position of parameter have to be same as position as arguments
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile(96668686,"Usman",100) #unexpected
LE - 326 K. RAMESH
10:29 AM
def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

profile(8074884522,"Ramesh",95)



# keyword variable length args


# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions

  
def profile(name,phone,mark):
    txt="My name is {}. My phone number {}. I got {} marks."
    print(txt.format(name,phone,mark))
profile(name="Kalyan",mark=100,phone=9666868634)



# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
profile("shashank",mark=98,phone=9876543210)


# ---> Default args
# The method of assigning the argument to the parameter while declaring the function.

# Eg:1

def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile("shashank",9876543210,89)



Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal




# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)

'''



# Variable length parameter

# Eg:1

# To pass more than 1 arg to a parameter means we use variable length args.
# To convert normal parameter to variable length param, add * to other prefix of param.

'''
def profile(name):
    print()

class person:
    def display():
        print("hello welcom to classes")

p = person()
p.disply()

# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are

'''
# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation
# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1
'''
def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    
'''
# Eg:-2
'''
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=
LE-318 DUDEKULA USMAN
3:05 PM
# ex:3
# create of a method
#When the function is created with a class is called as method
#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p=person()
#p.display()



# ? eg:4
class person1:
    frame = "malli" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()



































































































