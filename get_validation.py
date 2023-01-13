import os
import random
import shutil
from progressbar import ProgressBar

if __name__ == '__main__':
    TRAINPATH = r'./train/'
    VALPATH = r'./val/'

    seen = set()

    numberTrain = len(os.listdir(TRAINPATH))
    valFiles = int(numberTrain * (35 / 100))

    prog = 0
    ProgressBar(prog, valFiles * 2, prefix = 'Progress: ', suffix = '', length = 50)

    for i in range(valFiles):
        random_file = random.choice(os.listdir(TRAINPATH))

        seen.add(random_file.replace(".jpg", ""))

        source_file = "%s/%s"%(TRAINPATH,random_file)
        dest_file = VALPATH
        
        try: shutil.copy (source_file, dest_file)
        except: continue

        prog += 1
        ProgressBar(prog, valFiles * 2, prefix = 'Progress: ', suffix = '', length = 50)
        

    for file in seen:
        filename = '../labels/train/' + file + '.txt'
        try: 
            shutil.copy (filename, '../labels/val/' + file + '.txt')
            prog += 1
            ProgressBar(prog, valFiles * 2, prefix = 'Progress: ', suffix = '', length = 50)
        except: continue