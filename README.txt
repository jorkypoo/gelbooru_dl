dependencies: requests, bs4 & PIL - install with pip

this program searches danbooru with provided tags and saves the file to disk, naming each to the provided naming convention
tags u provide must be the same you find in the gelbooru url

==================== USAGE ====================

python3 path/to/gelbooru_dl.py [naming option] [tags]

==================== NAMING OPTIONS ====================

auto or a: assigns first 2 tags provided to be the file name
           auto exits if only 1 tag was provided

for example: 

$ python3 gelbooru_dl.py a armpits bikini -ai tanned
$ armpits_bikini1.jpg saved to disk

good for one liners such as rumia bikini armpit or whatever
not useful for characters, u may get shit like hakurei_reimu_(pc-98)_heart-shaped_pupils24.jpg


predef or p: uses one file name inputted by the user
             input the desired filename in the terminal after opening the script

for example 

$ python3 gelbooru_dl.py p hakurei_reimu_(pc-98) heart-shaped_pupils
$ reimu_purple
$ reimu_purple1.jpg saved to disk
 
no error handling around if ur operating system can handle the file #notmyproblem


manual or m: user chooses file name for each individual file, if they choose to save it
             NB: does not add a number to the end of filename, has potential to overwrite existing files
             again, no error handling regarding the name u input, be nice


char or c: combination of predef and manual, user inputs a base file name for all files & an individual filename appended to base for each file
           input the base filename in the terminal after opening the script
           NB: does not add a number at end of filename, can overwrite existing files. see manual

for example 

$ python3 gelbooru_dl.py c sonozaki_mion yuri
$ mion
$ sweatyarmpit
$ mion_sweatyarmpit.jpg saved to disk
$ shion_kissing
$ mion_shion_kissing.jpg saved to disk

for example:
$ reimu_yukarin
$ gapsex
$ reimu_yukarin_gapsex.jpg saved to disk
best used when ur looking for a specific character, i use this one the most


random or r: for u who don't care about file names (dude) uses the url of the current picture
for example 

$ python3 gelbooru_dl.py r tanned bikini armpits -ai
$ 24wiuEfFEfjdq9BYfqe.jpg saved to disk

not implemented yet
