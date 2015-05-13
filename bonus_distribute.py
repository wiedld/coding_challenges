# OBJECTIVE:
#
#     - have 1000TB to distribute.
#     - to not dilute impact, distribute 1-2 TB each to winners
#     - id no more than 1000 winners, return list of keybase userid
#
# calculations with assumption at the bottom of the file.
# Total time spend ~4.5 hours.  Definitely could have been better.

# APPROACH
#
    # MOST FOLLOWED ON KEYBASE
    # return 247 - take all 247
    # assume these are influencers on keybase.  Good morale.

    # KEYBASE - MOST ACCTS
    # returned 1420
    # under the assumption that we want to reward those with more accounts

    # GITHUB  - MOST FOLLOWED
    # due to api rate limitation, only check for for sub-set of keybase users, who use service
    # returned 444

    # DETERMINE MOST LIKELY ACTIVE IN SOCIAL MEDIA:
    # returns 1666, of which the majority are already in the most_accts (then ck'ed on github)
    # therefore, did not include this dataset in final determination.


# RESULT -- list of 664 keybase users, who are:
#     - most followed on keybase, and/or
#     - most accts, and most followed on github, and/or
#     - if have one of the above, then 1x bonus storage
#     - if have two of the above, then 2x bonus storage
#     - divide up 1 TB accordingly


# RETURNS - json array of users, with bonus amounts

################################################################
from urllib2 import urlopen
import json
import numpy
import sys

# my tokens.  Other users need to source their own tokens.
import os
client_id = os.environ["CLIENT_ID"]
client_token = os.environ["CLIENT_SECRET"]

################################################################
# GET DATA - json.   works with the two data sources used (keybase, github).

def retrieve_data(url):

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


# LIKELY SOCIAL MEDIA PARTICIPANT - keybase - not just based on num accts
def determine_most_media(result):
    many_social_media = []
    for user in result:            # each user is a dict of info
        if "reddit" in user and "hackernews" in user and "twitter" in user:
            many_social_media.append(user["keybase"])

    return many_social_media


################################################################

# used once -- to find all the kinds of dev accts, and frequency of acct

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


    ##  {'reddit': 6534, 'github': 25687, 'twitter': 24997,
    # 'keybase': 44739, 'tracks': 44739, 'hackernews': 2866, 'pgp': 37128}

################################################################
##  ANALYTICS ##


def determine_max(adict,k):
    """takes a list of items, with values = int.
    returns a list of top items above 3 std threshold"""

    # list of numbers, of followers
    num_followers = adict.values()
    f_stats = numpy.array(num_followers)

    avg, stdev = f_stats.mean(), f_stats.std()
    threshold = avg + (k*stdev)

    return [k for k,v in adict.items() if v >= threshold]


################################################################

def main(path):
    data = retrieve_data(path)

    # MOST FOLLOWED ON KEYBASE
    # return 247 - take all 247
    # assume these are influencers on keybase.  Good morale.
    keybase_num_following_user = determine_num_following_keybase(data)
    list_most_followed = determine_max(keybase_num_following_user,2)

    # KEYBASE - MOST ACCTS
    # returned 1420
    # under the assumption that we want to reward those with more accounts
    num_accts_ea_user = determine_num_dev_accounts(data)
    most_accts = determine_max(num_accts_ea_user, 2)

    # GITHUB  - MOST FOLLOWED
    # due to api rate limitation, only check for for sub-set of keybase users, who use service
    # returned 444
    github_num_following_user = determine_num_following_github(data, users_to_ck_github)
    github_most_followed = determine_max(github_num_following_user,1)

    # DETERMINE MOST LIKELY ACTIVE IN SOCIAL MEDIA:
    # returns 1666, of which the majority are already in the most_accts (then ck'ed on github)
    social_media_users = determine_most_media(data)

    # FINAL BATCH OF USERS
    final_list = []
    final_list.extend(list_most_followed)
    final_list.extend(github_most_followed)
    # final_list.extend(social_media_users)

    # DETERMINE BONUS AMTS
    pt_awards = {}
    for user in final_list:
        if user in pt_awards:
            pt_awards[user] += 1
        else:
            pt_awards[user] = 1

    total_bonus_pts = len(final_list)
    bonus_per_pt = 1000.00/total_bonus_pts

    bonus_amts = []
    for user, pt in pt_awards.items():
        final_award = round(pt * bonus_per_pt,3)
        bonus_amts.append( {"keybase": user, "bonus": final_award} )

    return json.dumps(bonus_amts)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        p = sys.argv[1]
    else:
        p = "https://keybase.io/jobs/q/b5c602f8306d711b?page=data"

    print main(p)
