'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})
returns {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
'''

def flatten_dict(d):
    result = dict()
    for i in d.keys():
        if type(d[i]) == dict:
            

print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))

'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4})
returns {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
'''

def unflatten_dict(d):
    pass

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))


'''
Problem 3: Write a function treemap to map a function over nested list.

treemap(lambda i: i*i, [1, 2, [3, 4, [5]]])
returns [1, 4, [9, 16, [25]]]
'''

def treemap(func, lst):
    pass

print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))
