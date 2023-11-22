a,b = 0 ,1
while a < 10:
    #NOTE:the end keyword can be used to avoid the new line or pass in another string to modify the output
    print(a,end=",")
    a, b = b, a + b


#0 means false
if 0:
    print("hello, world")