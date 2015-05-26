

def solution(N):
    """given N.  Print out 1->N, but replacing ints based on the rules:
        if divisible by 3 -> Fizz
        by 5 -> Buzz
        by 7 -> Woof
        by combo, cancat (3,5 -> FizzBuzz)"""

    # make list of nums
    results = [x for x in range (1,N+1)]

    # replace for multiples of variables
    results = word_replace(results, 3, "Fizz")
    results = word_replace(results, 5, "Buzz")
    results = word_replace(results, 7, "Woof")

    # print out result
    for item in results:
        print item


def word_replace(num_list, factorial, word):
    multiple = 1

    # replace at indexed location
    while (multiple*factorial) <= len(num_list):
        index = (multiple * factorial)-1    # list is 1->N

        if type(num_list[index]) == int:
            num_list[index] = word
        else:
            num_list[index] = num_list[index] + word
        multiple += 1

    return num_list


solution(24)
solution(105)
solution(2000000)

