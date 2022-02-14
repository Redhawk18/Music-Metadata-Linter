import os
from pathlib import Path

from mutagen import MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


def list_to_string(list):
    '''Takes a list input and returns the 0-th index'''
    string = list[0]
    return string

def save_current_song(song, tag, tag_value):
    '''takes the tag_value passed and saves the audio file'''
    song[tag] = tag_value
    song.save()

def string_linter(current_song, tag, tag_value):
    '''removes anything between () if it contains anything from badwords list, 
    and returns the string no matter if it was changed or not'''

    bad_words = ("remastered", "Remastered", "REMASTERED",
    "Re-Mastered", "Re-mastered", "re-mastered",
    "anniversary", "Anniversary", "ANNIVERSARY",
    "edition", "Edition", "EDITION",
    "version", "Version", "VERSION"
    )

    for bad_word in bad_words:
        #sees if string has bad word in it
        if bad_word in tag_value: #tag needs to be edited
            #this assumes the data is structured like this
            #title (remastered).mp3
            tag_value = list_to_string(current_song[tag]).split(' (')[0]
            
            return tag_value

    #tag is fine and does not need to be edited
    return list_to_string(current_song[tag]) #non edited

def main():
    '''takes any .mp3 in working-dir and lints the junk out of it's title and album tags and saves the song'''
    dir = Path("working-dir")

    #load all files in working dir into program
    list_of_songs = []
    for root,d_names,f_names in os.walk(dir):
            for f in f_names:
                list_of_songs.append(os.path.join(root, f))
    

    index = 0
    amount_of_errors = 0
    for current_song in list_of_songs:
        index += 1 #pre increment

        try:
            #create song object
            current_song = MP3(list_of_songs[index-1], ID3=EasyID3)
        except MutagenError:
            amount_of_errors += 1
            continue

        #process metadata
        title = string_linter(current_song, "title", list_to_string(current_song["title"]))
        save_current_song(current_song, "title", title)

        album = string_linter(current_song, "album", list_to_string(current_song["album"]))
        save_current_song(current_song, "album", album)


    #results
    print(index, "files proccessed,", amount_of_errors, "errors occurred")
    if not amount_of_errors == 0:
        print("errors can be caused by non music files in the directory")

main()