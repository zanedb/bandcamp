import requests
import re

def getStreamUrl(html):
  return re.findall(r'\"mp3-128\"\w*:\w*\"(.*?)\"', html.text)[0]

def getTitle(html):
  return re.findall(r'\"title\"\w*:\w*\"(.*?)\"', html.text)[0]

def downloadFile(stream_url):
  mp3_file = requests.get(stream_url)
  if mp3_file.status_code == 200:
    with open(file_name, 'wb') as f:
      f.write(mp3_file.content)
      print('Done!')

url = input('Please enter a Bandcamp song link: ')
html = requests.get(url)
stream_url = getStreamUrl(html)
title = getTitle(html)
print('URL: '+stream_url)
print('Title: '+title)
print('Downloading as "'+title+'.mp3"..')
file_name = title+'.mp3'
downloadFile(stream_url)
