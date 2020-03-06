# Factory functions
# define our functions here

#1
# As a user, I can use the make_dough with water and flour to make dough.

def make_dough(arg1, arg2):
    # if arg1 is water, and arg2 is flour
        # return dough
    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    # else
        # return not dough
    else:
        return 'not dough'

#2
# As a user, I can use the bake_dough with dough to get naan.

def bake_dough(arg3):
    # if arg1 is dough
        # return naan
    if arg3 == 'dough':
        return 'naan'
    # else
        # return not naan
    else:
        return 'not naan'


#3
# As a user, I can user the run_factory with water and flour and get naan.

def run_factory(arg1, arg2):
    # if arg1 is water and arg2 is flour
        # return dough
            # return naan
    if make_dough(arg1, arg2) == 'dough':
        arg3 = make_dough(arg1, arg2)
        return bake_dough(arg3)
    # else
        # return not naan
    else:
        return 'non naan'











































# def test_example():
#    return 'testing'

# print(test_example()) don't call functions here!
# this will violate the separation of concerns and
# it will run said functions when you are importing them elsewhere