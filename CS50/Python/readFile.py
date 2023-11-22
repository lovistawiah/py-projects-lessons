#open file: the open function accepts some parameters: "name of a file","mode of file whether read: r, write: w, append: a, readwrite:r+ "
employees = open("employees.txt","r")
#read a line
#readline() method: read the first line of a file 
#readlines() method: convert every line of the file to indexes of array
print(employees.readline())
#close a file
employees.close()