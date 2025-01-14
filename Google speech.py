#using USB Mic, led red,green,blue
#install : 'sudo apt install python3-pyaudio -y' , 'pip3 install speechrecognition == 3.8.0' , 'sudo apt-get install flac'
#go to goole cloud and make project, making a key

import speech_recognition as sr

#main
try:
    while True:
        #recode
        r = sr.Recognizer()

        with sr. Microphone() as source:
            print ("Say something!")
            audio = r.listen(source)
        #using goole Recognition
        try:
            print("You said: " + r.recognize_google(audio, language = 'ko-KR'))
        except sr.UnknownValueError:
            print("Google Speech could not understand")
        except sr.RequestError as e:
            print("Could not request results from google service; {0}".format(e))
        
    
except KeyboardInterrupt:
    pass
    

