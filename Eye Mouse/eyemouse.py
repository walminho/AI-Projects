#Dependencies
"""
pip install opencv-python
pip install mediapipe
pip install pyautogui
"""

import cv2
import mediapipe as mp
import pyautogui
from Xlib import X, display
import time

# video capture
cap = cv2.VideoCapture(0)
"""cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)"""
# face model = face mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen dimention
d = display.Display()
screen = d.screen()
screen_width = screen.width_in_pixels
screen_height = screen.height_in_pixels
screen_w, screen_h = pyautogui.size()

# fps
start_time = time.time()
frame_count = 0

#main loop
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1) # flip the frame horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # increment the frame counter
    frame_count += 1
    # fps tax
    elapsed_time = time.time() - start_time
    if elapsed_time > 1:
        fps = frame_count/elapsed_time
        cv2.putText(frame, "FPS: {:.2f}".format(fps), (50, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    # searchin for a face and apply the face mesh model
    output = face_mesh.process(rgb_frame)
    # storage the dictionary of landmarks values
    landmark_points = output.multi_face_landmarks
    # frame dimension
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[468:473]):
            x = int(landmark.x * screen_width)
            y = int(landmark.y * screen_height)
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                #pyautogui.moveTo(screen_x, screen_y)
        right = [landmarks[475], landmarks[477]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)
        if (right[0].y - right[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.putText(frame, "Press q to quit", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break