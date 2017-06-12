# Set comprehensions
a_set = set(range(10))
print(a_set)
print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2**x for x in range(10)})
'''
1. Set comprehensions can take a set as input. This set comprehension calculates the squares of the set of
numbers from 0 to 9 .
2. Like list comprehensions and dictionary comprehensions, set comprehensions can contain an if clause to
filter each item before returning it in the result set.
3. Set comprehensions do not need to take a set as input; they can take any sequence.
'''
