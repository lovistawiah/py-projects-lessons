#using None as empty value to check for the smallest value through iteration 
smallest = None
for num in [4, 73, 63, 62, 72, 1, 7, 3, 74, 0]:
    if smallest == None:
        #use the is keyword not the == operator, the is keyword is stronger than == operator. 
        #NOTE: do not use "is" on integers and floats rather on strings or characters
        smallest = num
        print(smallest)
    elif num < smallest:
        smallest = num
        print(smallest)
    else:
        print(smallest)
print('done')
