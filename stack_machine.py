
# build the stack classes

class Stack(object):

    def __init__(self):
        self.top_layer = None

    def push(self, data):
        self.top_layer = StackLayer(data, self.top_layer)

    def pop(self):
        if self.top_layer is not None:
            value = self.top_layer.data
            self.top_layer = self.top_layer.previous
        else:
            value = None

        return value



class StackLayer(object):
    def __init__(self, data, previous):
        self.data = data
        self.previous = previous


#######################################################

# make the solution function

def solution(S):
    # make the calc stack
    calc_stack = Stack()

    # S is a string.
    operators = ["+", "*"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for achar in S:
        if achar in digits:
            calc_stack.push(int(achar))
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

        else:
            return "Error, string contains an invalid character."

    return calc_stack.pop()


print solution("13+62*7+*")

print solution("11++")