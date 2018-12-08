from threading import Thread
try:
    from queue import Queue  # Python 3 import
except ImportError:
    from Queue import Queue  # Python 2 import

import speech_recognition as sr

r = sr.Recognizer()
audio_queue = Queue()

def recognize_worker():
    # this runs in a background thread
    while True:
        audio = audio_queue.get()
        if audio is None: break  
        try:
            # for testing purposes, we're just using the default API key
            print(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        audio_queue.task_done()  # mark the audio processing job as completed in the queue


# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with sr.Microphone() as source:
    try:
        while True:  
            audio_queue.put(r.listen(source))
    except KeyboardInterrupt:  
        pass

audio_queue.join()  # block until all current audio processing jobs are done
audio_queue.put(None)  # tell the recognize_thread to stop
recognize_thread.join()  # wait for the recognize_thread to actually stop
