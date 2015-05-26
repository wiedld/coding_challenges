
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

    for num in range(1,N+1):
        if num%105 == 0:
            print "FizzBuzzWoof"
        elif num%35 == 0:
            print "BuzzWoof"
        elif num%21 == 0:
            print "FizzWoof"
        elif num%15 == 0:
            print "FizzBuzz"
        elif num%7 == 0:
            print "Woof"
        elif num%5 == 0:
            print "Buzz"
        elif num%3 == 0:
            print "Fizz"
        else:
            print num

solution(24)

solution(105)