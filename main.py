from pathlib import Path

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

testsongs = Path("test-songs")

#testsongs = Path("test-song")
song = MP3(testsongs/"01 Don't Let Him Go  REO Speedwagon.mp3", ID3=EasyID3)
#song.keys()
print(song["title"])
print(song["artist"])
print(song["album"])
#print(song["year"])
print(song["tracknumber"])
#print(song["disc"])
print(song["genre"])
