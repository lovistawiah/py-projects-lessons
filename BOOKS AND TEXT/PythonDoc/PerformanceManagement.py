from timeit import Timer
#this module is used to check performance or the efficieny between solutions to a problem

t1 =Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(t1)
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print('t1 is {}'.format(t1))
print(F't2 is{t2}')
print(f'difference between t1 and t2 is {t1-t2}')
#TODO: LEARN QUALITY CONTROL AND BATTERIES