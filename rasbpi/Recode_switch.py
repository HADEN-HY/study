#recode

from gpiozero import Button
import time
import pyaudio
import wave
import datetime

#set Button
swPin = Button(14)

olSw = 0
newSw = 0

#set file
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 60


def saveVoice():
    p = pyaudio.PyAudio()

    # open stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start recording")

    frames = []

    # set file 
    now = datetime.datetime.now()
    fileName = now.strftime('%Y-%m-%d_%H-%M-%S')  

    # 60sec
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow=False)  #overflow prevention
        frames.append(data)

    print("Recording is finished.")

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    #file save as wav
    wf = wave.open(fileName +'.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"File saved as {fileName}.wav")

try:
    while True:
        newSw = swPin.is_pressed
        if newSw != olSw:
            olSw = newSw

            if newSw == 1:
                saveVoice()

            time.sleep(0.2)

except KeyboardInterrupt:
    pass

