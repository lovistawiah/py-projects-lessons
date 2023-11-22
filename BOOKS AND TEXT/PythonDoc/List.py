from collections import deque
"""
List is a comma-separated values or items in square brackets
Lists are mutable
list can also be indexed and sliced
list supports the "+ " operator
the built-in len() function return the length or number of elements in a list or string
"""
li  =[1,2,3,4,5,6,7,8,9,0]
#getting  particular value(s) of a list using the square bracket and slicing to return a portion of the list
print(li[0])

#Slicing to get the sublist from position 2 to 4 (excluded)
print(li[1:4])

#A value at a particular position can be changed by re-assigning a value to it
li[5] =20
print("modified array = ",li)

#new value can be added to the end of the array using the append method
#using append():

#NOTE:this ⬇ method accepts another list or one value as an argument
li.append(-1)
print("list modified by adding new values to it at the end of the array = ",li)

#NOTE:Re-assigning sliced list is possible and this can change the length of the list or clear it entirely
letters =['a','b','c','d','e','f','g']
#Re-assigning new values to sliced elements in the list
letters[2:5]=['C','D','E']
print(letters)

#clearing the list entirely
letters[:] = []
print(letters)

#it is possible to create list in another list(nested list)
a =[1,2,3,4]
b= ['a','b','c']
x=[a,b]

print(x)
#accesing multi dimensional arrays using multiple square brackets
print(x[1][1])


#Methods of list objects

#list.append(): add new item(s) to the end of the list.equivalent to a[len(a):] =[x]

#list.extend():is appending all the items of a list to another. equivalent to a[len(a):] =[iterable]

#list.insert(position,item): this method accepts two arguments. first is the position where the item will be inserted. the second is the item to be inserted

#list.remove(x): removes the first item that matches x in the list. if None it raise ValueError

#list.pop(): removes the last item of a list and return it. NOTE: list.pop([i]): removes item at the given position 

#list.clear(): removes every item in the list. equivalent to   del list[:]

#ist.index(value,start,end):this method has three arguments. the first is the value to look up to in the list.the second and third optional argument uses slice notation to limit the search to a particular subsequence. the second arg shows where the search should start from and third arg is where the search should end

#list.count(x): return the number of times a value appeared in a list

#TODO: learn list.sort() into details

#list.sort(list,key=None,reverse=False): sort the items of a list in place

#list.reverse(): reverses items of the list in place

#list.copy(): make a shallow copy of items of a list



#Using list as stacks
stack =[1,2,3]
stack.append(4)
print(stack)
print(stack.pop())
print(stack)

queue = deque(['lovis','lawrence','louis'])

queue.append('lawrencia')
queue.append('lovia')
queue.append('francis')
print(queue)
#this method removes the first item of the list
queue.popleft()
print(queue)

#list comprehension

squares = []
# for i in range(10):
#     squares.append(i**2)

# print(squares)

#efficient way of writing the same code
# squares = list(map(lambda x: x**2,range(10)))
# print(squares)

#more efficient way of writing the same code
squares =[x**2 for x in range(10)]
print(squares)

#print out if x is not equal to y
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])
#⬇ equivalent
print(100*"-")
combs =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)
print(100*"-")

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
matrix =list(zip(*matrix))
print(matrix)

#del statement: is used to delete value of a variable or item(s) of a list

#tuples
#NOTE:trailing comma to create one value of a tuple
single ='hello',
#empty tuple 
le =()


#SETS
#set is an undordered collection items with no duplicates.Basic use is membership testing and eliminating duplicate entries
basket= {'apple', 'orange','banana','apple','kiwi'}
#NOTE: all duplicates have been removed
print(basket)
#Membership testing
print('orange' in basket)
print('yoghurt' in basket)

#removes all duplicate letters 
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
#letters in var a in but not in var b
#NOTE: the arrangement can change 
print(a-b)

#letters in var a or var b or both
print(a|b)

#letters found in both var a and var b
print(a&b)
#letters in var a and in var b  but not both
print(a^b)

#Set comprehension
a ={x for x in 'abracadabra' if x not in 'abc'}
print(a)