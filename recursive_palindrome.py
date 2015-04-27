"""Take a string, and return its palindrome.  Handles spaces and caps.  Use recursion"""

# base case = atring len = 0
# state tracked with output, sliced astring


def palindrome(astring):
    astring = astring.replace(" ","").lower()
    return astring == reverse(astring)



def reverse(astring, output=""):
    if len(astring) == 0:
        return output

    output = astring[0] + output
    return reverse(astring[1:], output)



print palindrome("kayak")
print palindrome("aibohphobia")
print palindrome("Live not on evil")
print palindrome("Able was I ere I saw Elba")
print palindrome("not a palindrome")

