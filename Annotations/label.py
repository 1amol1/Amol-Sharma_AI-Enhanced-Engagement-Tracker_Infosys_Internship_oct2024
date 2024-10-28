import cv2
import os

def draw_bbox(image_dir, label_dir, output_dir, img_ext=".jpg", label_ext=".txt"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define specific label and image files to process
    img_file = "gun" + img_ext
    label_file = "gun" + label_ext

    # Construct full paths for the image and label
    img_path = os.path.join(image_dir, img_file)
    label_path = os.path.join(label_dir, label_file)

    # Load the image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Image not found: {img_path}")
        return

    # Get image dimensions
    height, width, _ = img.shape

    # Open and read label file
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            for line in f.readlines():
                values = line.strip().split()
                class_id = int(values[0])
                x_center, y_center, bbox_width, bbox_height = map(float, values[1:])

                # Calculate bounding box coordinates
                x1 = int((x_center - bbox_width / 2) * width)
                y1 = int((y_center - bbox_height / 2) * height)
                x2 = int((x_center + bbox_width / 2) * width)
                y2 = int((y_center + bbox_height / 2) * height)

                # Draw bounding box
                color = (0, 255, 0)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

                # Add label text
                label = f"Class {class_id}"
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    else:
        print(f"Label file not found: {label_path}")
        return

    # Save the output image
    output_img_path = os.path.join(output_dir, img_file)
    cv2.imwrite(output_img_path, img)
    print(f"Processed: {output_img_path}")

# Define paths
image_dir = r'C:\Users\amols\Downloads\Infosys Springboard\Infosys Springboard 1\Annotations'
label_dir = r'C:\Users\amols\Downloads\Infosys Springboard\Infosys Springboard 1\Annotations'
output_dir = r'C:\Users\amols\Downloads\Infosys Springboard\Infosys Springboard 1\output'

# Run function
draw_bbox(image_dir, label_dir, output_dir)
