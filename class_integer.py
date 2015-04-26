"""Purpose: to use stacks as a method to convert integers between different expressions (binary, hexadecimal).  Include class inheritance, and reusable functions & data structures."""


class Stack(object):
    def __init__(self):
        self.conversion_array=[]

    def push(self, num):
        self.conversion_array.append(num)

    def pop(self):
        value = self.conversion_array[-1]
        self.conversion_array = self.conversion_array[:-1]
        return value

    def isEmpty(self):
        return len(self.conversion_array) == 0




# subclass integer.  Inherits the stack and associated methods.
class Integer(Stack):
    def __init__(self, data):
        self.data = data

    def hexadecimal(self):
        num = self.data
        hexidec_chart="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.conversion_array=[]

        self.fill_stack(num, 16, hexidec_chart)
        return self.expression_from_stack()

    def binary(self):
        num = self.data
        binary_chart="01"
        self.conversion_array=[]

        self.fill_stack(num, 2, binary_chart)
        return self.expression_from_stack()


    # helper function for any int conversion to another format.
    def fill_stack(self, num, base, conversion_chart):
        """takes any base, and any conversion chart.  Returns a stack with the correct values in each stack layer"""
        while num > 0:
            idx = num%base
            self.push(conversion_chart[idx])
            num = num/base
        return

    # helper function for any int conversion to another format.
    def expression_from_stack(self):
        """takes the stack (associated with self), and returns the converted expression"""
        result = ""
        while self.isEmpty() != True:
            result = result + self.conversion_array.pop()
        return result




test = Integer(233)
print test.hexadecimal()    # E9
print test.binary()         # 11101001
test2 = Integer(1465)
print test2.hexadecimal()    # 5B9
print test2.binary()         # 10110111001

