#tracking eye
#install opencv and using usb cam
import cv2

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4.480)

 # Haar Cascade 파일 로드
    face_xml = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    eye_xml = cv2.data.haarcascades + 'haarcascade_eye.xml'
    face_cascade = cv2.CascadeClassifier(face_xml)
    eyes_cascade = cv2.CascadeClassifier(eye_xml)

    while True:
        ret, image = camera.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 얼굴 검출
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        print("Faces detected: " + str(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            face_gray = gray[y:y + h, x:x + w]
            face_color = image[y:y + h, x:x + w]

            # 눈 검출
            eyes = eyes_cascade.detectMultiScale(
                face_gray,
                scaleFactor=1.1,
                minNeighbors=5
            )
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # 결과 이미지 표시
        cv2.imshow('result', image)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) == ord('q'):
            break

    # 리소스 정리
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
