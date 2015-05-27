
# build the stack class

class Stack(object):

    def __init__(self):
        self.data = []

    def push(self, data):
        self.append(data)

    def pop(self):
        value = self.data.pop(-1)
        return value



#######################################################

# make the solution function

def solution(S):
    # make the calc stack
    calc_stack = Stack()

    # S is a string.
    operators = ["+", "*"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for achar in S:
        # what to do if an integer
        if achar in digits:
            calc_stack.push(int(achar))

        # what to do if an operator
        elif achar in operators:
            value_1 = calc_stack.pop()
            value_2 = calc_stack.pop()

            if value_1 is None or value_2 is None:
                return 'Error.  String is not valid'

            if achar == "*":
                prod = value_1 * value_2
            else:
                prod = value_1 + value_2
            calc_stack.push(prod)

        # what to do if not a recognizable character
        else:
            return "Error, string contains an invalid character."

    return calc_stack.pop()


print solution("13+62*7+*")
print solution("11++")