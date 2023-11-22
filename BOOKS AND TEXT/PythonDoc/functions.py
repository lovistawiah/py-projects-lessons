# def ask_ok(prompt, retries=4, reminder="Please try again"):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

#this function takes three arguments: which can be overidden 
#NOTE: function params assingment as argument can be overidden
# print(ask_ok("'Do you really want to quit?"))

#NOTE: a value can be assigned to function params
i = 5
def f(arg =i):
    print(arg)

#this will print 5
f()

#TODO: learn the default value

def list(a,l=[]):
    l.append(a)
    return l

print(list(3))
print(list(2))
print(list(33))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  

print(100*"*")
#NOTE:unknown keywords raise typeError
print("this gives an error.there is no know keyword argument called ='actor' in the function parrrot parenthesis")
# parrot(actor='Lovis')
print(100*"*")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.","It's really very, VERY runny, sir.",shopkeeper="Michael Palin",client="John Cleese",sketch="Cheese Shop Sketch")


#TRY:
#NOTE: " * " before a parameter creates a tuple, " ** " before a param creates a dictionary and only one of such argument is allowed
def names(age,*arguments,**details):
    print("You're are",age,":)")
    for arg in arguments:
        print(arg)
    for detail in details:
        print(detail, ":", details[detail])

names(21,"You're Lovis Tawiah","You're learning Python :)","will this work-out",firstName="Lovis",lastName="Tawiah",)

#special parameters
#NOTE: the parameters list( arguments) before the " / "  are " position-only parameters " and after can be position-keyword parameters or keyword arguments. the parameters after " * " are keyword-only arguments
def postionalFunction(pos1,pos2,/,pos_kw,*,kw):
    return None

postionalFunction()