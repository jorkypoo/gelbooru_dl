import requests, bs4, os, sys, io
from PIL import Image
from pathlib import Path

def get_nextpage():
  current_page = f'https://gelbooru.com/index.php?page=post&s=list&tags={tags_f}-video&pid={page_no}'
  req = requests.get(current_page)
  soup = bs4.BeautifulSoup(req.text, 'html.parser')
  p = soup.find_all(attrs={'class':'thumbnail-preview'})
  return soup, p


# ========= INITS ==========

# sys.argv[1] will be the file name option, rest will be gelbooru tags
n = len(sys.argv)
to_input_name = 0 # quick check to determine if user will need to manually decide each filename in any way shape or form
tags = [] # tags inputted by user
tags_f = '' # for the URL
file_name = 'image'

for i in range(2, n):
  tags.append(sys.argv[i])

# selecting file name based on users naming option choice
if sys.argv[1] == 'auto' or sys.argv[1] == 'a':
  if len(sys.argv) <= 2:
    print("not enough tags provided")
    sys.exit()
  file_name = f'{tags[0]}_{tags[1]}'
elif sys.argv[1] == 'predef' or sys.argv[1] == 'p':
  file_name = input()
elif sys.argv[1] == 'manual' or sys.argv[1] == 'm':
  file_name = ''
  to_input_name = 1
elif sys.argv[1] == 'char' or sys.argv[1] == 'c':
  file_name = input()
  file_name += '_'
  to_input_name = 1
elif sys.argv[1] == 'random' or sys.argv[1] == 'r':
  print("not implemented yet")
else:
  print("no valid naming option passed, quitting program sort of gracefully... kidding, not really")
  print("read the readme u retard")
  print("error messages be like:")
  sys.exit()
f_tempname = file_name



# statistics/counters
images_parsed = 0
images_saved = 0

for tag in tags:
  tags_f += tag + '+'

# create the temp dl folder
try:
  os.mkdir(f"{Path('.', 'dl_temp')}")
  print("created temp folder for downloads")
except:
  print("temp folder already exists")

# TODO make this os independant UGHHHH
folder_name = Path('.', 'dl_temp')

page_no = 0
choice = ''

soup, posts = get_nextpage() # gets first page
print('\n')

# ========== MAIN LOOP ==========
while len(posts) != 0:
  for entry in posts: # for each thumbnail entry on page
    for link in entry.find_all('a'): # get the link of the current thumbnail entry & open
      link = link.get('href')
      req = requests.get(link)
      soup = bs4.BeautifulSoup(req.text, 'html.parser')

      side_options = soup.find_all('section', {'class':'aside'}) # find the original image
      for side in side_options:
        for option in side.find_all('li'):
          if option.get_text() == 'Original image':
            link = option.find('a')
            link = link.get('href')

            image = requests.get(link).content # image file found & ready to show using PIL, right?
            print("DEBUG: image loaded from gelbooru...")

            image_inmem = io.BytesIO(image)
            im = Image.open(image_inmem)
            im.show()

            choice = input("Do you wish to save this photo? [1] yes [0] no ")
            if choice == '1' or choice == 'yes' or choice == 'y' or choice == ' ':
              if to_input_name == 1:
                f_tempname = file_name # resets for user input & stuff
                f = input(f"{file_name}")
                f_tempname += f
                with open(f"{folder_name}/{f_tempname}.jpg", "wb+") as file:
                  file.write(image)
                  file.close()
              else:
                with open(f"{folder_name}/{file_name}{images_saved}.jpg", "wb+") as file:
                  file.write(image)
                  file.close()
              print("image saved to disk")
              images_saved += 1
            else:
              print("image not saved")
            print("next image...")
            # close image window here
            images_parsed += 1
            # this doesnt close the tab btw, maybe works on windows idk
            im.close()
            image_inmem.close()

  page_no += 42
  soup, posts = get_nextpage()

# program has found all images
print(f"images parsed: {images_parsed} images saved: {images_saved}")
print("Execution finished.")
