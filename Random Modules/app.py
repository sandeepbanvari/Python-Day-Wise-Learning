import random

# print(dir(random))

print(random.random())      # random() method returns a random float number between 0 and 1
print(random.randint(1, 10))    # randint() method returns a random integer between 1 and 10
print(random.randrange(1, 10))  # randrange() method returns a random number from a specified range
print(random.uniform(1, 10))    # uniform() method returns a random float number between 1 and 10

fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi', 'orange', 'grape']
print(random.choice(fruits))    # choice() method returns a random element from a list

print(random.sample(fruits, 3))   # sample() method returns a random sample of k elements from a list

print(random.choices('sandeep'))  # choices() method returns a list of random elements

random.shuffle(fruits)  # shuffle() method shuffles the elements of a list
print(fruits)

random.seed(6)  # seed() method generates a sequence of random numbers
print(random.randint(1, 10))




chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

password = "".join(random.choices(chars, k=8))
print(password)

