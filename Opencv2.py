import cv2

def main():
    # 카메라 초기화
    camera = cv2.VideoCapture(0)  # 기본 카메라 인덱스는 0
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    camera.set(3, 640)  # 가로 해상도
    camera.set(4, 480)  # 세로 해상도

    # Haar Cascade 파일 로드
    xml = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(xml)

    while True:
        ret, image = camera.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 얼굴 검출
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)  # 검출 매개변수 조정
        print("Faces detected: " + str(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 결과 화면 표시
        cv2.imshow('result', image)

        # 'q' 키로 종료
        if cv2.waitKey(1) == ord('q'):
            break

    # 리소스 정리
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
