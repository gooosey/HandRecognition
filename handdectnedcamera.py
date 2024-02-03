import cv2
import mediapipe as mp

# Find face 
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Create Hand object
mp_hands = mp.solutions.hands.Hands()

# Initialize video capture (use 0 for the default camera, change if using an external camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the camera
    ret, frame = cap.read()

    # Break the loop if there's an issue with the camera
    if not ret:
        print("Failed to capture frame.")
        break

    # Convert the BGR image to RGB 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = mp_hands.process(rgb_frame)

    # Check if results are valid
    if results is not None:
        # Check if hands are detected
        if results.multi_hand_landmarks:
            print("hand")
            
            # Loop through each detected hand
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    # Extract x, y, and z coordinates of each landmark
                    x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]) ,int(landmark.z * 1000)
                    cv2.circle(frame, (x,y), 15, (0,255,0))
                    print(x,y,z)

    # Error handling
        else:
            print("No hands detected")
    else:
        print("??")
    
    # Invert camera
    fliphaha = cv2.flip(frame, 1)

    # Display the frame
    cv2.imshow('Hand Tracking', fliphaha)

    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()