#Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

#python scopes and namespaces



def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

#Instance Objects
#NOTE: There are two kinds of valid attribute names: data attributes and methods.

#method is function that belongs to an object

class Dog:
    tricks =[]
    def __init__(self,name):
        self.name = name
        
    def add_trick(self,trick):
        self.tricks.append(trick)

e = Dog('German Shepherd')
f = Dog('English Shepherd')
e.add_trick('play funny')
f.add_trick('play silly')
#dogs sharing similar tricks
print(40*'-')
print(e.tricks)


#Correct design for each dog should have its own tricks

class Dogs:
    def __init__(self,name):
        self.name = name
        self.tricks = []
    
    def add_tricks(self,trick):
        self.tricks.append(trick)
    

r =Dogs('German Shepherd')
s =Dogs('English Shepherd')
t =Dogs('Rotwaller')



r.add_tricks('play funny')
r.add_tricks('play silly')
r.add_tricks('play rough')
print(40*'-')
print(r.tricks)

s.add_tricks('play dirty')
s.add_tricks('play gin')
s.add_tricks('play fin')
print(40*'-')
print(s.tricks)

t.add_tricks('greedy')
t.add_tricks('flawless')
t.add_tricks('nice')
print(40*'-')
print(t.tricks)


#If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance
#NOTE: the instance variable value overrides the variable value of the class if the same
print(40*'-')
class Warehouse:
    purpose = 'storage'
    region  ='west'

house1 = Warehouse()
print(house1.purpose, house1.region)
house2 = Warehouse()
house2.region ='east'
print(house2.purpose, house2.region)


#function defined outside a class can be turn into a method

#function outside a class
def f1(self,name,age):
    return f'your name is {name} and age is {age}'

class Person:
    f = f1

    def g(self):
        return 'hello world'
    
    h =g

lovis = Person()
lov = lovis.f('lovis',21)
taw =lovis.g()
print(30*'-')
print(lov)
print(30*'-')
print(taw)




class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)
        return x

    def addTwice(self,x):
        self.add(x)
        self.add(x)


gucci = Bag()
gucci.add('lovis')
gucci.add('tawiah')
gucci.add('tetteh')

#returns the last item appended
print(gucci.add('loord'))

#returns the list of bags
print(gucci.data)
# print(Person.__class__)

#                       INHERITANCE

#syntax:
#DerivedClassName(BaseClassName):
    #statement 1
    # .....
    #statement N

#when base class is in another module
#syntax:
#DerivedClassName(moduleName.BaseClassName):
    #statement 1
    # .....
    #statement N


#MULTIPLE INHERITANCE

#DerivedClassName(Base1, Base2, Base3):



#PRIVATE VARIABLES
class Mapping:
    def __init__(self,iterable):
        self.item_list =[]
        self.__update(iterable)
    
    def update(self,iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update

class SubMapping(Mapping):
    def update(self,keys,values):
        for item in zip(keys,values):
            self.item_list.append(item)


item = Mapping('gee')


print(item.item_list)


#Odds and Ends

#Creating empty class bundling data attributes to it late

class Employee:
    pass

emp1 =Employee()

emp1.name="lovis tawiah"
emp1.occupation="Software Engineer"
emp1.companies="Bending Spoons and Trilogy"
emp1.salary = 70000

print(emp1.name,emp1.companies)


#ITERATORS

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("write.txt"):
    print(line, end='')
    


#NOTE: how for loop works behind the scenes
#the for calls the iter() built in function an pass the object to be iterated to it. the iter() class the next(). iterate the element of the object one at a time and raise StopIteration exception which tell the loop to terminate

chars = 'abc'
char =iter(chars)
print(next(char))
print(next(char))
print(next(char))


#this prints StopIteration exception
# print(next(char))

class Reverse:
    def __init__(self,data):
        self.data =data
        self.index = len(data)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index ==0:
            raise StopIteration
        self.index =self.index-1
        return self.data[self.index]


call = Reverse('lovis')
for char in call:
    print(char)


    #GENERATORS

#Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

def reverse(data):
    length =len(data)-1
    for index in range(length,0,-1):
        yield data[index]

for char in reverse('golfs'):
    print(char)


#GENERATOR EXPRESSION 
#generator expression are similar to list comprehension but parenthesis instead of square braces

print( (sum(i*i for i in range(10) )) )

list1 =[20,34,53]
list2 =[3,5,2]
product =sum(x*y for x,y in zip(list1,list2))
print(product)
page ='widgets and feeling secure in your job. It\'s just as much about developing the skills and sensibilities for leading a more rewarding '
unique_words =set(word for line in page for word in line.split())
print(unique_words)

#TODO: learn the standard library tomorrow