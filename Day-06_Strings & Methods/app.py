'''
Strings
        -- A string is a sequence of characters enclosed in single, double, or triple quotes,
    used to store in Python.
    String Indexing
        -- String indexing is a technique used to access individual characters of a string by
        referring to their position number.
        -- Indexing starts from 0 for the first character.
        -- Negative indexing starts from -1 for the last character.
    String Slicing
        -- String slicing is the process of extracting a part of a string by specifying the 
        starting and ending index positions using the slicing operator (:).
        -- syntax
        string[start : end : step]
            start → Starting index (included)
            end → Ending index (excluded)
            step → Number of positions to move (optional)
'''

s = 'python programming python'
print(s) # python programming
print(len(s)) # 18

# string indexing
print(s[0]) # p
print(s[-2]) # o

# String slicing
print(s[0:5:1]) # pytho
print(s[0:6:]) # python

# print(dir(str))

'''
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
    'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
    'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
    'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
    'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
    'title', 'translate', 'upper', 'zfill'
'''

'''
Searching Methods:-
    -- Searching methods are used to find the position of a character or substring within a string.
    find() -- Searches for a substring and returns its first occurrence index.
    rfind() -- Searches from right to left and returns the last occurrence index.
    index() -- returns the first occurrence index of a substring. If not found, it raises a ValueError.
    rindex() -- Returns the last occurrence index and raises an error if not found.
    count() -- Returns the number of times a specified value appears in the string.
'''
print(s.find('python')) 
print(s.rfind('python'))
print(s.index('python'))
print(s.rindex('python'))

'''
Formating Method:-
    -- Formatting methods are used to align, organize, and display strings in a readable format.
    ljust() -- Returns a left justified version of the string.
    rjust() -- Returns a right justified version of the string.
    center() -- Returns a centered version of the string.
    
'''
print(s.ljust(30,'$'))
print(s.center(30,'$'))
print(s.rjust(30,'$'))
    
# 1. capitalize()
# Definition: Converts the first character to uppercase and the rest to lowercase.
print("python programming".capitalize())
# Output: Python programming


# 2. casefold()
# Definition: Converts the string to lowercase (more aggressive than lower()).
print("PyThOn".casefold())
# Output: python


# 3. center()
# Definition: Centers the string within a specified width.
print("Python".center(10, '-'))
# Output: --Python--


# 4. count()
# Definition: Returns the number of occurrences of a substring.
print("banana".count('a'))
# Output: 3


# 5. encode()
# Definition: Converts the string into bytes.
print("Python".encode())
# Output: b'Python'


# 6. endswith()
# Definition: Returns True if the string ends with the specified suffix.
print("hello.py".endswith(".py"))
# Output: True


# 7. expandtabs()
# Definition: Replaces tab characters (\t) with spaces.
print("A\tB".expandtabs(4))
# Output: A   B


# 8. find()
# Definition: Returns the first index of the substring; -1 if not found.
print("banana".find('a'))
# Output: 1


# 9. format()
# Definition: Formats the string using placeholders {}.
print("Hello {}".format("Sandeep"))
# Output: Hello Sandeep


# 10. format_map()
# Definition: Formats the string using a dictionary.
data = {"name": "Sandeep"}
print("Hello {name}".format_map(data))
# Output: Hello Sandeep


# 11. index()
# Definition: Returns the first index of a substring; raises an error if not found.
print("banana".index('a'))
# Output: 1


# 12. isalnum()
# Definition: Returns True if all characters are letters or numbers.
print("abc123".isalnum())
# Output: True


# 13. isalpha()
# Definition: Returns True if all characters are alphabetic.
print("Python".isalpha())
# Output: True


# 14. isascii()
# Definition: Returns True if all characters are ASCII characters.
print("Python".isascii())
# Output: True


# 15. isdecimal()
# Definition: Returns True if all characters are decimal numbers.
print("123".isdecimal())
# Output: True


# 16. isdigit()
# Definition: Returns True if all characters are digits.
print("123".isdigit())
# Output: True


# 17. isidentifier()
# Definition: Returns True if the string is a valid Python identifier.
print("my_var".isidentifier())
# Output: True


# 18. islower()
# Definition: Returns True if all letters are lowercase.
print("python".islower())
# Output: True


# 19. isnumeric()
# Definition: Returns True if all characters are numeric.
print("123".isnumeric())
# Output: True


# 20. isprintable()
# Definition: Returns True if all characters are printable.
print("Hello".isprintable())
# Output: True


# 21. isspace()
# Definition: Returns True if all characters are whitespace.
print("   ".isspace())
# Output: True


# 22. istitle()
# Definition: Returns True if each word starts with an uppercase letter.
print("Hello World".istitle())
# Output: True


# 23. isupper()
# Definition: Returns True if all letters are uppercase.
print("PYTHON".isupper())
# Output: True


# 24. join()
# Definition: Joins elements of an iterable into a string.
print("-".join(["a", "b", "c"]))
# Output: a-b-c


# 25. ljust()
# Definition: Left-aligns the string in a specified width.
print("Python".ljust(10, '-'))
# Output: Python----


# 26. lower()
# Definition: Converts all characters to lowercase.
print("PYTHON".lower())
# Output: python


# 27. lstrip()
# Definition: Removes leading spaces or specified characters.
print("   hello".lstrip())
# Output: hello


# 28. maketrans() and translate()
# Definition: Creates and applies a translation table.
table = str.maketrans("abc", "123")
print("abc".translate(table))
# Output: 123


# 29. partition()
# Definition: Splits the string into three parts at the first separator.
print("hello-world".partition('-'))
# Output: ('hello', '-', 'world')


# 30. removeprefix()
# Definition: Removes the specified prefix if present.
print("Mr.Sandeep".removeprefix("Mr."))
# Output: Sandeep


# 31. removesuffix()
# Definition: Removes the specified suffix if present.
print("file.txt".removesuffix(".txt"))
# Output: file


# 32. replace()
# Definition: Replaces occurrences of a substring with another.
print("Hello World".replace("World", "Python"))
# Output: Hello Python


# 33. rfind()
# Definition: Returns the last index of a substring; -1 if not found.
print("banana".rfind('a'))
# Output: 5


# 34. rindex()
# Definition: Returns the last index of a substring.
print("banana".rindex('a'))
# Output: 5


# 35. rjust()
# Definition: Right-aligns the string in a specified width.
print("Python".rjust(10, '-'))
# Output: ----Python


# 36. rpartition()
# Definition: Splits the string at the last occurrence of a separator.
print("hello-world".rpartition('-'))
# Output: ('hello', '-', 'world')


# 37. rsplit()
# Definition: Splits the string from the right side.
print("a,b,c".rsplit(',', 1))
# Output: ['a,b', 'c']


# 38. rstrip()
# Definition: Removes trailing spaces or specified characters.
print("hello   ".rstrip())
# Output: hello


# 39. split()
# Definition: Splits the string into a list.
print("a,b,c".split(','))
# Output: ['a', 'b', 'c']


# 40. splitlines()
# Definition: Splits the string at line breaks.
print("Hello\nWorld".splitlines())
# Output: ['Hello', 'World']


# 41. startswith()
# Definition: Returns True if the string starts with the given prefix.
print("Python".startswith("Py"))
# Output: True


# 42. strip()
# Definition: Removes leading and trailing spaces.
print("  hello  ".strip())
# Output: hello


# 43. swapcase()
# Definition: Converts uppercase to lowercase and vice versa.
print("PyThOn".swapcase())
# Output: pYtHoN


# 44. title()
# Definition: Converts the first character of each word to uppercase.
print("hello world".title())
# Output: Hello World


# 45. upper()
# Definition: Converts all characters to uppercase.
print("python".upper())
# Output: PYTHON


# 46. zfill()
# Definition: Pads the string with zeros on the left.
print("42".zfill(5))
# Output: 00042