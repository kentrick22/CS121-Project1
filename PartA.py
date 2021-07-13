############################################################################
##  PART A: Word Frequencies:                                             ##
##   Description:                                                         ##
##      Run on command line using command:                                ##
##          python PartA.py [filename]                                    ##
##   Input: [filename] - the path to a txt file                           ##
##   Output: prints tokens and frequencies                                ##
##                                                                        ##
##   Source: https://canvas.eee.uci.edu/courses/32171/assignments/623046  ##
##   (Header Uploaded by Will Schallock, last updated 1/5/21)             ##
##                                                                        ##
##                                                                        ##
##   Online Resource:                                                     ##
##      - https://stackoverflow.com/questions/15371691/how-to-sort-a-     ##
##          dictionary-by-value-desc-then-by-key-asc                      ##
############################################################################

import sys

#TODO: write classes/methods/functions for PART A here
############################################################################
##  tokenize(argument_position)                                           ##
##  This function takes an integer that indicates argument position in    ##
##  the command line for the text file being read.                        ##
##                                                                        ##
##  This function is linear time relative to the size of the input. This  ##
##  is because there is no nested for loops or while loops. This can also ##
##  be proved by calculating the total of the big-O notation:             ##
##     O(1)+(O(1)*O(N)*O(1)*O(1)*O(1)*O(1)*O(1)*O(1)*O(1))+O(N)+O(N)+O(N) ##
##     +O(1) = O(N)                                                       ##
############################################################################
def tokenize(argument_position):
    final_string = []                                                       #O(1)

    with open(sys.argv[argument_position], 'r') as f:                       #O(1)
        while True:                                                         #O(N)
            temp_char = f.read(1).lower()                                   #O(1)
            if not temp_char:                                               #O(1)
                break #End Of File                                          #O(1)
            elif temp_char in 'abcdefghijklmnopqrstuvwxyz1234567890 ':      #O(1)
                final_string.append(temp_char)                              #O(1)
            elif temp_char not in 'abcdefghijklmnopqrstuvwxyz1234567890 ':  #O(1)
                final_string.append(' ')                                    #O(1)

    #Join all characters together and then split by whitespace
    final_string = "".join(final_string)                                    #O(N)
    final_string = list(final_string.split(" "))                            #O(N)
    #Remove unnecessary whitespaces left
    final_string = [sub for sub in final_string if sub != '']               #O(N)

    return final_string                                                     #O(1)

############################################################################
##  compute_word_frequencies(tokenized_list)                              ##
##  This function takes a list of tokens. The function loop through the   ##
##  list and then count their frequencies. The frequencies are stored     ##
##  in dictionary which will then be returned.                            ##
##                                                                        ##
##  This function is linear time relative to the size of the input. This  ##
##  is because there is no nested for loops or while loops. This can also ##
##  be proved by calculating the total of the big-O notation:             ##
##      O(1)+(O(N)*O(len(frequency_dict))*O(1)*O(len(frequency_dict))*    ##
##      O(1))+O(1) = O(N)                                                 ##
############################################################################
def compute_word_frequencies(tokenized_list):
    frequency_dict = {}                                                     #O(1)
    for i in tokenized_list:                                                #O(N)
        if i not in frequency_dict:                                         #O(len(frequency_dict))
            frequency_dict[i] = 1                                           #O(1)
        elif i in frequency_dict:                                           #O(len(frequency_dict))
            frequency_dict[i] += 1                                          #O(1)

    return frequency_dict                                                   #O(1)

############################################################################
##  printt(frequency_dict)                                                ##
##  This function takes a dictionary of the frequencies of the tokens.    ##
##  The function will first sort the dictionary using sorted() function   ##
##  and save the sorted list in sorted_list variable. The sorted_list     ##
##  will then be printed using for loop.                                  ##
##                                                                        ##
##  This function is quasiliniear time relative to the size of the input. ##
##  Python's sorted() function is basically O(N log N). Calculating the   ##
##  total of the big-O notation will give us a quasiliniear time:         ##
##      O(N log N)+(O(N)*O(1)) = O(N log N)                               ##
############################################################################
def printt(frequency_dict):
    #Sort
    sorted_list = sorted(frequency_dict.items(), key=lambda item: (-item[1], item[0]))  #O(N log N)

    #Print
    for i in sorted_list:                                                   #O(N)
        print("{}\t{}".format(i[0], i[1]))                                  #O(1)


if __name__ == "__main__":
    #TODO: call functions/ initalize class object/ call methods for PART A here
    printt(compute_word_frequencies(tokenize(1)))
