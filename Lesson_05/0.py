# Create a list of the squares of numbers from 1 to 10 using a list comprehension.

d1_list = [i ** 2 for i in range(1,11)]
print(d1_list)

# Create a list of numbers from 1 to 10 that are divisible by 3 using a list comprehension.

d3_list = [x for x in range(1,11) if x % 3 == 0]
print(d3_list)
# Create a list of the first 10 even numbers using a list comprehension.

d2_list = [x for x in range(2,21,2) ]#if x % 2 == 0]
print(d2_list)

# Create a list of all the uppercase letters in the string "Hello, World!" using a list comprehension.

uppercase_letters = [char for char in "Hello, World!" if char.isupper()]
print(uppercase_letters)

# d5_list = "Hello, World!"
# print(d5_list.upper())

# Create a list of the lengths of the words in the string "The quick brown fox jumps over the lazy dog" using a list comprehension

word_lengths = [len(word) for word in "The quick brown fox jumps over the lazy dog".split()]
print(word_lengths)


# Create a list of the squares of even numbers from 1 to 10 using a list comprehension.

d6_list = [i ** 2 for i in range(2,11,2)]
print(d6_list)

# Create a list of all the vowels in the string "Hello, World!" using a list comprehension.
# d7_list = [for n in  "Hello, World!" ]
vowels = [char for char in "Hello, World!" if char in "aeiouAEIOU"]


# Create a list of the sum of the elements in each tuple in the list [(1, 2), (3, 4), (5, 6)] using a list comprehension.

sums = [sum(tuple) for tuple in [(1, 2), (3, 4), (5, 6)]]

# Create a list of the first 10 Fibonacci numbers using a list comprehension.

fibonacci = [0, 1] 

[fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) for i in range(2, 10)]

print(fibonacci)

# Create a list of all the numbers from 1 to 10 that are not divisible by 2 or 3 using a list comprehension.

d10_list = [x for x in range(1,11) if not x % 2 == 0 and not x % 3 == 0]
print(d10_list)