from tools import Search  # My implementation instaed of pytube's one
from pytube import YouTube
import sys
import os
sys.argv.pop(0)  # removing file name from list of args
if len(sys.argv) == 0:
    print("No query query entered !")
else:
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
    videos = Search(patterns).get_link()
    for video in videos:
        print(f"{video} * {YouTube(video).title}")
    file.close()
