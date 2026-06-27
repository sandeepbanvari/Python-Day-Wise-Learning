print(dir(set))


# ==================================================
# PYTHON SETS
# ==================================================

# Definition:
# A set is an unordered, mutable collection of unique elements.

# Key Properties:
# 1. Unordered
# 2. Mutable
# 3. No duplicate values
# 4. Unindexed

# ==================================================
# CREATING SETS
# ==================================================

# Creating a set
numbers = {1, 2, 3, 4}
print(numbers) # Output: {1, 2, 3, 4}

# Duplicate values are removed automatically
data = {1, 2, 2, 3, 3, 4}
print(data) # Output: {1, 2, 3, 4}

# Empty set
empty_set = set()
print(type(empty_set)) # Output: <class 'set'>


# ==================================================
# COMMON SET METHODS
# ==================================================

# --------------------------------------------------
# 1. add()
# Definition: Adds a single element to the set.
# --------------------------------------------------

s = {1, 2, 3}
s.add(4)

print(s)  # Output: {1, 2, 3, 4}


# --------------------------------------------------
# 2. update()
# Definition: Adds multiple elements to the set.
# --------------------------------------------------

s = {1, 2}
s.update([3, 4, 5])

print(s)  # Output: {1, 2, 3, 4, 5}


# --------------------------------------------------
# 3. remove()
# Definition: Removes an element from the set.
# Raises KeyError if element is not found.
# --------------------------------------------------

s = {1, 2, 3}
s.remove(2)

print(s)  # Output: {1, 3}


# --------------------------------------------------
# 4. discard()
# Definition: Removes an element if present.
# Does not raise an error if not found.
# --------------------------------------------------

s = {1, 2, 3}
s.discard(4)

print(s) # Output: {1, 2, 3}


# --------------------------------------------------
# 5. pop()
# Definition: Removes and returns a random element.
# --------------------------------------------------

s = {10, 20, 30}
value = s.pop()

print(value)
print(s)  # Output may vary because sets are unordered.


# --------------------------------------------------
# 6. clear()
# Definition: Removes all elements from the set.
# --------------------------------------------------

s = {1, 2, 3}
s.clear()

print(s)  # Output: set()


# --------------------------------------------------
# 7. copy()
# Definition: Creates a shallow copy of the set.
# --------------------------------------------------

s1 = {1, 2, 3}
s2 = s1.copy()

print(s2)  # Output: {1, 2, 3}


# ==================================================
# SET OPERATIONS
# ==================================================

a = {1, 2, 3}
b = {3, 4, 5}

# --------------------------------------------------
# union()
# Definition: Returns all unique elements from both sets.
# --------------------------------------------------

print(a.union(b))
# Output: {1, 2, 3, 4, 5}

print(a | b)
# Output: {1, 2, 3, 4, 5}


# --------------------------------------------------
# intersection()
# Definition: Returns common elements in both sets.
# --------------------------------------------------

print(a.intersection(b))
# Output: {3}

print(a & b)
# Output: {3}


# --------------------------------------------------
# difference()
# Definition: Returns elements in the first set
# but not in the second set.
# --------------------------------------------------

print(a.difference(b))
# Output: {1, 2}

print(a - b)
# Output: {1, 2}


# --------------------------------------------------
# symmetric_difference()
# Definition: Returns elements present in either set
# but not in both.
# --------------------------------------------------

print(a.symmetric_difference(b))
# Output: {1, 2, 4, 5}

print(a ^ b)
# Output: {1, 2, 4, 5}


# ==================================================
# RELATIONAL METHODS
# ==================================================

# --------------------------------------------------
# issubset()
# Definition: Returns True if all elements of one set
# are present in another set.
# --------------------------------------------------

x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))
# Output: True


# --------------------------------------------------
# issuperset()
# Definition: Returns True if a set contains all
# elements of another set.
# --------------------------------------------------

print(y.issuperset(x))
# Output: True


# --------------------------------------------------
# isdisjoint()
# Definition: Returns True if two sets have
# no common elements.
# --------------------------------------------------

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
# Output: True


# ==================================================
# MEMBERSHIP OPERATORS
# ==================================================

fruits = {"apple", "banana"}

print("apple" in fruits)
# Output: True

print("mango" not in fruits)
# Output: True


# ==================================================
# BUILT-IN FUNCTIONS WITH SETS
# ==================================================

numbers = {10, 20, 30, 40}

print(len(numbers))
# Output: 4

print(max(numbers))
# Output: 40

print(min(numbers))
# Output: 10

print(sum(numbers))
# Output: 100


# ==================================================
# CONVERTING LIST TO SET
# ==================================================

lst = [1, 2, 2, 3, 3, 4]

unique = set(lst)

print(unique)
# Output: {1, 2, 3, 4}


# ==================================================
# SET COMPREHENSION
# ==================================================

squares = {x**2 for x in range(5)}

print(squares)
# Output: {0, 1, 4, 9, 16}


# ==================================================
# SUMMARY
# ==================================================

# Properties of Sets:
# Ordered            -> No
# Mutable            -> Yes
# Duplicates Allowed -> No
# Indexed            -> No
# Heterogeneous      -> Yes