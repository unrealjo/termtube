import requests
import json
"""
I implemnted my own search class
bescause I found search class from pytube somehow slow
and a bit complecated :) and also for the seek of practicing
in python
"""


class Search():
    def __init__(self, search_query):
        self.query = search_query

    def get_info(self):
        infos = []
        r = requests.get(F'https://vid.puffyan.us/api/v1/search?q={self.query}')
        data = json.loads(r.content)
        lendata = len(data)
        for i in range(lendata):
            infos.append(data[i]['videoId'])
            infos.append(data[i]['title'])
        return infos, lendata
