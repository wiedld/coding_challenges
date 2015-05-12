# OBJECTIVE:
#
#     - have 1000TB to distribute.
#     - to not dilute impact, distribute 1 TB each to winners
#     - id no more than 1000 winners, return list of keybase userid
#
# calculations with assumption at the bottom of the file.
# Total time spend ~4.5 hours.  Definitely could have been better.

# RESULT -- list of 664 keybase users


################################################################


# GET DATA - json.   works with the two data sources used (keybase, github).
def retrieve_data(url):
    from urllib2 import urlopen
    import json

    response = urlopen(url)
    result = response.read()

    output = json.loads(result)

    return output


################################################################
##  RAW COUNTS ##


# NUM FOLLOWING - keybase
def determine_num_following_keybase(result):

    num_following_user = {}
    for user in result:
        who_tracking = user["tracks"]       # will return a list

        for tracked in who_tracking:
            if tracked not in num_following_user:
                num_following_user[tracked] = 1
            else:
                num_following_user[tracked] += 1

    return num_following_user


# NUM FOLLOWING - github
def determine_num_following_github(result, users_most_accts):
    """github doc: https://developer.github.com/v3/users/followers/"""
    import os
    client_id = os.environ["CLIENT_ID"]
    client_token = os.environ["CLIENT_SECRET"]

    num_following_user = {}

    for user in result:
        keybase_id = user["keybase"]

        if "github" in user and keybase_id in users_most_accts:
            github_id = user["github"]

            print "api call for:", github_id
            try:
                url = "https://api.github.com/users/%s/followers?client_id=%s&client_secret=%s" % (github_id, client_id, client_token)
                github_data = retrieve_data(url)
                num_following_user[keybase_id] = len(github_data)
            except:
                pass

    return num_following_user


# NUM OF DEV ACCTS - keybase
def determine_num_dev_accounts(result):

    num_accts = {}
    for user in result:            # each user is a dict of info
        accts = user.keys()       # will return a list

        user_id = user["keybase"]
        num_accts[user_id] = len(accts)

    return num_accts


# used once -- to find all kinds of dev accts, and frequency of acct
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


################################################################
##  ANALYTICS ##


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

def main():
    data = retrieve_data("https://keybase.io/jobs/q/b5c602f8306d711b?page=data")

    # MOST FOLLOWED ON KEYBASE
    # return 247 - take all 247
    # assume these are influencers on keybase.  Good morale.
    keybase_num_following_user = determine_num_following_keybase(data)
    list_most_followed = determine_max(keybase_num_following_user,2)
    print len(list_most_followed)

    # KEYBASE - MOST ACCTS
    # returned 1420
    # under the assumption that we want to reward those with more accounts
    # print make_list_account_types(data)
    ##  {'reddit': 6534, 'github': 25687, 'twitter': 24997,
    # 'keybase': 44739, 'tracks': 44739, 'hackernews': 2866, 'pgp': 37128}
    num_accts_ea_user = determine_num_dev_accounts(data)
    most_accts = determine_max(num_accts_ea_user, 2)
    print len(most_accts)

    # num of those in common between two selection criteria so far
    print len([user for user in most_accts if user in list_most_followed])  #33
    # therefore, do not limit the keybase influences

    # GITHUB  - MOST FOLLOWED
    # due to api rate limitation, only check for followers of those with many keybase accts
    # returned 444
    github_num_following_user = determine_num_following_github(data, most_accts)
    github_most_followed = determine_max(github_num_following_user,1)
    print len(github_most_followed)


    # FINAL BATCH
    final_list = []
    final_list.extend(list_most_followed)
    final_list.extend(github_most_followed)
    final_set = set(final_list)

    return final_set, len(final_set)


print main()