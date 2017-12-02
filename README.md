# Lyrics API of www.azlyrics.com
API to extract lyrics from www.azlyrics.com through web-scraping, beautifulSoup and similar python modules


# Functions-Analysis
1. `get_lyrics(singer,song)`:
input 	- singer: name of the singer
	- song	: name of the song
output 	- returns a list of words, essentially the lyrics without any extra lexical notations or tags 

2. `write_infile(lyrics,singer,song)`:
input - takes the list of words in lyrics, singer and song
output - writes the list of words into a file named "singer_song.txt", syantactically correct.

3. `details_input()`: 
//this is just supportive method, invoking this begins the main function
it returns a list with singer at first index and song at the second index

# Usage

1. Run the file as
```
> python LyricsAPI.py
```
in python(version 3.x) environment
2. Ouput will be a text file in the same directory with name as
```
> singer_song.txt
```
