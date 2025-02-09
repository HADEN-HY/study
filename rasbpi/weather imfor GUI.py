import requests
import re
import tkinter
import tkinter.font

def tickMin():
    try:
        # 기상청 날씨 정보 가져오기
        url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2635053000'
        response = requests.get(url, timeout=10)  # 10초 타임아웃 설정
        response.raise_for_status()  # HTTP 상태 코드 확인
        
        # 온도와 습도 추출
        temp = re.findall(r'<temp>(.+)</temp>', response.text)
        humi = re.findall(r'<reh>(.+)</reh>', response.text)
        
        # 온도와 습도를 화면에 표시
        if temp and humi:
            display = f"{temp[0]}°C {humi[0]}%"
        else:
            display = "정보를 가져올 수 없습니다."

    except requests.exceptions.RequestException as e:
        # 네트워크 에러 처리
        display = "날씨 정보를 가져오는 데 실패했습니다."

    # 레이블 업데이트
    label.config(text=display)
    window.after(60000, tickMin)  # 1분마다 업데이트

# 메인 윈도우 생성
window = tkinter.Tk()
window.title("TEMP HUMI DISPLAY")
window.geometry("400x100")  # 소문자 x 사용
window.resizable(False, False)

# 폰트와 레이블 설정
font = tkinter.font.Font(size=30)
label = tkinter.Label(window, text="Loading...", font=font)
label.pack(pady=20)  # 레이블 배치

# 첫 업데이트 호출
tickMin()

# GUI 실행
window.mainloop()
