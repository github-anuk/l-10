# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

cap=cv2.VideoCapture("C:/Users/Anukriti/Desktop/all my files (anukriti)python/projects/open cv/l-10/cars.mp4")

car_cascade=cv2.CascadeClassifier("C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-10/cars.xml")

while True:
    ret,frames=cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    car=car_cascade.detectMultiScale(frames,1.1,1)
    for (x,y,w,h) in car:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("autmobiles with rectangles on them",frames)
    if cv2.waitKey(33)==27:
        break

cv2.destroyAllWindows()


