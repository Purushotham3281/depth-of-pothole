import cv2

# Load an image or frame containing a pothole
image = cv2.imread("C:\\Users\purus\OneDrive\Pictures\pot1.jpg")

# Convert the image to grayscale for edge detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to identify edges
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours to find the pothole
for contour in contours:
    # You may need to set specific criteria to identify the pothole
    # For example, you can check for contour area or shape
    area = cv2.contourArea(contour)
    if area > 1000:
        # Fit a bounding rectangle around the detected pothole
        x, y, width, height = cv2.boundingRect(contour)
        
        # Draw a rectangle around the pothole
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
        
        # Print the width and height of the pothole
        print(f"Pothole Width: {width}, Height: {height}")

# Display the image with bounding boxes
cv2.imshow("Pothole Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
