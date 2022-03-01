# This program is to open web browser and search for 4k live videos and play

import webbrowser
import urllib.request
import re

# Opening the Browser
#webbrowser.open('https://www.youtube.com')

# Search for 4k live videos
searchKeyword1 = "4k_live_stream"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeyword1)

# Search for live news
#searchKeyword2 = "live_news"
#html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeyword2)

# picking the videos
live_video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
#live_news = re.findall(r"watch\?v=(\S{11})", html.read().decode())


webbrowser.open("https://www.youtube.com/watch?v=" + live_video[0])
webbrowser.open("https://www.youtube.com/watch?v=" + live_video[1])
webbrowser.open("https://www.youtube.com/watch?v=" + live_video[2])
