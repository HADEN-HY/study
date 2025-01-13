#using usb mike and checking virtual environment

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16 #16bit audio data