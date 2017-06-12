#Dictionary comprehensions
a_dict = {'a': 1, 'b': 2, 'c': 3 }
print(a_dict)
a_dict = {value:key for key, value in a_dict.items()}
print(a_dict)

'''
Of course, this only works if the values of the dictionary are immutable, 
like strings or tuples. If you try this with a dictionary that contains lists,
it will fail most spectacularly.
'''
