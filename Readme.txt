For WSL:
#download and initiate "Xming Server"
#edit bashrc
sudo vim ~/.bashrc
#paste the line below
export DISPLAY=:0

Dependencies:
Using Python 2.7

Tkinter
=======
sudo apt-get install python-tk

Pillow
==========
sudo pip install pillow

SpeechRecognition
=================
sudo pip install SpeechRecognition

PyAudio
=======
sudo apt-get install python-pyaudio

GoogleImagesDownload
====================
sudo pip install googe_images_download

Execution:

python
from fullscreen import fullscreen
fullscreen('keyword')