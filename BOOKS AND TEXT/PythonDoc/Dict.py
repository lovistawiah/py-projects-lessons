import math
"""
Dictionary is key:value pair. this data type can be created assigning an empty curly braces to a variable name
Tuples can be used as keys if they contain strings,numbers or tuples. 
NOTE: list can not be used as keys. list can be modified in place using index assignments 
"""
#simple dictionary
dic = {1:'skido',2:'Money'}

print(dic)
#using the dict() constructor and tuples to create key:value pairs
dic =dict([(1,'lovis'),(2,'tawiah')])
print(dic[1])

#dict comprehension
dic = {key: key**2 for key in (2,3,4,6)}
print(dic)

#specify pairs using keyword arguments
dic = dict(sape='living',home='Spintex',rooms='4',plot='2',money='$150,000')
print(dic)


#looping techniques
#when iterating dictionary, the key and the value can be printed out the same time using dictionaryName.items()
for k,v in dic.items():
    print(f'key={k} value={dic[k]}')

#using enumerate() 
for k,v in enumerate(['tic','tac','toe']):
    print(k,v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
#using zip() function to unpack
for q, a in zip(questions,answers):
    print('What is your {0}? It is {1}'.format(q,a))

#loop a sequence in a reverse form
#NOTE: range accepts one compulsory arg and two optional args: 
for x in reversed(range(2,10,2)):
    print(x)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
print(100*'-')
for f in sorted((set(basket))):
    print(f)


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
print(string1,string2,string3)

#lexicographical ordering
#comparing sequences of the same type
print((1, 2, 3) < (1, 2, 4))
print('ABC' < 'C' < 'Pascal' < 'Python')