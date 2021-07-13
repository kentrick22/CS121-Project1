############################################################################
##  Part B: Intersection of two files:                                    ##
##   Description:                                                         ##
##      Run on command line using command:                                ##
##          python PartB.py [filename1] [filename2]                       ##
##   Input: [filename1] - the path to a txt file                          ##
##          [filename2] - the path to a txt file                          ##
##   Output: prints the number of tokens file1 and file2 have in common   ##
##                                                                        ##
##   Source: https://canvas.eee.uci.edu/courses/32171/assignments/623046  ##
##   (Header Uploaded by Will Schallock, last updated 1/5/21)             ##
############################################################################

#TODO: *optional* import classes/methods/functions from PartA you want to reuse in PartB
from PartA import tokenize

#TODO: write classes/methods/functions for PartB here
############################################################################
##  find_intersection(list1, list2)                                       ##
##  This function takes two lists. The function converts the two lists    ##
##  into two sets. It will then return the length of the intersection     ##
##  between the two sets.                                                 ##
##                                                                        ##
##  This function is linear time relative to the size of the input. This  ##
##  can be proved by calculating the total of the big-O notation:         ##
##      O(N)+O(N)+O(N) = O(N)                                             ##
############################################################################
def find_intersection(list1, list2):
    set1 = set(list1)                                                       #O(N)
    set2 = set(list2)                                                       #O(N)

    return len(set1.intersection(set2))                                     #O(N)

if __name__ == "__main__":
    #TODO: call functions/ initalize class object/ call methods for PART B here
    list1 = tokenize(1)
    list2 = tokenize(2)

    print(find_intersection(list1, list2))
