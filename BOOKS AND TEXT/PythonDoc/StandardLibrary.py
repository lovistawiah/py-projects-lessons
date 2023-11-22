#the os module has a lot useful function
import os
#get the current working directory
cwd =os.getcwd()
print(cwd)

#the system method() helps to run command in the shell.it accepts string command as arguments
#os.system('mkdir today')

#NOTE:use the import os style instead of from os import *. This will keep os.open() from shadowing the built-in open() function which operates much differently.

#the dir() function is used to print a list of all methods and atrributes of the module
print(dir(os))

#help() prints the docstring of the os
#help(os)

#                           SHUTIL
#for daily file and directory management, use shutil
import shutil

#used for coping the element of a file to another file
#shutil.copyfile('lovis.txt','write.txt')


#WILD CARDS 
#the glob() is a function that, return a list of files in the directory during the searches
import glob

find = glob.glob('*.py')
print(find)

#COMMAND LINE ARGUMENTS
#
import sys

#the argv return a list of current working file
print(sys.argv)


# import argparse
# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
#print(args)


#ERROR OUTPUT REDIRECTION AND PROGRAM TERMINATION 
#the sys holds a lot of useful methods.some are stdin, stdout, stderr

#the stderr is used for emitting warning and error messages to make them visible even if the stdout has been redirected

sys.stderr.write('Warning, log file not found starting a new one\n')


#NOTE: the most direct way to terminate a script is to use sys.exit()

#STRING PATTERN MATCHING
#regular expression module
import re


#findall() return a list of matching text that
#the first argument specifies the regular expression pattern (return a list of matching text that start with f)
findall = re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
print(findall)

#TODO: learn about the sub()
sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat 122')
print(sub)

