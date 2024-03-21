#---->common function for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))
'''
'''
l1=[6,7,8,9,"p","u"]
print(max(l1))
print(min(l1))
'''
'''
l1=[6,7,8,9,0,8.89,-5,0.78]
print(min(l1))
'''
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
index()
print(l1.index(9))
'''
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
count()
print(l1.count(6))
'''

# some funtions which is specifically used for list

#to add element inside list
#insert() -->to add element at specific index position
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
l1.insert(2,"cars")
print(l1)
# --> to delete element from list
l1=[6,7,8,9,0,8.9,-5,0.78]
pop()
l1.pop()
print(l1)
'''
'''
# pop (index_value)-->used to delete element at specific index
l1.pop(4)
print(l1)
'''

# remove(element)---> used to delete element directly
'''
l1.remove(8.89)
print(l1)
'''
# clear()--> to complete delete all element in list
'''
l1.clear()
print(l1)
'''

#del--> to delete the list
'''
del l1
print(l1)
'''

#---> join 2 list
'''
l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)
'''

#extend()--> to combine 2 lists
'''
l1.extend(12)
print(l1)
'''
#---> copy()
'''
l1=[6,7,8,9,3]
l2=l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))
'''
#---> diff between shallow copy and deep copy
# shallow copy
#imort copy
'''
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
'''
# deep copy --> used to copy the list with nested list
# import copy
'''
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[]-1[1])
l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''
# sort--> arrange element in list in ascending or discending order
'''
l1=[9,7,45,0,-6,5,12]
l1.sort()
print(l1)
l1.sort(reverse=true)
print(l1)
l1=['z','i','o','p','9']
l1.sort()
print(l1)
'''
# list constructor
# list()---. to conver other collection datatype to list
'''
l3=((8,9,0))
print(list(l3))
l4=(8,90
print(list(l4)
'''

# ---> nested list
'''
l1=[8,9,[0,8,7],ArithmeticError["p","o",'y'],[8,'t']]
p[rint(l1[-2][1])
print(l1[1:4])
print(l1[1:-1])
'''
# to delete "t" from l1
'''
l1[-1].remove('t')
print(l1)
'''
# combine these 



# ! ----> Tuple

1.) tuple have to be surrounded by ()
2.) The element inside tuple are not changable
3.) The element inside tuple are indexed
4.) The element will excuted in order
5.) It is heterogenous
6.) It allow duplicate element
l1=[8]
'''
print(type(l1))#list

l1=(8,)
print(type(l1))#tuple

l1=8,9
print(type(l1))#tuple
'''
#len(),min(),max(),index(),count()--->all same as list
# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples
'''
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)

# To add all element inside list and tuple
sum()
l1 = (8, 9, 7, 6)
prin
LE-348 S.Nagoor basha
11:40 AM
oldman got covid,,,in csk camp
'''
# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples
'''
l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
'''
# Iterate based on index value
'''
l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
'''
#----> strings
'''
s1='0'
print(type(s1))
s1="hello world"
'''
#
# To access string
#print(s1)

# indexing and slicing ---> same as list and tuple

#print(s1[0:5])

# len(),min(),max(),index(),count()

s1="hello world"

# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord() ---> used to find the ASCII value of a character
s1='u'
print(ord(s1))


# functions of string
s1 = "hello world"
# To convert all characters to upper case
print(s1.upper())

'''


# To convert all characters to lower case
'''
s1="HYIDUJIKWady"
print(s1.lower())
'''


#---> strip()--> to eliminate thge space in beginning and end of string
'''
s1=" where are yoou?"
print(s1.lstrip())
print(s1.rstrip())

print(s1.strip())
'''
# split--> to split the words in string based on charecter
'''
s1="where are yoou?"
print(s1.split(" "))
print(s1.split("e"))
'''


# replace()--> to reeplace  a specific char in the string
'''
s1="where are yoou?"
print(s1.replace('r','**'))
'''
#swapcase()--> to convert capital to small and small to capital at a time

# Swapcase()---> to convert capital to small and small to capital
'''
s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 =
how are you
iam fine
hey there


# splilines() ---> used to split the string based on lines
s1 ='''
#how are you
#iam fine
#hey there
'''
print(s1.splitlines())


# Find () --> To find the index based on a character
s1="hello world"
print(s1.index('z'))

# Join() --->
l1=["hey", "there"]
#print(" ".join(l1))
print("$".join(l1))


s1="Welcome to all"
print(s1.endswith('L')) ---> we get either true or false
'''

# print revese the string
'''
s1="Welcome to all"
print(s1[::-1])
'''
## wap to find the number of lower case letters

'''
s1="HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1
print("the total number of lower case letters:",count)
'''

#--> eg:2 r----"$"
'''
s1='restarter'
print(s1.replace('r','$'))
'''
# find chars

s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop p"
char=len(s1)
print(char)
words=s1.split()
print(len(words))
sentenses=s1.split(".")
print(len(sentenses))






























































