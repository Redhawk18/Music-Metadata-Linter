from pathlib import Path

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

testsongs = Path("test-songs")

def listToString(list):
    '''Takes a list input and returns the proper string'''
    string = list[0]
    return string

#testsongs = Path("test-song")
song = MP3(testsongs/"01 Don't Let Him Go  REO Speedwagon.mp3", ID3=EasyID3)
print(song.keys())
print(song["title"])
title=song["title"]
title=title[0]
print(title)
print(song["artist"])
album = listToString(song["album"])
print(album)
print(song["date"]) 
print(song["tracknumber"])
print(song["discnumber"]) 
print(song["genre"])
