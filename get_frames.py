import cv2
import os
from progressbar import ProgressBar

get_name = input('enter your name: ')
number_images = int (input ('enter the number of images: '))
firstname = get_name.split()
name = firstname[0].lower()

try:
	os.mkdir(name)
except OSError:
	print("Failed to create folder.")
os.chdir(name)

vid = cv2.VideoCapture(0)

i = 0
print (f'Photo capture started...!')
ProgressBar (i, number_images, prefix = 'Progress: ', suffix = '', length = 100)
while(i < number_images):
	ret, frame = vid.read()
	cv2.imwrite(f'{name}{str(i)}.jpg', frame)
	i += 1
	ProgressBar (i, number_images, prefix = 'Progress: ', suffix = '', length = 100)
print (f'Data collected...!')

vid.release()
cv2.destroyAllWindows()