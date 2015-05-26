# APPROACH:
# - first pass, make dict with k=num and v = [] of idx positions
#
# - pass over dict
#     - if len(v) > 1:
#         spread = abs(v[0]-v[-1])
#         max_spread = max(max_spread, spread)

def solution(A):

    nums_dict = {}
    for idx in range(len(A)):
        key = str(A[idx])
        if key in nums_dict:
            nums_dict[key].append(idx)
        else:
            nums_dict[key] = [idx]

    max_spread = 0
    for k,v in nums_dict.items():
        if len(v) > 0:
            spread = abs(v[0]-v[-1])
            max_spread = max(max_spread, spread)


    return max_spread


A = [4,6,2,2,6,6,1]
print solution(A)