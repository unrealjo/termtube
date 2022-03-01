from subprocess import run, PIPE, Popen
from requests import get
from json import loads
import argparse

"""
I implemnted my own search class
bescause I found search class from pytube somehow slow
and a bit complecated :) and also for the seek of practicing
in python
It's not a fork of yt-fzf !!
"""

def search(query, pipe_to):
    video_id = []
    titles = []
    resut_query = get(F'https://vid.puffyan.us/api/v1/search?q={query}')
    data = loads(resut_query.content)
    for i in range(len(data)):
            video_id.append(data[i]['videoId'])
            titles.append(data[i]['title'])

    # Writing results to temporary file
    file = open("/tmp/results","w", encoding="utf-8")
    i = 0
    for title in titles:
        file.write(f"{i} [{title}]\n") # Writing index and title of each video
        i += 1
    file.close()

    # Getting chose from user
    get_chosed_videoId = Popen(f"cat /tmp/results | {pipe_to}", shell=True, stdout=PIPE)
    result = str(get_chosed_videoId.stdout.read())
    index = int(result[2:3]) # Get index of selected video
    return "https://youtube.com/watch?v=" + video_id[index] 

# Thaks to awesome people over reddit (r/python)

parser = argparse.ArgumentParser(description="Search and play Youtube videos from CLI")
parser.add_argument("query", type=str , help="Query to search for", nargs='+')
parser.add_argument("-f", default=False, action="store_true", help="Run throught fzf")
parser.add_argument("-d", default=False, action="store_true", help="Run throught dmenu")
parser.add_argument("-r", default=False, action="store_true", help="Run throught rofi")
args = parser.parse_args()

video = ''
query = '+'.join(args.query)
if args.d:
    video = search(query,'dmenu')
if args.f:
    video = search(query,'fzf')
if args.r:
    video = search(query,'rofi -dmenu')
if video != '':
    run(['/bin/mpv', video])

