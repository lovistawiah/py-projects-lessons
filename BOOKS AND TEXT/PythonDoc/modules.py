"""
it is customary not required to place import statement at the top of the module
"""
#importing modules(statement,function definition ) from other files

#Using from and import as keywords
# from " filename " import " statements or function definition "

#Importing everything from a module
# from module (fileName) import * NOTE: " * " represents all

#changing the name of a statement or function definition when imported
# from module(fileName) import (statements or function definitions) as (newName to be given to imported function or statements)

#NOTE:For efficiency reasons, each module is only imported once per interpreter session
import builtins
print(dir(builtins.len('lovis')))