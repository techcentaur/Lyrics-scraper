from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse

class Scraper():
    def __init__(self, song, singer):
        song = song.lower()
        self.song = "".join(song.split())
        
        singer = singer.lower()
        self.singer = "".join(singer.split())

    def get_lyrics(self):
        print("\n[*] Scraping off lyrics...")
        url = 'https://www.azlyrics.com/lyrics/' + self.singer+'/' + self.song+'.html'
        
        raw = urllib.request.urlopen(url)
        data = raw.read()
        
        soup = BeautifulSoup(data, 'html.parser')
        l = soup.find_all("div", attrs={"class": None, "id": None})
        
        lyrics = [i.getText() for i in l]
        return lyrics

    def write_infile(self, lyrics):
        file = open(self.song + ".txt", 'w')
        
        file.write(lyrics[0])
        file.close()


if __name__ == "__main__":
    song = input("[?] Enter song: ")
    singer = input("[?] Enter singer: ")
    
    s = Scraper(song, singer)
    lyrics = s.get_lyrics()
    s.write_infile(lyrics)

    print("\n[*] Lyrics is stored in file with name " + s.song + ".txt")

#This code is contributed by techcentaur