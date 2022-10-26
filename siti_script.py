import subprocess
import json
import csv

# input: mp4 content to process
nameEpisodeTS = 'example.ts' # file to convert
nameEpisode = 'example.mp4' # filetype to convert to
# if necessary convert episode to mp4 eg.:
subprocess.run(f'./ffmpeg -i {nameEpisodeTS} -map 0:1 -c:v copy -map 0:5 -c:a copy {nameEpisode}')
# output: csv file containing SI and TI values for all frames of input

# csv file for storing siti values
siti_values_file = 'example.csv' # file for siti values

# run through entire episode and grab SITI values for each frame
x = subprocess.run(f'siti -f {nameEpisode}',stdout=subprocess.PIPE)
siti_file = json.loads(x.stdout)
num_frames = len(siti_file['si'])

with open(siti_values_file,'a',newline='') as csvfile:
   writer = csv.writer(csvfile)
   #writer.writerow(['Episode','Frame','SI','TI'])
   for i in range(num_frames):
    writer.writerow([nameEpisode, i, siti_file['si'][i], siti_file['ti'][i]])
