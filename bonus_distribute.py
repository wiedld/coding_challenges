


def retrieve_data(url):
    from urllib2 import urlopen

    response = urlopen(url)
    result = response.read()

    return eval(result)         # result is a list.  items are users.


def determine_num_following(result):
    print len(result)

    num_following_user = {}
    for user in result:
        who_tracking = user["tracks"]       # will return a list

        for tracked in who_tracking:
            if tracked not in num_following_user:
                num_following_user[tracked] = 1
            else:
                num_following_user[tracked] += 1

    return num_following_user


def make_list_account_types(result):

    acct_types = {}
    for user in result:
        accts = user.keys()       # will return a list

        for acct in accts:
            if acct not in acct_types:
                acct_types[acct] = 1
            else:
                acct_types[acct] += 1

    return acct_types


def determine_num_dev_accounts(result):

    num_accts = {}
    for user in result:            # each user is a dict of info
        accts = user.keys()       # will return a list

        user_id = user["keybase"]
        num_accts[user_id] = len(accts)

    return num_accts


def determine_max(adict,k):
    """takes a list of items, with values = int.
    returns a list of top items above 3 std threshold"""
    import numpy

    # list of numbers, of followers
    num_followers = adict.values()
    f_stats = numpy.array(num_followers)

    avg, stdev = f_stats.mean(), f_stats.std()
    threshold = avg + (k*stdev)

    return [k for k,v in adict.items() if v >= threshold]


################################################################


data = retrieve_data("https://keybase.io/jobs/q/b5c602f8306d711b?page=data")

# under the assumption that the most followed are influencers
num_following_user = determine_num_following(data)
list_most_followed = determine_max(num_following_user,3)
print len(list_most_followed)   #121

# under the assumption that we want to reward those with more accounts
# print make_list_account_types(data)
##  {'reddit': 6534, 'github': 25687, 'twitter': 24997,
# 'keybase': 44739, 'tracks': 44739, 'hackernews': 2866, 'pgp': 37128}
num_accts_ea_user = determine_num_dev_accounts(data)
most_accts = determine_max(num_accts_ea_user, 2)
print len(most_accts) # 1420

# num of those in common between two selection criteria so far
print len([user for user in most_accts if user in list_most_followed])  #16

# most number on github
#  https://developer.github.com/v3/users/followers/