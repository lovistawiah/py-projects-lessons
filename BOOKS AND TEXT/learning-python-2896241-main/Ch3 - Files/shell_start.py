#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

from os import path
import shutil

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath('textfile.txt')

    # let's make a backup copy by appending "bak" to the name
        dst = src + " .bak"
        shutil.copy(src, dst)
    # rename the original file

    # now put things into a ZIP archive

    # more fine-grained control over ZIP files


if __name__ == "__main__":
    main()
