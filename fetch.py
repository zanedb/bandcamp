import requests
import re

def getStreamUrl(html):
    return re.findall(r'\"mp3-128\"\w*:\w*\"(.*?)\"', html.text)[0]

url = input('Please enter a Bandcamp song link: ')
html = requests.get(url)
stream_url = getStreamUrl(html)
print(stream_url)
