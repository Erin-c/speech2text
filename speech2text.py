import subprocess
subprocess.Popen(['jackd', '-d', 'alsa'])

import multiprocessing

from fullscreen import fullscreen

from threading import Thread
try:
    from queue import Queue  
except ImportError:
    from Queue import Queue

import speech_recognition as sr

r = sr.Recognizer()
audio_queue = Queue()

sample_rate = 8000
chunk_size = 1024 


def recognize_worker():
    # this runs in a background thread
    pic_thread = None
    while True:
        audio = audio_queue.get()
        if audio is None: break  
        try:
            # for testing purposes, we're just using the default API key
            #print(r.recognize_google(audio))
            #p = multiprocessing.Process(target=fullscreen,args=(r.recognize_google(audio),))
            #p.start()
            #if pic_thread is not None:
            #    pic_thread.terminate()
            
            pic_thread = fullscreen(r.recognize_google(audio),pic_thread)

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        audio_queue.task_done()  # mark the audio processing job as completed in the queue


# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with sr.Microphone(sample_rate = sample_rate,chunk_size = chunk_size) as source:
    try:
        while True:  
            audio_queue.put_nowait(r.listen(source))
    except KeyboardInterrupt:  
        pass

# audio_queue.join()  # block until all current audio processing jobs are done
audio_queue.put(None)  # tell the recognize_thread to stop
# recognize_thread.join()  # wait for the recognize_thread to actually stop
