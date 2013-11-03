#!/bin/bash
# write an French text string as an audio file using Google Translate
# usage: en2audio.sh <text>

wget -q -U Mozilla -O "$*.mp3" "http://translate.google.com/translate_tts?ie=UTF-8&tl=fr&q=$*"
mpg123 -w $*.wav $*.mp3
mv $*.wav output.wav
sox output.wav -r 44100 -c 2 $*.wav
