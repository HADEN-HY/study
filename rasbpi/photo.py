#photo

from picamera2 import Picamera2
import time

picam = Picamera2
camera_config = picam.create_preview_configuration()
picam.configure(camera_config)
picam.start
time.sleep(2)
picam.capture_file("test.jpg")
