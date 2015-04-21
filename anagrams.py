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
# - other approach, instead of sorting to a dict key.
#         - achar in string into a set (iterating = O(n)) * m words
#         - same use as key in dict
#             - set is unordered.  so equivalency should work (e,m,i,t)==(i,t,e,m).
#             - but set is mutable.  need to convert to tuple to be a key.  convert back to set O(m) for the comparison/equivalency.
#         - total:  (2m * n keys/comparisons)  * m dict insertion
#         ~ n linear time
# - then of course the final step is the output of the values.  Iterating over dict values.  + nlogn.  And the same for both approaches.

# choose:
# - approach 2.

##############################################################
# SOLUTION





