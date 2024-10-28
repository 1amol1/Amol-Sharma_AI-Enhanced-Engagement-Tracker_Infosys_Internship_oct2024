import cv2
image_filenames = ["image1.jpg", "image2.jpg"]  # Replace with your actual image names

for filename in image_filenames:
    image = cv2.imread(filename)
    if image is not None:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"{filename} dimensions: {image.shape}")
    else:
        print(f"Failed to load {filename}")