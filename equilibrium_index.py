# PROBLEM
#
# A zero-indexed array A consisting of N integers is given.
# An equilibrium index of this array is any integer P such that
# 0 <= P < N and the sum of elements of lower indices is equal to
# the sum of elements of higher indices

#
# Write a function:
#
# def solution(A)
#
# that, given a zero-indexed array A consisting of N integers,
# returns any of its equilibrium indices.
# The function should return -1 if no equilibrium index exists.
#
# For example, given array A shown above, the function may return 1, 3 or 7, as explained above.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range
# [-2,147,483,648,2,147,483,647].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.
#
#
# APPROACH
#
#     - goal: return one, any one, of the equilibrium points
#             if no equilibrium index, then return -1
#
#     - linear time
#         - go through entire list once, and sum all values (total)
#         - then go through second time, keeping track of:
#             sum_so_far
#             curr_value
#             remaining (total - (sum_so_far + curr_value) )
#         - if at any pt sum_so_far == remaining, return curr index
#         - once hit end, return -1
#

##################################################

def solution(A):
    # early exit
    if len(A) <= 1:
        return -1

    # get total
    total = sum(A)

    # find poss equilibrium pt
    sum_so_far = 0

    for i in range(len(A)):
        remaining = total - (A[i] + sum_so_far)

        if sum_so_far == remaining:
            return i

        sum_so_far += A[i]

    return -1


print solution([-1,3,-4,5,1,-6,2,1])
