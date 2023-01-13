import cv2
import os
from PIL import Image
from progressbar import ProgressBar

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + r'haarcascade_frontalface_default.xml')

def toYOLO (x, y, w, h, img_height, img_width):
    x_center = x / img_width
    y_center = y / img_height

    box_width = w / img_width
    box_height = h / img_height

    x_center += box_width / 2
    y_center += box_height / 2

    return (x_center, y_center, box_width, box_height)

cid = int (input ('enter the class id: '))
dataset = os.listdir ('/Volumes/Expansion/Deep Learning/dataset_tools')
number_label = int (input ('enter the number of files to label per class: '))
seen = list ()

prog = 0
ProgressBar(prog, number_label * len (dataset), prefix = 'Progress: ', suffix = '', length = 100)
for folder_name in dataset:

    if not os.path.isdir (folder_name): continue

    print (f'labelling started for {folder_name}!')
    idx = 0

    try:
        os.mkdir (f'/Volumes/Expansion/Deep Learning/dataset_tools/{folder_name}/{folder_name}')
    except OSError:
        print('Failed to create folder.')

    fx = f'/Volumes/Expansion/Deep Learning/dataset_tools/{folder_name}/{folder_name}{idx}.jpg'
    fakeImage = Image.open(fx)
    fxHeight = fakeImage.height
    fxWidth = fakeImage.width

    entry_list = os.listdir (f'/Volumes/Expansion/Deep Learning/dataset_tools/{folder_name}')
    files = 1450
    os.chdir (f'/Volumes/Expansion/Deep Learning/dataset_tools/{folder_name}')

    for i in range (files):
        try: img = cv2.imread(f'/Volumes/Expansion/Deep Learning/dataset_tools/{folder_name}/{folder_name}{idx}.jpg')
        except:
            idx += 1
            continue

        try: gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except:
            idx += 1
            continue

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        filename = f'{folder_name}/{folder_name}{str(idx)}.txt'
        with open (filename, 'w') as f:
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                yoloC = toYOLO (x, y, w, h, fxHeight, fxWidth)
                prog += 1
                ProgressBar(prog, number_label * len (dataset), prefix = 'Progress: ', suffix = '', length = 100)
                # print (f'{x} {y} {w} {h}')
                f.write(f'{cid} {yoloC[0]} {yoloC[1]} {yoloC[2]} {yoloC[3]}')
            cv2.imshow('img', img)
            cv2.waitKey(1)

        idx += 1
    print (f'completed labelling for {folder_name}!')
    seen.append (folder_name)
    cid += 1

    os.chdir ('/Volumes/Expansion/Deep Learning/dataset_tools')

print (seen)
cv2.destroyAllWindows()
