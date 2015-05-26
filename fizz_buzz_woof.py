

def solution(N):
    """given N.  Print out 1->N, but replacing ints based on the rules:
        if divisible by 3 -> Fizz
        by 5 -> Buzz
        by 7 -> Woof
        by combo, cancat (3,5 -> FizzBuzz)"""

    # 15 is 3*5
    # 21 is 3*7
    # 35 is 5*7
    # 105 is 3*5*7

    # make list of nums
    results = [x for x in range (1,N+1)]

    # replace for multiples of variables
    results = word_replace(results, 3, "Fizz")
    results = word_replace(results, 5, "Buzz")
    results = word_replace(results, 7, "Woof")
    results = word_replace(results, 21, "FizzWoof")
    results = word_replace(results, 35, "BuzzWoof")
    results = word_replace(results, 105, "FizzBuzzWoof")

    # print out result
    for item in results:
        print item


def word_replace(num_list, factorial, word):
    multiple = 1

    # replace at indexed location
    while (multiple*factorial) <= len(num_list):
        index = (multiple * factorial)-1    # list is 1->N
        num_list[index] = word
        multiple += 1

    return num_list


solution(24)
solution(105)
solution(2000000)

