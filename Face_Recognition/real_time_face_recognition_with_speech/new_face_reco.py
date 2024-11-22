import cv2 as cv
import face_recognition
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load the known image of Amol Sharma
known_image = face_recognition.load_image_file("img.jpeg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

# Confidence threshold
confidence_threshold = 0.6

# Flags to manage speech
already_spoken_recognized = False
already_spoken_not_recognized = False

# Start processing frames
while True:
    ret, frame = cam.read()
    if not ret:
        print("Can't receive the frame")
        break

    # Face detection in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    recognized = False

    for face_encoding, face_location in zip(face_encodings, face_locations):
        distance = face_recognition.face_distance([known_faces], face_encoding)[0]
        if distance < confidence_threshold:
            recognized = True
            # Draw rectangle and label
            top, right, bottom, left = face_location
            cv.rectangle(frame, (left, top), (right, bottom), color=(0, 255, 0), thickness=2)
            cv.putText(frame, 'Amol Sharma', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                       (255, 0, 0), 2, cv.LINE_AA)
            if not already_spoken_recognized:
                engine.say("Amol Sharma")
                engine.runAndWait()
                already_spoken_recognized = True
                already_spoken_not_recognized = False
        else:
            # Not recognized, draw rectangle and label
            top, right, bottom, left = face_location
            cv.rectangle(frame, (left, top), (right, bottom), color=(0, 0, 255), thickness=2)
            cv.putText(frame, 'Not Amol Sharma', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                       (0, 0, 255), 2, cv.LINE_AA)

    if not recognized:
        if not already_spoken_not_recognized:
            engine.say("Match not found")
            engine.runAndWait()
            already_spoken_not_recognized = True
            already_spoken_recognized = False

    # Display the resulting frame
    cv.imshow('Video Stream', frame)

    # End the streaming
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cam.release()
cv.destroyAllWindows()
