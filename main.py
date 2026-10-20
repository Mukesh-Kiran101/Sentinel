import cv2
import time

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


face_model = "face_detector.tflite"

Base_Option = python.BaseOptions(model_asset_path = face_model)

options = vision.FaceDetectorOptions(base_options = Base_Option
                                     , running_mode=vision.RunningMode.IMAGE
                                     ,min_detection_confidence= 0.5)

detector = vision.FaceDetector.create_from_options(options)

video = cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Project SENTINEL", cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    "Project SENTINEL",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)


#Timer initialistion
outside_since = None

print("--------------- PROJECT : SENTINEL ---------------")
while True:
    ret , frame = video.read()

    if not ret :
        print("Failed to capture frame")
        break

    #bgr to rgb cause
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    #creates mp's own image aside from cv2 image frame
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    #Safe Zone
    height, width, colour = frame.shape
    left = int(width * (28 / 100))
    right = int(width * (72 / 100))
    top = int(height * (23 / 100))
    down = int(height * (77 / 100))


    #msg to display on frame
    alert_text = ""

    #returns all detected faces
    detect_result = detector.detect(mp_image)
    if detect_result.detections:
        face = detect_result.detections[0]
        #face coords detection
        box = face.bounding_box

        #Our face box coords
        ord_x = box.origin_x
        ord_y = box.origin_y
        face_width, face_height = box.width , box.height
        face_right = ord_x + face_width
        face_down = ord_y + face_height

        face_center_x = ord_x + (face_width/2)
        face_center_y = ord_y + (face_height/2)

        face_inside = (left <= face_center_x <= right and top <= face_center_y <= down)

        #grace period
        if not face_inside:
            if outside_since is None:
                outside_since = time.time()
            elif time.time() - outside_since >=1 :
                box_color = (0, 0, 225)
                alert_text = "!!! ALERT ALERT ALERT : Privacy Invaded !!!"

        else:
            outside_since = None
            box_color = (0, 225, 0)


    cv2.rectangle(frame , (ord_x , ord_y) , (face_right , face_down) , box_color , 2)

    if alert_text:
        cv2.putText(frame , alert_text , (350, 650 ) , cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Project : SENTINEL" , frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()

