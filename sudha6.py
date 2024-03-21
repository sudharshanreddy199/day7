# to  print the first and last letters are capitalize
'''
s1="hello world"
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

n=128
i=0
while n!=0:
    rem=n%10
    print(rem)
    n=n/10

#add both l1 and l2 ---> ans[6,8,10,12]
l1=[1,2,3,4]
l2=[5,6,7,8]

'''
#############################################


'''
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
     print("no")
'''


#add both l1 and l2 ---> ans[6,8,10,12]
'''
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
#print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)
'''
# charecterestic of set
'''
 1.)--> set can be created using{}
 2.)--> the elements inside set are not indexed
 3.)--> does not allow duplicate values
 4.)--> it unorderd
 5.)--> hetrogenious
 6.)--> mutable or changeble
'''
 #eg-1
'''
s1={9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)
'''
# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
'''
print(s1)
230 LEKKALA AKASH REDDY
11:27 AM
# eg
# ? to add element inside list

s1 = {8, 78, 67, 'u'}
s1.add(43)
print(s1)


# update()
s1 = {8,6,7,3,546,'u'}
s1.update([45,'i'])
print(s1)
LE -330 Rutwik mani kanth
11:33 AM
Eg:3,
# min(), max(), len()

# Eg:4,
# ? to add element inside set
#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
##s1.update(9, 0)
##print(s1)

#To deleat element inside set

s1 = {8, 78, 67, 'u'}

#pop() # to deleat one element randomly
##s1.pop()
##print(s1)
##
##remove()


s1.remove(78)
print(s1)

#discard()
##s1.discard(67)
##print(s1)
Ali Baba
11:33 AM
# update()
#s1.update([9, 0])
#print(s1)


# ? To delete element inside set

s1 = {8, 78, 67, 'u'}
# pop() # ---> To delete one element randomly
s1.pop()
print(s1)


#  ---> remove()

s1.remove(78)
print(s1)

discard()
'''


# join the sets
'''s1={8,9,5,6}
s2={56,8,25,63}
# union to combine two sets
print(s1.union(s2))
# intersection is used to get common elements inside the list
print(s1.intersection(s2))
'''
'''
s1={4,5,6}
s2={5,6,7,8}
s3=s1.difference(s2)
s4=s2.difference(s1)
print(s3.union(s4))

'''
#---> problem-1
'''
s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print(str1)
'''  



#----  char of dictionary
'''
1;have t be surrounded by{}
2;it have to be in the form of key,value pair
3;it is mutable
4;duplicate keys are not allowed,duplicate values are allowed
5;it is unindexed
6;it is ordered
7;key does not allow mutable datattypes,values allow mutable datatypes
'''

'''
d1={1:100,2:200,3:300,4:400}
print(d1)   # to acees the elements in dictionary
print(d1[2]) # to acces the values,have to use keys
# some common functions --> { len(),min(),max(),}
print(min(d1.values()))
print(max(d1.values()))
# Dictionary based functions
# To add element(key and value pair) in dict

d1 = {1:100, 2:200, 3:300, 4:400}
d1[5]=500
print(d1)



# To replace a value in dictionary
d1={1:100, 2:200, 3:300, 4:400}
d1[2]= "mango"
print(d1)

'''

# to delete the elements from dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
d1.popitem()  # pop() function is used to delete the last key value pair in dict
print(d1)
'''
#clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[90])
#print(d1.get(90))

#  to print all the keys
'''print(d1.keys())'''


#Iterating dictionary
#for val in d1:
#    print(val)

#for val in d1.value():
#    print(val)

# to get both keys and values

'''
for key, val in d1.items():
    print(key, val)

'''

#problem:1

'''
n=int(input(" enter num of times: "))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)== float:
        float_value.append(value)
    elif type(value)==string:
         string.append(value)
    else:
        print("pls provide data in int,float,string")
 '''
