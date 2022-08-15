#!/bin/bash

res="720"

for a in ./*.mp4; do
  < /dev/null ffmpeg -i "$a" -vf scale=-1:720 "${a[@]:0:-4}-720p.mp4"
done

