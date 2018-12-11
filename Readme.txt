For WSL:
#download and initiate "Xming Server"
#edit bashrc
sudo vim ~/.bashrc
#paste the line below
export DISPLAY=:0


For display:
sudo vim /boot/config.txt
=========================

hdmi_cvt=1024 600 60 3 0 0 0
hdmi_group=2
hdmi_mode=87
display_rotate=1



Dependencies:
Using Python 2.7


Pillow
==========
sudo pip install pillow

GoogleImagesDownload
====================
sudo pip install googe_images_download

Geeqie (Image Viewer)
=====================
sudo apt-get install geeqie

Execution:

sudo python
from fullscreen import fullscreen
fullscreen('keyword')
