# using USB Mic, LED red, green, blue
import speech_recognition as sr
from gpiozero import LED

# LED 설정
green = LED(16)
blue = LED(20)
red = LED(21)

# LED 초기화 함수
def reset_leds():
    green.off()
    blue.off()
    red.off()

try:
    # LED 초기화
    reset_leds()
    
    while True:
        # 음성 녹음 시작
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say anything!")
            audio = r.listen(source)

        # Google Speech Recognition 사용
        try:
            text = r.recognize_google(audio, language='ko-KR')
            print("You said: " + text)
            
            # LED 제어
            if text == "빨간색":
                reset_leds()
                red.on()
            elif text == "파란색":
                reset_leds()
                blue.on()
            elif text == "녹색":
                reset_leds()
                green.on()
            elif text == "꺼":
                reset_leds()
            else:
                print("Unknown command.")
        
        except sr.UnknownValueError:
            print("Google Speech could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google service: {e}")
        
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
finally:
    reset_leds()
