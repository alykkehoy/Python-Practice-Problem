# Problem as I remembered it:
# read file
# get unique words
# output unique words to file in csv format

# Questions I should have asked:
# 1. Does capitalization matter? aka are "Apple" and "apple" unique?
# 2. When we output to our new file do we care about the order? aka read in: a b c write out: b, c, a

import csv
import re

def readFile(fileName):
    wordString = ""
    with open(fileName, 'r') as f:
        wordString = f.read()
    return wordString

def parseFile(wordString):
    # only issue with this is if you had a string like "a\nb" it would not split.
    # After checking stackoverflow, I found you can use pythons regex library to split
    # a string meaning you could split on somethign like ' +|\n+|\t+' to catch that.

    # words = re.split(' +|\n+|\t+', wordString)

    words = wordString.split(" ")

    map = {}
    uniqueWords = []

    for word in words:
        if map.get(word) == None:
            # I found out you could just print the keys from the dictionary
            # but this was my thought process during the interview, so I implemented that way first
            # I also learned I could have done this way simpler with a set since sets are forced to have unique values
            # and have included that implementation below as parseFileNew
            map[word] = True
            uniqueWords.append(word)

    return uniqueWords


# After a quick google this is how I would have done it in python.
# Only issue that might arise is if order of the words matters. If so
# chainging the list of strings into a set would not work since theres 
# no guarantee they are kept in order.
def parseFileNew(wordString):
    words = re.split(' +|\n+|\t+', wordString)
    uniqueWords = set(words)

    return uniqueWords

# This is the implementation I described in the interview.
# I did discover theres a csv library that makes this way easier. 
# The implementation using that is provided below as outputFileNew.
def outputFile(fileName, fileText):
    with open(fileName, 'w') as f:
        for i in range(len(fileText) - 1):
            f.write(fileText[i] + ", ")

        # As I was working on this I realized this is bad since I did not make sure the length
        # of the fileText list was greater than 0. Leading to the possibility that I would be accessing
        # filetext[-1] which in and of its self inst bad since you can access negative indexes as elements from 
        # the end of the list, but to get to this state the length would have had to be 0 leading to an 
        # index out of bounds.
        f.write(fileText[len(fileText) - 1])

    return

def outputFileNew(fileName, fileText):
    with open(fileName, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fileText)

    return

def main():
    wordString = readFile("./test_file.txt")

    # original functions as I described in the interview
    uniqueWords = parseFile(wordString)
    outputFile("./unique.csv", uniqueWords)

    # updated functions after doing a little research
    uniqueWords = parseFileNew(wordString)
    outputFileNew("./unique_new.csv", uniqueWords)

if __name__ == "__main__":
    main()