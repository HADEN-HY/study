#install espeak before start
import os

def speak(option, msg):
    os.system("espeak {} '{}'".format(option, msg))
    print('espeak', option, msg)

option = '-s 180 -p 50 -a 200 -v ko+f5'
msg = '안녕하세요 반갑습니다.'
speak(option, msg)
