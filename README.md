# Amol-Sharma_AI-Enhanced-Engagement-Tracker_Infosys_Internship_oct2024

# AI Enhanced Engagement Tracker 🕵️

## Overview :

The AI Enhanced Engagement Tracker is a smart system crafted to observe and evaluate user engagement in real-time. Utilizing artificial intelligence and data analytics, it delivers actionable insights aimed at improving productivity and interaction. This tool is perfect for educators, marketers, and workplace managers who want to refine their engagement strategies.<br />

## Project Structure 

- **Image Processing**
- **Video Processing**
- **Annotations**
- **Face Recognition**


#    Image Processing : 
**Image processing involves techniques for analyzing, enhancing, and transforming images to extract useful information or improve visual quality. This field encompasses tasks like noise reduction, image sharpening, segmentation, and object recognition. It's widely used in areas like medical imaging, computer vision, and multimedia applications.** <br />

## Libraries or Frame Works Used -
## opencv <br />
- **Version - 4.10.0.84**
- **NumPy - For array manipulation** <br />

## Developed Logics -<br />

#### A) `image_concatenation`
Image concatenation is a function that resizes two images to a designated pixel range and merges them both horizontally and vertically. The resulting images are then shown in separate windows.

- **Input:**

  ![Image 1](https://github.com/user-attachments/assets/a481e6f3-dea0-4f5b-b737-be84254d65b3)
  
  ![Image 2](https://github.com/user-attachments/assets/09ed3031-2733-4385-abc8-d117625327e0)

- **Output:**

  ![Concatenated Image](https://github.com/user-attachments/assets/a20f0dee-b19f-474f-b991-8d6b8cfb2667)

#### B) `image_contour`
This detects contours in a grayscale image using a binary threshold and `cv2.findContours()`. The contours are drawn onto the original image in green.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

  ![Contoured Image](https://github.com/user-attachments/assets/c9fb4919-5f6b-49f8-a4e4-c4817360076c)

#### C) `image_crop`
This function extracts a specific region of an image based on pixel range and displays the cropped section.

- **Input:**
 
  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Cropped Image](https://github.com/user-attachments/assets/ca28abac-d130-4b24-b143-fcebf4244e04)

#### D) `image_dilation & erosion`
This function applies morphological operations, dilation and erosion, to enhance and reduce features in an image, respectively.

- **Input:**
 
  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

  ![Dilated and Eroded Image](https://github.com/user-attachments/assets/193acd23-5a7a-4aa6-afff-d00664fc44b8)

#### E) `image_edge_detection`
This applies the Canny edge detection algorithm to detect edges in a grayscale image.

- **Input:**
 
  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Edge Detected Image](https://github.com/user-attachments/assets/2c118d60-4164-4cc8-b46a-ca00af050017)

#### F) `image_histogram_equalization`
This enhances the contrast of a grayscale image using histogram equalization.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Histogram Equalized Image](https://github.com/user-attachments/assets/905ccca9-4b7b-4a7a-8669-992f4d3a61bf)

#### G) `image_hsv`
This converts a color image from the BGR color space to HSV.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![HSV Image](https://github.com/user-attachments/assets/4df430d1-379c-45ba-b01c-34ce8460bd23)

#### H) `image_morphological_transformation`
This applies opening and closing morphological operations to a grayscale image to remove noise and fill gaps.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Morphologically Transformed Image]((https://github.com/user-attachments/assets/02762f79-7840-4e10-a892-b10717205747)

#### I) `image_resize`
This resizes an image to specified dimensions.

- **Input:**
 
  ![Image 1](https://github.com/user-attachments/assets/a481e6f3-dea0-4f5b-b737-be84254d65b3)

- **Output:**
 
  ![Resized Image](https://github.com/user-attachments/assets/ed586023-ebec-40aa-bf8c-43f439ec4d65)

#### J) `image_rgb2gray`
This converts a color image to grayscale.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Grayscale Image](https://github.com/user-attachments/assets/d8dc7186-8336-43cf-a60f-f74e34289be0)

#### K) `image_rotate`
This rotates an image by 90 degrees around its center.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

  ![Rotated Image](https://github.com/user-attachments/assets/57a660aa-cd02-4643-ad75-019d5ef58b2f)

#### L) `image_blur`
This applies a Gaussian blur to an image to reduce noise and detail.

- **Input:**

  ![Image 3](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**
 
  ![Blurred Image](https://github.com/user-attachments/assets/015ba166-811c-4622-9c15-a2c37434388b)

#### M) `image_noise_removal & closing_gaps`
This function removes noise and fills gaps using morphological operations.

#### N) `image_template`
This function performs template matching to locate a template image within a larger image.

  #  Video Processing
   
   **Video processing refers to the manipulation and analysis of video data to enhance quality, extract information, or facilitate specific functions such as motion detection and object tracking. Techniques used in video processing include frame-by-frame enhancement, compression, and filtering to ensure smooth playback or enable real-time processing. This technology is essential in areas such as surveillance, streaming, and augmented reality..** <br />

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84

### Developed Logics:

#### A) `Video_multivideo`
This function reads and displays images from a specified folder, printing the dimensions of each image.

#### B) `Video_fps`
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

#### C) `Video_save`
This function captures live video and saves it to a specified output file.

#### D) `Video_stack`
This function reads and resizes two video files, concatenating them horizontally.

#### E) `Video_stream`
This function captures live video from the webcam and displays it in real-time.

#  ANNOTATIONS
  **Annotations are supplementary labels or notes added to data, such as images or text, to provide context or emphasize specific details. In machine learning, annotations play a crucial role in supervised learning, where labeled data is used to train models for tasks like object detection or sentiment analysis. They are commonly employed in applications such as image tagging, document markup, and speech recognition to enhance model performance.** <br />

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### Developed Logics:

### A.data_segregate<br />

**Image and Label Segregation Script**
This script sorts images according to their associated label files. It separates matched image-label pairs into a matched directory while placing unmatched images in an unmatched directory. The script allows for custom file extensions and automatically creates the necessary directories if they are not already present.<br /> 

### B.label<br />

**Bounding Box Drawer for Images**
This script processes images along with their associated label files, drawing bounding boxes around detected objects using the provided label coordinates. The annotated images are then saved to a specified output directory. It supports label files in YOLO format and allows for customization of file extensions and output locations.



![gun](https://github.com/user-attachments/assets/ff66747f-dfaa-48f1-907b-47517be84778)


### C. label_manipulate<br />

**Class Number Updater for Label Files**
This script updates class IDs in label files, replacing a specified old class ID with a new class ID. It reads each label file, modifies the class ID as needed, and saves the changes back to the file, handling any malformed entries gracefully. This tool is useful for batch updating class labels in YOLO-format datasets.

### D. label_Image.txt<br />
 
![Screenshot 2024-11-15 142323](https://github.com/user-attachments/assets/79577d74-108f-4392-9b54-095746356cb3)

# Face_Recognition 
- Face recognition is a biometric technology that identifies or verifies individuals by examining facial features in images or videos. The process includes detecting a face, extracting distinctive features, and comparing them against a database for authentication or identification purposes. Widely utilized in security systems, smartphones, and social media platforms, face recognition has applications in access control and enhancing personalized experiences. <br />

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) `Face_recognition`
This system performs real-time face recognition to determine if the individual in live video frames matches a known image. If recognized, the person's name is displayed; if not, "Not Recognized" is shown instead.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 040819](https://github.com/user-attachments/assets/c7bbd0f2-335e-4ea2-894d-820cb76b7f36)


#### B) `Attendence_save`
Utilizing a live video stream, this system conducts real-time face recognition to identify individuals. When a person's face is recognized, their name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every five recognitions, the current log is saved to the Excel file, and both the recognition counter and DataFrame are reset.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 040819](https://github.com/user-attachments/assets/e2beea5c-7c96-4c35-9e2b-9b85b59e4fda)

![Screenshot 2024-11-17 042020](https://github.com/user-attachments/assets/e7a873ee-b608-4b9e-967c-a099d9e75f70)


#### C) `Test`
This system conducts real-time face recognition to identify individuals in a live video feed, logging each recognition event along with the date and time into an Excel file every 30 seconds. It monitors recognition intervals to prevent duplicate entries and displays the individual's name or "Not Recognized" based on the identification outcome.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 043046](https://github.com/user-attachments/assets/094a56ca-e1e8-40aa-bdf1-d225f5a1e1dc)

![Screenshot 2024-11-17 043150](https://github.com/user-attachments/assets/8432fd56-4d5c-4eb6-8fd5-2a156021d334)


#### D) `Tools`
This system conducts real-time face recognition using the live camera feed to identify individuals. Each time a face is recognized, it logs the name, date, and time in a data frame. When the recognition count reaches 5, it saves the records to an Excel file and then resets both the counter and the data frame. The system displays either "His/Her Name" or "Not His/Her Name" over the video feed, and pressing 'q' exits the program, ensuring any remaining records are saved.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 043715](https://github.com/user-attachments/assets/98adec35-0332-4ae6-abb0-a6874ce326be)

![Screenshot 2024-11-17 043809](https://github.com/user-attachments/assets/3b6cdf07-dd33-4b50-b6f8-b5a524d5d40c)


#### E) `excel_sc`
This system is designed for face recognition with time-based logging and is well-organized, incorporating the functionality to save screenshots and record attendance in an Excel file.

1. **Efficiency**: Resizing frames to 640x480 enhances processing speed. Further reduction in size is possible if necessary.
2. **File Saving**: Screenshots are stored in the folder named "amol_screenshots(5)", while the Excel file is updated every 30 seconds.
3. **Recognition Timings**: Attendance is logged every 30 seconds for the same individual and recorded every 5 minutes to prevent multiple entries within short intervals.
4. **Error Handling**:  A proper try-except block is implemented for error management.
5. **Termination**: The program exits when the 'q' key is pressed.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 044604](https://github.com/user-attachments/assets/6c8a47b4-8537-49ba-b0c8-3b220a135b75)

![Screenshot 2024-11-17 044733](https://github.com/user-attachments/assets/8bb80051-f1a3-460c-92ca-fc31bb7417c3)


#### F) `excel_sc_dt`
This system utilizes OpenCV and face_recognition to detect and recognize a specific individual from a webcam feed. When a face is recognized, a screenshot is captured, and attendance information (including name, date, time, and screenshot path) is recorded in an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures that attendance is logged only once every 5 minutes for the same person. The attendance data is maintained in a DataFrame and periodically exported to an Excel file.

Key Features:-->
->Real-time face detection and recognition.
->Captures and saves screenshots with timestamps.
->Records attendance in Excel every 30 seconds.
->Prevents multiple logs for the same individual within a 5-minute window.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 050648](https://github.com/user-attachments/assets/6e228f87-87d2-4379-b144-b6ee91cd16e4)

![Screenshot 2024-11-17 044733](https://github.com/user-attachments/assets/8bb80051-f1a3-460c-92ca-fc31bb7417c3)

#### G) `Landmark`
This code implements a real-time face recognition and attendance tracking system.

 Key functions include:

1. **Face Recognition**: Identifies and recognizes "His/Her face" from the camera using a pre-loaded image.
2. **Attentiveness Detection**: Utilizes facial landmarks and head pose estimation to evaluate the subject's attentiveness.
3. **Logging**: Captures each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, updating every 30 seconds.
4. **Live Feedback**: Shows "Attentive" or "Not Attentive" on the video feed, along with facial landmarks.

--The program exits when the 'q' key is pressed.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 052059](https://github.com/user-attachments/assets/8be5cf80-6bfb-4aa8-b89c-63d902654aa7)

![Screenshot 2024-11-17 052203](https://github.com/user-attachments/assets/d1b38770-2d8c-4055-a132-03e1123e67a4)

#### H) `Atten_score`
This script captures real-time webcam video to recognize a person's face and evaluate their attentiveness based on head pose:

1. **Setup**: Loads the face data for the individual and initializes the necessary detection algorithms.
2. **Face Recognition**: Compares detected faces with the known face to determine if there is a match.
3. **Attentiveness Check**: Estimates head orientation (yaw/pitch) to calculate an attentiveness score.
4. **Logging**: Records details (name, date, time, attentiveness, and screenshot) in an Excel file every 30 seconds if the individual is deemed attentive.
5. **Display**: Presents the video feed with face labels, attentiveness status, and facial landmarks. 

The program exits when the 'q' key is pressed, ensuring that the final data is saved to the Excel file.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 054103](https://github.com/user-attachments/assets/37f18506-bd97-450d-8c78-bb0cb47634a2)

![Screenshot 2024-11-17 175557](https://github.com/user-attachments/assets/05c71ec3-15ab-47da-b615-06a19e515df0)


#### I) `Avg_atten_score`
This program captures video from a webcam, performs face recognition to identify a specific individual, calculates attentiveness based on head pose, and logs the data into an Excel file every 30 seconds. Here’s a summary of its main functions:

1. **Face Recognition**: Utilizes the face_recognition library to identify the specified individual by comparing face encodings.
2. **Head Pose Detection**:  Employs dlib's facial landmark predictor to determine head pose (yaw and pitch) for assessing attentiveness.
3. **Attentiveness Calculation**: Computes an attentiveness score based on the yaw and pitch values, ranging from 0 (not attentive) to 1 (fully attentive).
4. **Logging**: Every 30 seconds, the script saves information about recognized faces (including name, date, time, attentiveness status, attention score, and screenshot) into an Excel file.
5. **Display and Feedback**: Displays a live video feed with facial landmarks, attentiveness status, and bounding boxes around detected faces.

At the end of the session, the output includes an Excel file containing the logged details and the average attentiveness score. The user can terminate the video stream by pressing the 'q' key.


- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

- **Output:**

![Screenshot 2024-11-17 054103](https://github.com/user-attachments/assets/37f18506-bd97-450d-8c78-bb0cb47634a2)

![Screenshot 2024-11-17 061841](https://github.com/user-attachments/assets/d738f77d-5b96-45bd-bc2e-467336c05bab)

🏆 Extra Work: Going Beyond the Classroom
Real-Time Face Recognition with Speech Notification
📜 Overview
This system leverages cutting-edge face recognition technology to identify individuals in real-time using live video input. By comparing live video frames to a preloaded known face, the program can accurately determine if the person is recognized. It also provides real-time visual feedback and audio notifications to enhance user interaction.
Apart from the requirements of my coursework, I undertook this project as a personal challenge to push the boundaries of what I’ve learned and apply my skills creatively in the field of computer vision and artificial intelligence.This extra work reflects my dedication to innovation and my passion for developing practical, real-world solutions using AI and machine learning. Below are the enhancements and additional efforts I incorporated:

🎯 Enhanced Features:

Implemented real-time audio notifications using pyttsx3 for recognized and unrecognized individuals, enriching user interaction.
Optimized face detection and recognition by integrating confidence thresholds to improve accuracy.
Designed an intuitive visual feedback system with dynamic bounding boxes and labels for identified and unidentified faces.
Real-Time Interaction:

The program is equipped with a text-to-speech engine, making it more engaging and accessible.
Achieved seamless handling of live video streams while maintaining responsiveness.
Improved User Experience:

Added a graceful exit mechanism with a single key press (q), ensuring all resources are released properly.
Fine-tuned the logic to avoid repetitive announcements for smoother operation.
Personalized Application:

Adapted the system to recognize specific individuals and log attendance or attentiveness as required.

🛠️ Setup Instructions
Prerequisites:
Install Python 3.7 or higher.
Install the required libraries:
bash
Copy code
pip install opencv-python face-recognition pyttsx3
Running the Program:
Place the known image (img.jpeg) in the project directory.
Run the program:
bash
Copy code
python face_recognition_with_speech.py
Allow camera access when prompted.
Press q to stop the program and close the video feed.

- **Input:**

![amol](https://github.com/user-attachments/assets/568c0a1b-39fb-42a8-9723-2a12fd5e8cba)

🖼️ Example Outputs
1. Recognized Face:
Visual Output:
Bounding box with the label "Amol Sharma".
Audio Output:
The system announces: "Amol Sharma".
2. Unrecognized Face:
Visual Output:
Bounding box with the label "Not Recognized".
Audio Output:
The system announces: "Match not found".

🤖 Applications
Authentication Systems: Secure access by verifying identities.
Personal Projects: A fun project to recognize friends or family members.
Learning Purpose: Explore face recognition and text-to-speech integration.

🧩 Future Enhancements
Add support for recognizing multiple known individuals.
Implement a database to dynamically add or remove known faces.
Optimize performance for low-end devices.
