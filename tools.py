import urllib.request
import re
"""
I implemnted my own search class
bescause I found search class from pytube somehow slow
and a bit complecated :) and also for the seek of practicing
in python
"""


class Search():
    def __init__(self, search_query):
        self.query = search_query

    def get_link(self):
        html = urllib.request.urlopen(
            F"https://www.youtube.com/results?search_query={self.query}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        html.close()
        urls = []
        for i in range(5):
            urls.append(F"https://www.youtube.com/watch?v={video_ids[i]}")
        return urls
