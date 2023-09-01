import cv2
import webbrowser

cap = cv2.VideoCapture(1) #Here the value 1 represent the camera number and it depends on system to decide the camera number 
detector = cv2.QRCodeDetector() #assigning alias to various open-cv functionalities

while True:
    _, img = cap.read() 
    data,_,__ = detector.detectAndDecode(img)
    if (data):
        a=data
        break
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break

b=webbrowser.open(str(a)) #Opens the browser using the qr_code data recieved
cap.release() #freeing the camera
cv2.destroyAllWindows()#closes the camera view window

