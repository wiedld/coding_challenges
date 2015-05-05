
# recursive calls are log n
# merge is O(n) each time.
# final is n log n
def merge_sort(alist):
    if len(alist)==1:
        return alist

    midpt = len(alist)/2
    list1 = merge_sort(alist[:midpt])
    list2 = merge_sort(alist[midpt:])

    return merge_lists(list1, list2)



# bigO  O(n)
def merge_lists(list1, list2):
    output = []

    # if we had a list data structure which was not a linked list under the cover, then the pop function woudl cause 0(n) each time.
    # instead, let's use pointers.
    p1, p2 = 0, 0
    while len(list1)>p1 and len(list2)>p2:
        if list1[p1] > list2[p2]:
            output.append(list2[p2])
            p2 = p2 + 1
        else:
            output.append(list1[p1])
            p1 = p1 + 1

    # one of the lists is empty
    return output + list1[p1:] + list2[p2:]




test = [4,8,1,4,5,9,10,24,19,54]
print merge_sort(test)

