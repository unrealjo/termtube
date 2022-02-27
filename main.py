from tools import Search # My implementation instaed of pytube's one
import getopt, sys
import subprocess

opts, args = getopt.getopt(sys.argv[1:],"hdfr")
query= '+'.join(args) # join args with + as separator
pips = ('fzf', 'dmenu', 'rofi -dmenu') # List of programs to pip results to
if len(opts) > 0 : # means if the option is specified
    opt = opts[0][0]
else:
    opt = ''
def yt(search_query, pip2):
    vidIds, titles = Search(search_query).get_info()   

    # Writing results to temporary file
    file = open('/tmp/results', 'w') 
    i = 0
    for title in titles:
        file.write(f"{i} [{title}]\n") # Writing index and title of each video
        i += 1
    file.close()

    # Getting chose from user
    runer = subprocess.Popen(f"cat /tmp/results | {pip2}", shell=True, stdout=subprocess.PIPE)
    result = str(runer.stdout.read())
    index = int(result[2:3]) # Get index of selected video
    return "https://youtube.com/watch?v=" + vidIds[index] 

video = ''
if opt == '-h':
    print("""termtube [options] [search_query]
    -h : Help
    -d to get result in dmenu
    -f to get result in fzf
    -r to get result in rofi
    """)
elif opt == '-f':
    video = yt(query,pips[0])
    subprocess.run(['/bin/mpv', video])
elif opt == '-d':
    video = yt(query,pips[1])
    subprocess.run(['/bin/mpv', video])
elif opt == '-r':
    video = yt(query,pips[2])
    subprocess.run(['/bin/mpv', video])
elif opt == '':
    print("You need to specity an option")
