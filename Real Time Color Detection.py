import cv2
import pandas as pd
import numpy as np

# Initialize global variables
r = g = b = xpos = ypos = 0

# Load the color data
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv('Color-Detection\\Data\\colors.csv', names=index, header=None)

# Define the callback function for mouse events
def update_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b, g, r = int(frame[y, x, 0]), int(frame[y, x, 1]), int(frame[y, x, 2])
        print("R =", r, "G =", g, "B =", b)
    xpos, ypos = x, y

# Function to get color name from RGB values
def colorname(B, G, R):
    minimum = 10000
    cname = ""
    for i in range(len(df)):
        d = np.sqrt((B - int(df.loc[i, "B"]))**2 + (G - int(df.loc[i, "G"]))**2 + (R - int(df.loc[i, "R"]))**2)
        if d <= minimum:
            minimum = d
            cname = df.loc[i, "color_name"] + " Hex " + df.loc[i, "hex"]
    return cname

# Open a connection to the webcam
camera = cv2.VideoCapture(0)

# Setup the window and callback
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", update_color)

while True:
    # Capture frame-by-frame
    grabbed, frame = camera.read()
    if not grabbed:
        break

    # Draw a rectangle and put text for the color name and RGB values
    frame_copy = frame.copy()
    imgWidth = frame.shape[1]-50
    cv2.rectangle(frame_copy, (20, 20), (imgWidth, 60), (b, g, r), -1)
    text = colorname(b, g, r) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    cv2.putText(frame_copy, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    if r + g + b >= 600:
        cv2.putText(frame_copy, text, (50, 50), 1, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Draw a bright cursor (e.g., a yellow cross)
    cv2.drawMarker(frame_copy, (xpos, ypos), (0, 255, 255), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)
    
    # Display the resulting frame
    cv2.imshow("Webcam", frame_copy)

    # Break the loop when 'ESC' key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
