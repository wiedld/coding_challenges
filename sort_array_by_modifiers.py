# PROBLEM
#
# given an array int,
# write funct
# find min x that is changed, that makes:
# -generate new array, sorted by ascending order
#
# original array: 5,4,3,2,8
# min value = - 3, result abs(-3) = 3
# modifiers applied:  -3, -1, +1, +3, 8
# outcome array: 2,3,4,5,8
#
#################################################
#
# APPROACH:
#
# min value = 2
# max value = 8
# len = 5
# avg value = midpt.  starting_value = avg - len/2

# make target/outcome array.
# one pass through original array (with conditionals) to find modifiers
# min of modifiers

#################################################

import math

def sort_by_modifiers(alist):
    min_value, max_value = min(alist), max(alist)
    avg_value = (max_value + min_value)/2
    length = len(alist)

    # building target list
    starting_value = avg_value - length/2.0
    # handle different starting values, based on float math
    value_1, value_2 = int(math.floor(starting_value)), int(math.ceil(starting_value))

    target_1 = [x for x in range (value_1, value_1+length) ]
    target_2 = [x for x in range (value_2, value_2+length) ]

    # determine modifiers
    modifiers_1, modifiers_2 = [], []
    max_mod_1, max_mod_2, = None, None

    for i in range(len(alist)):
        modifier_1 = abs(target_1[i] - alist[i])
        modifiers_1.append(modifier_1)
        max_mod_1 = max(max_mod_1, abs(modifier_1))

        modifier_2 = abs(target_2[i] - alist[i])
        modifiers_2.append(modifier_2)
        max_mod_2 = max(max_mod_2, abs(modifier_2))

    return min(max_mod_1, max_mod_2)



print sort_by_modifiers([5,4,3,2,8])  #3
print sort_by_modifiers([5,4,8,2,3])  #4
print sort_by_modifiers([8,4,3,2,5])  #5