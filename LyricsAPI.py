# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

def get_lyrics(singer, song):
    singer = singer.lower()
    singer = "".join(singer.split())
    song = song.lower()
    song = "".join(song.split())
    url = 'http://azlyrics.com/lyrics/'+singer+'/'+song+'.html'
    data = urllib.request.urlopen(url)
    data2 = data.read()
    raw = BeautifulSoup(data2,'html.parser')
    lyr = raw.find_all("div", attrs={"class": None, "id": None})
    lyrics = [i.getText() for i in lyr]
    f = open(singer+'_'+song+'.txt','w')
    f.write("\n".join(lyrics).strip())
    f.close()

def details_input():
    singer = input("enter singer name :")
    song = input("enter song name :")
    get_lyrics(singer,song)

if __name__ == "__main__":
    details_input()