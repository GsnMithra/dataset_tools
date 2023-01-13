import os
import glob
import shutil

path_make = '/Volumes/Expansion/Deep Learning/dataset_tools/make_set'
path_data = '/Volumes/Expansion/Deep Learning/dataset_tools/data_set'

make_path = os.listdir (path_make)

for folder in make_path:
    for root, dirs, files in os.walk(f'{path_make}/{folder}'):
        for file in files:
            if file.endswith('.jpg'):
                shutil.copy(os.path.join(root, file), f'{path_data}/images/train')

for folder in make_path:
    for root, dirs, files in os.walk(f'{path_make}/{folder}/{folder}'):
        for file in files:
            if file.endswith('.txt'):
                shutil.copy(os.path.join(root, file), f'{path_data}/labels/train')