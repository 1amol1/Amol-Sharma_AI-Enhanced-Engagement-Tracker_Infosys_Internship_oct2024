import cv2
import numpy as np

cap1 = cv2.VideoCapture('video1.avi')
cap2 = cv2.VideoCapture('video2.avi')

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    h_concat = np.hstack((frame1, frame2))

    cv2.imshow('Concatenated Video', h_concat)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()


# for camera if video not Available
# import cv2
# import numpy as np
#
# # Open the first camera (webcam)
# cap1 = cv2.VideoCapture(0)  # Use 0 for the default camera
# cap2 = cv2.VideoCapture(1)  # Use 1 for the second camera (if available)
#
# # Check if both cameras are opened successfully
# if not cap1.isOpened() or not cap2.isOpened():
#     print("Error: Could not open camera.")
#     exit()
#
# while True:
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#
#     # Check if frames are captured successfully
#     if not ret1 or not ret2:
#         break
#
#     # Resize frames to a common size
#     frame1 = cv2.resize(frame1, (640, 360))
#     frame2 = cv2.resize(frame2, (640, 360))
#
#     # Concatenate frames horizontally
#     h_concat = np.hstack((frame1, frame2))
#
#     # Display the concatenated video
#     cv2.imshow('Concatenated Video', h_concat)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
# # Release the camera resources and close windows
# cap1.release()
# cap2.release()
# cv2.destroyAllWindows()