import cv2
import time

my_input = ""

# Function to take picture with enter
def prepare_input():
    pic1 = cv2.imread("temporary_pics/insert.png")
    cv2.imshow('image', pic1)
    cv2.waitKey(1)
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    key = input("Tryk Enter for at tage billede")
    if key == "q":
        quit()
    ret,frame = cap.read() # return a single frame in variable `frame`
    #Save the picture in "camera_pics"
    cv2.imwrite("camera_pic.png", frame)
    cap.release()

    my_input = "camera_pic.png"
    return my_input

