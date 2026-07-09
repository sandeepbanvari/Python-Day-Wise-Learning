# File Handling 
    # -- File Handling in python allow to create, read, write and modify files stored on our computers.

# Write File
file = open('simple.txt', 'w')
file.write('Name :- Sandeep\n')
file.write('Course :- Python\n')
file.close()

# Read File
file = open('simple.txt', 'r+')
print(file.read())
file.close()

# Apend
with  open('simple.txt', 'a') as f:
    f.write('Programming Language\n')
    

