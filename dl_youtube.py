
# importing packages
from pytube import YouTube 
import os
import sys

url = sys.argv[1]
  
# url input from user 
yt = YouTube(url) 
  
# extract only audio 
video = yt.streams.filter(only_audio=True).first() 
  
# check for destination to save file
destination = '.'
  
# download the file 
out_file = video.download(output_path=destination) 
  
# save the file 
base, ext = os.path.splitext(out_file)

base_with_underscores = base.lower().replace(' ', '_')

new_file = base_with_underscores + '.mp3'
os.rename(out_file, new_file)

# result of success 
print(base_with_underscores + " has been successfully downloaded.")
