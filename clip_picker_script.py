import subprocess
import json
import csv

# turn frames into time as hh:mm:ss (subtract 5s so max frame in middle)
# manually enter values for each set of matches & the TI/SI info
# I'm sure you could automate this, but given the need to manually check the clips anyway I haven't bothered
clip_times = ['00:09:14','00:22:50','00:42:05'] # example times
episode = 'example_episode.mp4'
TI = 60 # rough TI of given

i=1
with open('clip_picks_SI.csv','a',newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['Episode number','File name','Start time','Max SI','Max TI'])
    #iterate through clips of interest
    for clip_time in clip_times:
        filename = f'TI_{TI}_clip_{i}'
        subprocess.run(f'./ffmpeg -i {episode} -ss {clip_time} -t 00:00:10 -map 0:v -c:v copy -map 0:a -c:a copy -sn {filename}.mp4')
        x = subprocess.run(f'siti -f {filename}.mp4', stdout=subprocess.PIPE)
        siti_file = json.loads(x.stdout)


        writer.writerow([episode, filename, clip_time, siti_file['max_si'],siti_file['max_ti']])
        i +=1
