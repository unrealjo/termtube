from tools import Search # My implementation instaed of pytube's one
import getopt, sys
import subprocess

opts, args = getopt.getopt(sys.argv[1:],"hdfr")
query= '+'.join(args) # join args with + as separator
pips = ('fzf', 'dmenu', 'rofi -dmenu') # List of programs to pip results to
if len(opts) > 0 : # means if the option is specitied
    opt = opts[0][0]
else:
    opt = ''
def yt(search_query, pip2):
    vidIds, num = Search(search_query).get_info()   

    # Writing results to temporary file
    file = open('/tmp/results', 'w') 
    for i in range(0 ,num*2 ,2):
        file.write(f"{vidIds[i]} [{vidIds[i+1]}]\n")
    file.close()

    # Getting chose from user
    runer = subprocess.Popen(f"cat /tmp/results | {pip2}", shell=True, stdout=subprocess.PIPE)
    result = str(runer.stdout.read())
    return "https://youtube.com/watch?v=" + result[2:13] 

video = ''
if opt == '-h':
    print("""termtube [options] [search_query]
    -h : Help
    -f to get result in fzf
    -d to get result in dmenu
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
