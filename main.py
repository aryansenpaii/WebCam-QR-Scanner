import cv2
import webbrowser

cap = cv2.VideoCapture(1)
detector = cv2.QRCodeDetector() 

while True:
    _, img = cap.read()
    data,_,__ = detector.detectAndDecode(img)
    if (data):
        a=data
        break
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()

