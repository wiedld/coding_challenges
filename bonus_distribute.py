


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
    print len(result)

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


def determine_max(adict):
    """takes a list of items, with values = int.
    returns a list of top items above 3 std threshold"""
    import numpy

    # list of numbers, of followers
    num_followers = adict.values()
    f_stats = numpy.array(num_followers)

    avg, stdev = f_stats.mean(), f_stats.std()
    threshold = avg + (3*stdev)

    return [k for k,v in adict.items() if v >= threshold]


################################################################


data = retrieve_data("https://keybase.io/jobs/q/b5c602f8306d711b?page=data")

# under the assumption that the most followed are influencers
num_following_user = determine_num_following(data)
List_most_followed = determine_max(num_following_user)

# under the assumption that we want to reward those with more accounts
print make_list_account_types(data)