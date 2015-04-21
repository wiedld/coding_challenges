# PROBLEM:

# An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and "tops".

# Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.

# The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.

# The output produced by your code should be in this format:

# emit, item, mite, time
# merit, miter, mitre, remit, timer
# reins, resin, rinse, risen, serin, siren
# inert, inter, niter, retin, trine
# inset, neist, snite, stein, stine, tsine

#################################################################
# # APPROACH:

# given:
# - a file path (funct param)
# - file is a dictionary.  Assuming in the sense of a conventional dictionary (listing all words) and not the data structure per se.
# - 1 line per word

# output:
# - all possible anagrams
# - with 4 plus words

# approach:
# - if len < 4, then skip
# - conventional approach: using a dict.
#         - place sorted word as the key,
#         - the unsorted word as a value in the listing
#         - sorting time - best sorting is O(nlogn).  * m words
#         - insertion time = O(1), has table, per m= words to insert.
#         - total:  m(nlogn) sorting * m dict insertion.
#         ~  nlogn time.

# - then of course the final step is the output of the values.  Iterating over dict values.  + nlogn.  And the same for both approaches.

# choose:
# - approach 1.   **updated choice of approach**

##############################################################
# SOLUTION


def id_anagrams_in_file(path):
    """takes file path.  returns a list of lists, with each nested list of anagrams"""
    dict_anagrams = {}

    with open(path) as f:
        for word in f:      # each line = word
            word = word.strip() # clean out whitespace

            if len(word) >= 4:       # metadata.  O(1)
                key = sort_str(word)

                if key not in dict_anagrams:
                    dict_anagrams[key] = [word]
                else:
                    dict_anagrams[key].append(word)

    # create output list from dict_anagrams
    #  is not an "anagram" unless there is more than 1 value in

    for list_values in dict_anagrams.values():
        print ", ".join(map(str,list_values))






def sort_str(astring):
    """ input string.  output ordered string for dict keys"""
    key =', '.join(sorted(astring))
    # sorted returns as a listed, then join to string again.

    return key




test = "test.txt"
id_anagrams_in_file(test)











