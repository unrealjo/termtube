import urllib.request
import re
from pytube import YouTube
import sys
search = ""
count = -1
"""
count variablr is used to count number of spaces
in our search string
I set it to -1 because the last iteration
 in the loop adds a space at the end of search string
and I don't want to count it
"""
sys.argv.pop(0)  # removing file name from list of args
for item in sys.argv:
    search += item + " "
    count += 1
search = search.replace(" ", "+", count)  # transform space to "+"
html = urllib.request.urlopen(
    F"https://www.youtube.com/results?search_query={search}")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
html.close()
for i in range(5):
    url = F"https://www.youtube.com/watch?v={video_ids[i]}"
    print(url, "*", YouTube(url).title)
