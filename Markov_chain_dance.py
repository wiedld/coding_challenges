

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


##################################################
##################################################
# HOW DFS WORKS

node_B = Node("B")
node_C = Node("C")

node_A = Node("A", node_B, node_C)


def print_DFS(node):
    if node == None:
        print "no node"
        return

    print node.data

    print_DFS(node.left)
    print "come back up from left"
    print_DFS(node.right)
    print "come back up from  right"


print_DFS(node_A)

print "######################################"


##################################################
##################################################
# PASSING A STATE VARIABLE

n4, n3, n6, n2 = Node(4), Node(3), Node(6), Node(2)

n7 = Node(7, n4, n3)
n9 = Node(9, n6, n2)

n5 = Node(5, n7, n9)


#### WRONG WAY ####
# found is beind passed as what it is at that moment the recursive call is done

# def find_data(node, find=3, found=False):
#     # base case
#     if node == None:
#         return

#     # see the current node
#     print node.data, found

#     # base case
#     if node.data == find:
#         print "FOUND IT!!!!"
#         found = True
#         return

#     if found != True:
#         find_data(node.left, find, found)
#         find_data(node.right, find, found)


#### CORRECT WAY ####
# found is returned, and redefined, by all the recursive calls to child nodes

def find_data(node, find=3, found=False):
    # BASE CASE == when to stop, and go back up
        # fail condition
        # success condition
    # base case
    if node == None:
        return found

    # see the current node
    print node.data, found

    # base case
    if node.data == find:
        print "FOUND IT!!!!"
        return True

    # STATE VARIABLES = WHAT YOU ARE TRACKING!!!!
        # found = True, False.
        # return the state variable

    # RECURSIVE CALL
    if found != True:
        found = find_data(node.left, find, found)

    if found != True:
        found = find_data(node.right, find, found)

    return found


find_data(n5)

print "######################################"


##################################################
##################################################
# STATE VARIABLES -
    # option #1 = as copies (string visited)
        # each node gets it's own copy, which it modifies.
        # child gets the copy from parent. and does not see changes made by siblings.
    # option # 2 - as array pointers (success).
        # all nodes can access this array!


class Node2(object):

    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


poss = ["rar",'yo',"gory","joy","sam"]
max_steps = 3

poss = {"rar": ["yo", "gory"],
        "joy": ["gory", 'rar', 'rar']}


def build_all_dance_choices(curr_step=0, visited=None, success=None):
    # if first time, no steps yet taken
    if visited == None:
        visited = ""
        success = []

    # conditions to fail!!!!


    # Base case = if we have taken enouguh steps, without failing == SUCCESS
    if curr_step >= max_steps:
        success.append(visited)
        return success

    curr_step += 1

    for p in poss:
        build_all_dance_choices(curr_step, visited+","+p, success)

    return success


print build_all_dance_choices()
# outcome --> could choose a random dance path (visited string) from within the success array

print "######################################"


##################################################
##################################################
# RANDOM WALKS -- on a tree.

# this is one method. Not necessarily the best way!

from random import choice


n_grams = {"rar": ["gory", "joy", "sam"],
            "yo": ["rar", "rar", "joy"],
            "gory": ["gory", "gory", "sam"],
            "joy": ["joy", "rar", "rar"],
            "sam": ["sam", "sam", "yo"]
            }

max_counts = 64
counts_per_step = {'rar': 2, "yo": 4, "gory": 4, "joy": 8, "sam": 12}


def build_dance_random_walks(visited, found=False):
    print "VISITED:", visited

    # BASE CASE # 1 = bubbling back up the stack
    if found == True:
        return found, visited

    # BASE CASE # 2 = CONDITIONS TO FAIL
        # ELY HAS RULES!  could be fail conditions written here.
    if fail_conditions(visited):
        print "FAILED CONDIITONS"
        visited.pop(-1)
        return found, visited

    # BASE CASE # 3 = SUCCESS!!!!
    if get_total_counts(visited) == max_counts:
        found = True
        return found, visited

    # UPDATING THE STATE -> next dance steps
    last_step = visited[-1]
    tried_next_steps = set()
    # while all possible steps not exhausted:
    while (tried_next_steps != set(n_grams[last_step])) and (found == False):
        next_step = choice(n_grams[last_step])
        visited.append(next_step)
        tried_next_steps.add(next_step)
        found, visited = build_dance_random_walks(visited, found)

    # BACK TRACKING -> go back an extra step
    if found != True:
        print "BACK TRACKED"
        visited = visited[:-2]

    return build_dance_random_walks(visited, found)


def get_total_counts(steps_list):
    """helper funct. Get total counts thus far."""
    return sum([counts_per_step[step] for step in steps_list])


def fail_conditions(steps_list):
    """helper funct. Failure condition. return True if failed."""
    # ONE FAIL CONDIITON = too long, past 64 steps
    total_counts = sum([counts_per_step[step] for step in steps_list])

    # SECOND FAIL CONDITION = a single step is repeated more than 5 times within the sequence
    count_step_types = {step: steps_list.count(step) for step in steps_list}
    max_repeated = max(count_step_types.values())

    # check fail conditions
    if (total_counts > max_counts) or max_repeated >= 5:
        return True     # failed
    else:
        return False    # did not fail


first_step = choice(n_grams.keys())
result = build_dance_random_walks([first_step])
print "\nFINAL RESULT:", result

print "######################################"

