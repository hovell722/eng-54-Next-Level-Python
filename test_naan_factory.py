
# import naan factory functions
# define and run tests

from naan_factory_functions import *

#1
# As a user, I can use the make_dough with water and flour to make dough.
print("calling make_dough with water and flour, expect 'dough' as a result")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

print("calling make_dough with water and concrete, expect 'not dough' as a result")
print(make_dough('water', 'concrete') == 'not dough')
print('got:', make_dough('water', 'concrete'))

#2
# As a user, I can use the bake_dough with dough to get naan.
print("calling bake_dough with dough, expect 'naan' as a result")
print(bake_dough('dough') == 'naan')
print('got:', bake_dough('dough'))

print("calling bake_dough with and, expect 'not naan' as a result")
print(bake_dough('and') == 'not naan')
print('got:', bake_dough('and'))


#3
# As a user, I can user the run_factory with water and flour and get naan.
print("calling run_factory with water and flour, expect 'naan' as a result")
print(run_factory('water', 'flour') == 'naan')
print('got:', run_factory('water', 'flour'))

print("calling run_factory with water and leather, expect 'not naan' as a result")
print(run_factory('water', 'leather') == 'not naan')
print('got:', run_factory('water', 'leather'))