from google_images_download import google_images_download

import subprocess
import time
import sys

import os, shutil
if os.path.isdir("downloads"):
    shutil.rmtree('downloads')

def fullscreen(keyword):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":keyword, "limit":1, "format":"jpg", "size":"large", "aspect_ratio":"tall", "print_urls":True}
    image_path = response.download(arguments)
    try:
        print(image_path[keyword][0])
        sp = subprocess.Popen(["geeqie", "-f", image_path[keyword][0]])
        time.sleep(3)
        #Erin, you can change this to complete some other action before closing the window. You can also just keep the window open by removing the line below:
        sp.terminate()
    except IndexError:
        print "No images found for that keyword query."
