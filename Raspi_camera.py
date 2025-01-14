#before the start install opencv 'pip3 install opencv-python'
import cv2

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)

    while(camera.isOpend()):
        _,image = camera.read()
        cv2.imshow('camera test', image)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__=='__main__':
    main()