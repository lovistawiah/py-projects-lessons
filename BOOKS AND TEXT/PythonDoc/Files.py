    #Reading and Writing files
    #open() accepts two arguments, the file name and the mode of the file(optional: when omitted, read becomes the file mmode)
    #mode:can be
    #  r- to read the file
    # w- to write to the file. it clears existing data if not empty and start writing
    # a- append text(data) to the end of the file 
    # r+ - read and write to the file
    # b - open file in binary mode NOTE:this should be used for files that do not contain text
    
    #NOTE:In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

#f = open('lovis.txt','w')

#using the with keyword
#NOTE: the advantage of using the with is that, files are properly closed when done working on them,even if an exception is raised at some point and is shorter when writing equivalent to the try-finally blocks

with open('lovis.txt') as f:
    read_data =f.read()

print(f.closed)

#NOTE: if you are not using the with keyword, remember to close the file using file_name.close() and free up any system resources used by it

#NOTE:f.write() might not completely write to the disk when called without using ' with '  or f.close() even if the program exits successfully  

# Attempting to write to a file when closed with ' with ' or f.close() will raise a ValueError

with open('lovis.txt') as file:
    #NOTE: when integer passed as argument, the value the number of characters to print out or empty string is passed as an argument it returns empty string
    read_data = file.read(10)
#    print(read_data)

#Reading a line in a text or binay file

with open('lovis.txt') as file_readline:
    #NOTE:using the readline() method to read the first line of a text or binary file. it stops reading and return string when it first sees \n symbol
    read_data = file_readline.readline()
    #print(read_data)

#to read lines of file objects, loop through each line of text or binary file. it is memory efficient and simple code
with open('lovis.txt') as file_readlines:
    for line in file_readlines:
        print(line, end='')


with open('lovis.txt') as file_lines:
    read_data = file_lines.readlines()
    for datum in read_data:
        print(datum)

#Writing to a file
# the write() method with the specification of file mode, if ' w ', clears existing text and write new text in the file. if ' a ' add text to the end of existing file
with open('write.txt','w') as file:
    write_file = file.write('this is Lovis Tawiah\n')
    print(write_file)


with open('write.txt','a') as f:
    value = ('the answer', 42)
    s = str(value)  # convert the tuple to string
    read = f.write(s)
    print(read)

#f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode:

with open('lovis.txt') as file_lines:
    read_data = file_lines.tell()
    print('current position of file',read_data)

#FIXME: not writing in binary numbers
with open('workfile.txt','rb+') as f:
    read_data = f.write(b'01234567890abcdef')
    print(read_data)