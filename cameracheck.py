import cv2

# Initialize the camera (0 is usually the default camera, change to 1, 2, etc., for other cameras)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture the frame.")
        break

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Press 'q' to exit the camera feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
