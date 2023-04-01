import os
string = 'ffmpeg -i suzi.mov -ss 00:00:00 -to 00:00:04 -vcodec copy -acodec copy suzi.mp4'
os.system(string)
