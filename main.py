from operator import contains
from pathlib import Path

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

testsongs = Path("test-songs")

def list_to_string(list):
    '''Takes a list input and returns the 0-th index'''
    string = list[0]
    return string

def save_current_song(song, tag, tag_value):
    '''takes the tag_value passed and saves the audio file'''
    song[tag] = tag_value
    song.save()
    print("song has been saved")

def string_linter(tag, tag_value):
    '''removes anything between () if it contains anything from badwords list, 
    and returns the string no matter if it was changed or not'''

    bad_words = ("remastered", "Remastered", "REMASTERED",
    "anniversary", "Anniversary", "ANNIVERSARY",
    "edition", "Edition", "EDITION"
    )
    index = 0
    for bad_words in tag_value:
        #sees if string has bad word in it
        if bad_words[index] in tag_value: #tag needs to be edited
            #this assumes the data is structured like this
            #title (remastered).mp3
            #TODO find out why the if statement is true 100%
            tmplist = list_to_string(current_song[tag]).split(' (')
            tag_value = tmplist[0]
            
            return tag_value #returns edited value

        else: #tag is fine and does not need to be edited
            return list_to_string(current_song[tag]) #non edited
    index += 1

filename = "02 Candle In The Wind (Remastered 2014)  Elton John"
filetype = ".mp3"
complete_filename = filename + filetype
current_song = MP3(testsongs/complete_filename, ID3=EasyID3)
#print(song.keys())
title = string_linter("title", list_to_string(current_song["title"]))
save_current_song(current_song, "title", title)


album = string_linter("album", list_to_string(current_song["album"]))
save_current_song(current_song, "album", album)




