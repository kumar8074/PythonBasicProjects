import sys
import os
from PIL import Image


#grab the pokedex and a new folder name as arguments

image_folder=sys.argv[1]
output_folder=sys.argv[2]

#print(image_folder,output_folder)


#check if the new folder exists or not if not then create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)



#loop through the pokedex folder and convert images to png and save them to new folder

for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    #print(clean_name)
    img.save(f'{output_folder}{clean_name}.png','png')