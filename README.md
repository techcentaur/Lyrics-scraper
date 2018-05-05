# Lyrics scraper
Scrapes the lyrics of songs.

## Usage

#### Terminal Usage

```console
gavy42@jarvis:~/Lyrics-scraper$ python3 lyrics.py 
[?] Enter song: Red 
[?] Enter singer: Taylor Swift

[*] Scraping off lyrics...

[*] Lyrics is stored in file with name red.txt
```

#### Methods

After instatiating the object of the class Scraper, with arguments as song name and singer name in order, these methods can be banged - 
- `get_lyrics()`: Returns lyrics by scraping the song on web.

- `write_infile(lyrics)`: Writes the lyrics in a file and store it in same directory.

