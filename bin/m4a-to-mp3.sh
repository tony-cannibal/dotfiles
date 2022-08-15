#!/bin/bash

for a in ./*.m4a; do
  < /dev/null ffmpeg -i "$a" -qscale:a 0 "${a[@]/%m4a/mp3}"
done
