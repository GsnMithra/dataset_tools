import os
import re
from PIL import Image
from time import sleep

path = '/Volumes/Expansion/Deep Learning/dataset_tools/flipper'
dataset = os.listdir (path)
seen = list ()

for folder in dataset:
    iter = 700

    each_path = f'/Volumes/Expansion/Deep Learning/dataset_tools/flipper/{folder}'
    try: each_file = os.listdir (each_path)
    except:
        continue

    for file in each_file:
        image_path = f'/Volumes/Expansion/Deep Learning/dataset_tools/flipper/{folder}/{file}'
        try: img = Image.open(image_path)
        except: 
            iter += 1
            continue

        new_image = img.transpose(Image.FLIP_LEFT_RIGHT)
        new_image_name = folder
        new_image_name = re.sub (r'\d', '', new_image_name)
        new_image_name += f'{iter}.jpg'

        print (new_image_name)

        new_image.save(f'{each_path}/{new_image_name}')
        iter += 1
    
    print (f'{folder}')
    seen.append (folder)

print (seen)