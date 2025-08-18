READ ME!!!
dependencies: requests, bs4 & PIL - install with pip

it's ok to put this program right in ur pictures folder, it creates it's own folder to save images to; separate from ur own, preventing overwrites
HOWEVER, be warned this program can overwrite files inside the dl_temp directory. don't come whinging to me if that happens, ur meant to move them out after

==================== USAGE ====================

python3 path/to/gelbooru_dl.py [naming option] [tags]

==================== TIPS =====================

when asked to save a file, input nothing for no

ermmmm.... uhmmm......

it takes me a while to dl some images so be patient

ctrl + c to quit out of the program at any time (hope thats the same on windows lmao scrub)

==================== NAMING OPTIONS ====================

pass only 1 of these 5 choices. applies to all files saved to disk in current session



auto or a: assigns first 2 tags provided to be the file name
           auto exits if only 1 tag was provided
for example: 

> python3 gelbooru_dl.py a armpits bikini -ai tanned

> armpits_bikini1.jpg saved to disk


good for one liners such as rumia bikini armpit or whatever
not useful for characters, u may get shit like hakurei_reimu_(pc-98)_heart-shaped_pupils24.jpg


predef or p: uses one file name inputted by the user
             input the desired filename in the terminal after opening the script
for example:

> python3 gelbooru_dl.py p hakurei_reimu_(pc-98) heart-shaped_pupils

> reimu_purple

> reimu_purple1.jpg saved to disk


no error handling around if ur operating system can handle the file #notmyproblem


manual or m: user chooses file name for each individual file, if they choose to save it
             NB: does not add a number to the end of filename, has potential to overwrite existing files! TODO: fix this. duh, nigga
             again, no error handling regarding the name u input, be nice


char or c: combination of predef and manual, user inputs a base file name for all files & an individual filename appended to base for each file
           input the base filename in the terminal after opening the script
           NB: does not add a number at end of filename, can overwrite existing files. see manual
for example:

> python3 gelbooru_dl.py c sonozaki_mion yuri

> mion

> sweatyarmpit

> mion_sweatyarmpit.jpg saved to disk

> _shion_kissing

> mion_shion_kissing.jpg saved to disk


for example:

> reimu_yukarin

> gaperm

> reimu_yukarin_gaperm.jpg saved to disk


best used when ur looking for a specific character, i use this one the most


random or r: for u who don't care about file names (dude) uses the url of the current picture
for example:

> python3 gelbooru_dl.py r hakurei_reimu yuri

> 24wiuEfFEfjdq9BYfqe.jpg saved to disk


not implemented yet


===================== TAGS ====================

must be separated by spaces
& the tags must be valid for gelbooru - for example: hakurei_reimu_(pc-98)
or else you'll get an error or smth, idk
