import os
from pathlib import Path

from mutagen import MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC



def list_to_string(list):
    '''Takes a list input and returns the 0-th index'''
    return list[0]

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
    sum = 0

    for bad_word in bad_words:
        #sees if string has bad word in it
        if bad_word in tag_value: #tag needs to be edited
            #this assumes the data is structured like this
            #title (remastered).mp3 
            sum += 1
            return_list = ((list_to_string(current_song[tag])).split(' (')[0], sum)
            return return_list

    #else
    return_list = (tag_value, sum)
    return return_list


def main():
    '''takes any .mp3 in working-dir and lints the junk out of it's title and album tags and saves the song'''
    #reads from the directory
    dir = Path("working-dir")

    #if directory doesnt exist
    if not os.path.exists(dir):
        #create directory and exit the program
        os.makedirs(dir)
        print("working directory created!\nExiting program early\n")
        exit() #since if the folder didnt exist its a waste of time to continue


    #load all files in working dir into program
    list_of_songs = []
    for root,d_names,f_names in os.walk(dir):
            for f in f_names:
                list_of_songs.append(os.path.join(root, f))


    #statistical varaibles
    index = 0
    amount_of_errors = 0
    tags_modified = 0

    for current_song in list_of_songs:
        index += 1 #pre increment
        try:
            #figure out if file is a .flac or .mp3        
            if ".mp3" in current_song:
                current_song = MP3(list_of_songs[index-1], ID3=EasyID3)
                valid_song = True

            elif ".flac" in current_song:
                current_song = FLAC(list_of_songs[index-1])
                valid_song = True

            else:
                print(current_song,"is not a .mp3 or .flac file")
        except MutagenError:
            amount_of_errors += 1
            continue
    
        #lint and save title and album name
        if valid_song:
            #fix title name
            title_list = string_linter(current_song, "title", list_to_string(current_song["title"]))
            save_current_song(current_song, "title", title_list[0])
            tags_modified += title_list[1]

            #fix album name
            album_list = string_linter(current_song, "album", list_to_string(current_song["album"]))
            save_current_song(current_song, "album", album_list[0])
            tags_modified += title_list[1]

            valid_song = False


    
    #results
    print(index, "files proccessed")
    print(amount_of_errors, "errors occurred")
    print(tags_modified, "tags modified\n")

    if not amount_of_errors == 0:
        print("errors can be caused by non music files in the directory")


main()
