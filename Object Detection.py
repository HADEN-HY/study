import cv2

# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

def id_class_name(class_id, classes):
    return classes.get(class_id, "Unknown")

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    try:
        model = cv2.dnn.readNetFromTensorflow(
            '/home/pi/myProjects/OpencvTest/OpencvDnn/models/frozen_inference_graph.pb',
            '/home/pi/myProjects/OpencvTest/OpencvDnn/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
        )

        while True:
            keyValue = cv2.waitKey(1)
            if keyValue == ord('q'):
                break

            ret, image = camera.read()
            if not ret:
                print("Failed to capture image")
                break

            image_height, image_width, _ = image.shape

            model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
            output = model.forward()

            for detection in output[0, 0, :, :]:
                confidence = detection[2]
                if confidence > 0.5:
                    class_id = int(detection[1])  # Ensure class_id is an integer
                    class_name = id_class_name(class_id, classNames)
                    print(f"{class_id} {confidence:.2f} {class_name}")

                    box_x = detection[3] * image_width
                    box_y = detection[4] * image_height
                    box_width = detection[5] * image_width
                    box_height = detection[6] * image_height

                    cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=2)
                    cv2.putText(image, class_name, (int(box_x), int(box_y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow('image', image)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()