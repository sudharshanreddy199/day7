#---->while loop

#---->break using while loop
#ex:1
# 1.) iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
'''
# 2)
'''
i=20
while i<31:
    print(i)
    
    if i==27:
        break
    i+=1
    '''
#3)
'''
    i=20
while i<31:
    
    if i==27:
        print(i)
        break
    i+=1
'''
#--->continue
#--->eg:1
'''    
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1
'''
#2)
'''
i=20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)
'''
#3)
#while to iterate from 12 to 22
#find the sum of all numbers
'''
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
'''
#--->eg:6
# find the average of value from 20 to 25
'''
i=20
sum=0
count=0
while i<25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
'''

#----->nested for loop
#eg1:)
'''
for i in range (1,3+1):
    for j in range (1,4+1):
        print(i,j)
'''
#eg:)
#****
#****
#****
#****

'''
for rows in range(4):
    for col in range (4):
        print("*",end=" ",)
    print()
'''
'''
rows=int(input("enter the rows"))
cols=int(input("enter the cols"))
for row in range(rows):
    for col in range (cols):
        print("*",end=" ",)
    print()
'''

'''
sum=0
for row in range(5):
    for col in range (5):
        sum=sum+1
        print(sum,end=" ",)
    print()

'''
# to print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row):
        print("*",end=" ")
    print()
'''
'''
for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
    print()

'''
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==4or row==0 or row==4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3)
            or (row==1 and (col>=2 and col<=4)
                or(row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


'''
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

'''
# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary
# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous


# To access the elements in the list
'''
l1 = [1,4,1,7,7.89,'p','i']

print(l1)

'''
'''
# Indexing --->
In the collection datatypes like list,tuple,string,the elements will be alloted with predefines unique value called index value.

# We have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side
'''
'''
# Positive indexing -->

lst1 = [1,4,1,7,7.89,'p','i']
print(lst1[0])
print(lst1[4])

#-----> negative indexing
lst1=[1,4,1,7,89,7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])

'''









































