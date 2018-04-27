import requests
import re

def getStreamUrl(html):
    return re.findall(r'\"mp3-128\"\w*:\w*\"(.*?)\"', html.text)[0]

url = input('Please enter a Bandcamp song link: ')
html = requests.get(url)
stream_url = getStreamUrl(html)
print(stream_url)
mp3_file = requests.get(stream_url)
if mp3_file.status_code == 200:
  with open("file.mp3", 'wb') as f:
    f.write(mp3_file.content)
