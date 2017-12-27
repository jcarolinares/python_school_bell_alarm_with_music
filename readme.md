# Python school bell alarm
A bell alarm program designed to play a song some time every day inside a computer or a raspberry pi in a school

Original idea from Felo Couto

Hope you'll find useful!

<a href="https://youtu.be/AnBly9F83Wk" target="_blank">
<img src="http://img.youtube.com/AnBly9F83Wk/5.jpg"
alt="Preview video" width="240" height="180" border="10" /></a>

Made by Julián Caro Linares

* email: jcarolinares@gmail.com
* twitter: @jcarolinares

# How to use
Python version and libraries:
* Python 3
* Pygame

First of all, if you don't have Python 3.X on your computer, you'll need to install it.

<a href="https://www.python.org/downloads/">Official Python 3 page</a>

You'll also need the library Pygame:

$ apt-get install python-pygame

Or

$ pip3 install pygame

You have to put a sound file in the same folder of the program, by default the file has to be named as "music.wav". I highly recommend to use a wav file but I think you can also uses anothers music formats without problems.

Now executes the python program "school_bell.py" using python3:

* Put the hour (example: 14)

* Put the minute (example: 10)

* Put the play time of the song in seconds (example: 30)

* By default the fadeout effect will be two seconds, but you can change this fadeout time inside the code (Alarm.self.fadeout)

The program will play the song and waits until the next alarm (next day, same hour). It's a True loop. To stop the program just put Ctrl+Z inside the terminal



=============

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">School bell alarm</span> por <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Julián Caro Linares</span> licensed by <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br /><br />
