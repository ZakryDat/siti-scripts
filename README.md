# siti-scripts
python scripts for calculating SI &amp; TI values from each frame of a given mp4 input.
multiple inputs can be added to same csv file output (episode, frame, si, ti)

SI and TI local maxima determined in rolling 16 sec window.
Local maxima compared to find matches within +-1 SI/TI.
result output to csv files containing SI or TI matches (frame, episode, SI, TI, matches).
matches given as a timestamp of the matching local maximum.

matches must be checked manually for coherence.
clip_picker script can be used to extract 10 second clips from given episodes
and write siti details of the clips to a csv file.
