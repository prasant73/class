import os # library imports

from inputs import list_input # local imports

# import -> common file directory, path->lib

# global variable declaration


# classes -> oops


# functions
def join_2_lists_return_dict(l1, l2):
    # length of both the lists are equal
    d = {}
    for i in range(len(l1)):
        d[ l1[i] ] = l2[i]
    return d


def join_2_lists_return_dict_unequal_len(t):
    # length of the lists are unequal
    l1, l2 = t
    d = {}
    for i in range(len(l1)):
        if i >= len(l2):
            d[l1[i]] = 0 # when the elements of the smaller list exhausts
        else:
            d[ l1[i] ] = l2[i] # till the elements of the smaller list gets exhausted
    return d


# determines which one of 2 is the larger list
def return_larger_list(l1, l2):
    if len(l1) > len(l2):
        return l1, l2
    else:
        return l2, l1


# driver code
if __name__ == "__main__":
    try:
        # local variables
        l1 = list_input(int(input("Enter length of l1 : ")))
        l2 = list_input(int(input("Enter length of l2 : ")))

        # function call
        if len(l1) == len(l2):
            print(join_2_lists_return_dict(l1, l2))
        else:
            print(join_2_lists_return_dict_unequal_len(return_larger_list(l1, l2)))
    
    
    
    except (ValueError, NameError) as v:
        print("an error occured : ", v)

    except Exception as e:
        print(e)

    
    
    # a = int(input("Enter a : "))
    # b = int(input("Enter b : "))
    # if b == 0:
    #     try:
    #         raise ZeroDivisionError
    #     except ZeroDivisionError as z:
    #         print(z)
    
'''
    Exception -> is the mother class
        all other exceptions are childs on the baseclass Exception
        ValueError
        NameError
        ZeroDivisionError
        AssertionError
        IndentionError

'''