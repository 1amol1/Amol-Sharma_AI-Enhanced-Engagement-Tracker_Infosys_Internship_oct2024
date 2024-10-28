import cv2

# Load the images
img = cv2.imread('image1.jpg', 0)  # Load the source image in grayscale
template = cv2.imread('image2.jpg', 0)  # Load the template image in grayscale

# Check if images are loaded properly
if img is None:
    print("Error loading image1.jpg")
    exit()
if template is None:
    print("Error loading image2.jpg")
    exit()

# Perform template matching
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# Get the best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the matched region
cv2.rectangle(img, top_left, bottom_right, (255, 255, 255), 3)

# Display the result
cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()