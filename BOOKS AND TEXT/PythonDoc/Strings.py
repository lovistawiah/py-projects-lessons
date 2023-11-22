#using r to print raw strings. it helps to print the row text in the quotes
print(r"C:\lovis")

#the use of six quotes helps in printing text on multiple lines and how the text was written
print("""
-h: lovis   tawiah
   lofldf  Tetteh
""")


#String concantenation
#NOTE: using the + operator on strings add them together 
print("hello, " + "there")

#using the " * " operator on strings
#NOTE:with the use of number and the operator(*) on a string repeats the string by the specified number. When the string appears before the operator and the number,displays Syntax error
print(3* "hello ")

#NOTE: two enclosed strings with quotes(single or double) closer to each other, concantenates
#this feature is used when you want to break long string into parts but displayed joined
print("py" "thon")


#Strings are indices of characters (subscripted) with index starting from 0
#NOTE: strings are treated like elements of list
word  ="Python"
#getting the letters of a string using list notation
print(word[0])

#NOTE: indices can be negated(negative number) to start counting from right

print(word[-1])


#Word slicing
#Slicing is use to obtain a substring of a string

# getting characters of string from 0 to 2 excluding 2 NOTE: strings are treated like lists(arrays)
print(word[0:2])

#geting chars from the beginning to position 4 (excluded)
print(word[:4])

#getting last second chars from the string
print(word[-2:])

#NOTE: Strings are immutable: re-assinging index of a character results in TypeError

#the built-in function len() return the length of a string