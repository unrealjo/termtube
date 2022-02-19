# termtube
Search Youtube videos from terminal
# Requirements
- [pytube](https://github.com/pytube/pytube/blob/master/docs/index.rst)
- [fzf](https://github.com/junegunn/fzf) (optional)
- [mpv](https://mpv.io/installation/) (optional)
- [python3.x](https://www.python.org/downloads/)
# Notes
- you can install [pytube](https://github.com/pytube/pytube/blob/master/docs/index.rst) using :
```bash
    pip install pytube
```
- Currently this programs shows first 8 results in order to speed run time
# Usage
From you terminal :
```bash
    python3 termtube.py [search_query]
```
This one returns a list of available videos then you can pipe it to fzf the mpv.
- this programm is tested under linux/unix machine
# Todo
- [ ] Support for Windows
- [ ] Optimization
