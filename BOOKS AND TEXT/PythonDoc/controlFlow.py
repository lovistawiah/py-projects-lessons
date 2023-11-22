x= int(input("Enter integer number: "))

#using the if statements
#NOTE:when comparing the same value use the match statemnent for more efficiency
if x < 0:
    x = 0
    print("Negative number changed to Zero (0)")
elif x == 0:
    print(0)
elif x==1:
    print("single")
else:
    print("More")


#Using the for statement
#Unlike C, Python allow the flexibity for iteration on numbers,list and string (sequences)

words =['cat','elephant','dog','mouse']

#iterating elements in a list
for w in words:
    #printing the list and its corresponding length
    print(w, len(w))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    #TODO: learn about the copy() and items() in dict
for user,status in users.copy().items():
    if status =='inactive':
        del users[user]

print(users)


#empty dict

active_users ={}

for user, status in users.items():
    #checking for particular string in users' dictionary
    if status =='active':
        #assigning key-value pair to dictionary
        active_users[user] = status
        print(active_users[user])

print(active_users)


#to iterate over sequence of numbers, the range() it really handy
for i in range(10):
    #prints 0-9 
    print(i)

#NOTE:to start iterating with a specied number, the range() has it first argument to be the specified number and second argument is the value to be iterated up to exluding the value
for i in range(3,10):
    print(i)

#NOTE: when using three arguments in the range(): the first argument is the initial value, second is the value to be iterated up to excluding the value, the third becomes the stepping value.the range() also accepts negative numbers as arguments


for i in range(0,100,2):
    print(i,end=',')

#iterating over sequences 
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i],len(a[i]))


print(sum(range(10)))


#Loop using else clause
for n in range(2,10):
    for x in range(2,n):
        if n % x ==0: 
            print(n, 'equals', x, '*', n//x)
            break
        #NOTE: loop statements may have else clause when the condition becomes false
    else:
        print(n,"is a prime number")


#using the continue statement:

for num in range(2,10):
    if num % 2 ==0:
        print(num,"is an even number")
        continue
    #NOTE: the continue keyword  continues with next iteration if the continue keyword is executed
    print(num,"is a odd number")


#pass statement: does nothing 
#NOTE: it is commonly used to create minimal classes. Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

#while True:
   # pass


#match statement: it takes an expression and compare it value to one or more case blocks in the match statement

def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something went wrong with the internet"



http = http_error(200)
print(http)


#combining single literals using "| " or the " or "

def http_error1(status):
    match status:
        case 400 | 404 | 418:
            return "bad request"
        case _:
            return "Something went wrong with the internet"


http1 = http_error1(300)
print(http1)


#matching tuples
#FIXME: create matching tuples
class Point:
    x:int
    y:int

    def is_point(point):
        match point:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")

point = Point.__dir__

print(point)