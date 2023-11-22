import sys
"""
the try:
the statement(s) in the try and exception block is executed
if no exception is raised, the code keeps running after the try block statement
if there's an exception, it checks the exception block to find a matching a error name to execute the the code under it
if there's no exception matching name for the exception, execution stops and prints out error and exception name
"""
while True:
    #continue to loop till an integer is entered
    try: 
        x =int(input('Enter integer number: '))
        print(x)
        break
    except ValueError:
        #raise a value error to printed 
        print('this is not integer')

try:
    f = open('lovis.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

#using else clause in try block
#NOTE:The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')

    except OSError:
        print('cannot open',arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


try:
    f =open('lovis.txt')
    #chaining methods
    read = f.readline()
except: 
    print('error here')
else:
    print(read)
    f.close()

#Raising Exception 
#the raise statement allows a programmer to force an exception to occur