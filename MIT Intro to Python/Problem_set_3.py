#%%
example_collection = ['a', True, 'Python is cool', 123, 0]
any_value_truthy = any(example_collection)
all_values_truthy = all(example_collection)
print('any truthy: {}, all truthy: {}'.format(any_value_truthy, all_values_truthy))

#%%
names = ('John', 'Lisa', 'Terminator', 'Python')
semicolon_separated = ';'.join(names)
print(semicolon_separated)
#%%
def oddTuples(aTup):

    return print(aTup[::2])
oddTuples(('I', 'am', 'a', 'test', 'tuple'))
