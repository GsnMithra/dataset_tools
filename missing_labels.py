import os

path_to_images = '/Volumes/Expansion/Deep Learning/dataset_tools/data_set/images/train'
path_to_labels = '/Volumes/Expansion/Deep Learning/dataset_tools/data_set/labels/train'

deleted = 0

for file in os.listdir (path_to_labels):
    src = f'{path_to_labels}/{file}'
    try:
        if os.path.getsize (src) == 0:
            print (f'deleting {file}')
            file = file[0:-4]
            image_src = f'{path_to_images}/{file}.jpg'

            deleted += 1

            os.remove (src)
            os.remove (image_src)
    except: pass

print (f'number of files deleted: {deleted}')