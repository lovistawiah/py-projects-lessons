# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#


run = True

while run:
    print("which day of the week you want to count")
    count = 0
    for day in ['Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        print('{0}: {1}'.format(count, day))
        count = count + 1

    print("Or 'exit' to quit")
    user_answer = input("?")
    if user_answer == "exit":
        run = False
        print("which day of the week you want to count")
        count = 0
        for day in ['Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            print('{0}: {1}'.format(count, day))
            count = count + 1
            run = True
    else:
        print('hello')
