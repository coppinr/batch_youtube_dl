The python script "batch_youtube_dl" reads in a text file, specified as a command-line argument, which contains youtube link addresses, one per line.

The script then makes a subprocess call to the youtub_dl script, in the same directory, to download those videos at highest available quality.

The "batch_youtube_audio_dl" also converts the results to an MP3 file, and saves both the video and audio files.

Rquirements:
Python... bash shell.
The youtube_dl script used is from this repo: http://rg3.github.com/youtube-dl/
