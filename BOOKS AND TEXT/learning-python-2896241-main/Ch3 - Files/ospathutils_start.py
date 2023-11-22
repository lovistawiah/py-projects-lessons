#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print('item exist:', str(path.exists('textfile.txt')))
    print('item is file', path.isfile('textfile.txt'))
    print('item is a directory', path.isdir('textfile.txt'))

    # Work with file paths

    # Get the modification time

    # Calculate how long ago the item was modified


if __name__ == "__main__":
    main()
