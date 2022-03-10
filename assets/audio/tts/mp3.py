from os import path
from pydub import AudioSegment

import os

path = "./audio/"
file_list = os.listdir(path)

print ("file_list: {}".format(file_list))
# files                                  
# 
for i in file_list:    
    if '.mp3'in i :                                   
        src = path +"%s" %i
        dst = path +"%s.wav" %i[0:-4]

        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")