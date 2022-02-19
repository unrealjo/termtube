from tools import Search # My implementation instaed of pytube's one
import sys

sys.argv.pop(0)  # removing file name from list of args
patterns = ""
count = -1
"""
count variable is used to count number of spaces
in our query string
I set it to -1 to not count the last space
"""
for item in sys.argv:
    patterns += item + " "  # separate argumment
    count += 1
patterns = patterns.replace(" ", "+", count)  # transform space to "+"
vidIds, num = Search(patterns).get_info()   
for i in range(0 ,num*2 ,2):
    print(F"{vidIds[i]} [{vidIds[i+1]}]")
