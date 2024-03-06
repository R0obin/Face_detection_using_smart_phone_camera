import cv2

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize the video capture object
# If using webcam
video = cv2.VideoCapture(0)  

# If using smartphone camera through IP address
smart_phone_camera_ip_address = "http://192.168.1.100/video"
video.open(smart_phone_camera_ip_address)

while True:
    # Capture frame-by-frame
    ret, frame = video.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow("camera", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
video.release()
cv2.destroyAllWindows
