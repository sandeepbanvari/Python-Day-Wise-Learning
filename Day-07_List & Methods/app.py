# ==================================================
# PYTHON LISTS
# ==================================================

# Definition:
# A list is an ordered, mutable (changeable) collection
# that can store multiple items of different data types.

# Features of Lists:
# 1. Ordered
# 2. Mutable
# 3. Allows duplicates
# 4. Stores different data types

# Creating a List
numbers = [1, 2, 3, 4]
print(numbers)          # [1, 2, 3, 4]

data = [10, "Python", 3.14, True]
print(data)             # [10, 'Python', 3.14, True]


# ==================================================
# ACCESSING ELEMENTS
# ==================================================

fruits = ["apple", "banana", "mango"]

# Indexing
print(fruits[0])        # apple
print(fruits[-1])       # mango

# Slicing
print(fruits[0:2])      # ['apple', 'banana']


# ==================================================
# MODIFYING LISTS
# ==================================================

fruits[1] = "orange"
print(fruits)           # ['apple', 'orange', 'mango']


# ==================================================
# BUILT-IN LIST METHODS
# ==================================================

# --------------------------------------------------
# 1. append()
# Definition: Adds an item to the end of the list.
# --------------------------------------------------

nums = [1, 2]
nums.append(3)

print(nums)             # [1, 2, 3]


# --------------------------------------------------
# 2. extend()
# Definition: Adds elements from another iterable.
# --------------------------------------------------

a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)                # [1, 2, 3, 4]


# --------------------------------------------------
# 3. insert()
# Definition: Inserts an item at a specific index.
# --------------------------------------------------

fruits = ["apple", "mango"]

fruits.insert(1, "banana")

print(fruits)           # ['apple', 'banana', 'mango']


# --------------------------------------------------
# 4. remove()
# Definition: Removes the first occurrence of a value.
# --------------------------------------------------

nums = [10, 20, 30, 20]

nums.remove(20)

print(nums)             # [10, 30, 20]


# --------------------------------------------------
# 5. pop()
# Definition: Removes and returns an item by index.
# --------------------------------------------------

nums = [10, 20, 30]

value = nums.pop()

print(value)            # 30
print(nums)             # [10, 20]

nums.pop(0)

print(nums)             # [20]


# --------------------------------------------------
# 6. clear()
# Definition: Removes all items from the list.
# --------------------------------------------------

nums = [1, 2, 3]

nums.clear()

print(nums)             # []


# --------------------------------------------------
# 7. index()
# Definition: Returns the index of an element.
# --------------------------------------------------

fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))   # 1


# --------------------------------------------------
# 8. count()
# Definition: Counts occurrences of an element.
# --------------------------------------------------

nums = [1, 2, 2, 3, 2]

print(nums.count(2))    # 3


# --------------------------------------------------
# 9. sort()
# Definition: Sorts the list in ascending order.
# --------------------------------------------------

nums = [5, 2, 8, 1]

nums.sort()

print(nums)             # [1, 2, 5, 8]

nums.sort(reverse=True)

print(nums)             # [8, 5, 2, 1]


# --------------------------------------------------
# 10. reverse()
# Definition: Reverses the list.
# --------------------------------------------------

nums = [1, 2, 3]

nums.reverse()

print(nums)             # [3, 2, 1]


# --------------------------------------------------
# 11. copy()
# Definition: Creates a shallow copy of the list.
# --------------------------------------------------

a = [1, 2, 3]

b = a.copy()

print(b)                # [1, 2, 3]


# ==================================================
# LIST OPERATIONS
# ==================================================

# Concatenation (+)

a = [1, 2]
b = [3, 4]

print(a + b)            # [1, 2, 3, 4]


# Repetition (*)

print([1, 2] * 3)       # [1, 2, 1, 2, 1, 2]


# Membership Operators

fruits = ["apple", "banana"]

print("apple" in fruits)        # True
print("mango" not in fruits)    # True


# ==================================================
# LIST COMPREHENSION
# ==================================================

squares = [x**2 for x in range(5)]

print(squares)          # [0, 1, 4, 9, 16]


# ==================================================
# NESTED LISTS
# ==================================================

matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[1][0])     # 3


# ==================================================
# BUILT-IN FUNCTIONS USED WITH LISTS
# ==================================================

nums = [10, 20, 30, 40]

print(len(nums))        # 4
print(max(nums))        # 40
print(min(nums))        # 10
print(sum(nums))        # 100


# ==================================================
# SORTED FUNCTION
# ==================================================

nums = [5, 3, 1, 4]

new_list = sorted(nums)

print(new_list)         # [1, 3, 4, 5]
print(nums)             # [5, 3, 1, 4]


# ==================================================
# SUMMARY
# ==================================================

# List Properties:
# Ordered      -> Yes
# Mutable      -> Yes
# Duplicates   -> Yes
# Indexed      -> Yes
# Heterogeneous-> Yes