import cv2
import serial

rostoEx = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
sorrisoEx = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

serialCom = serial.Serial('COM3', 9600)
aux=''
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rostos = rostoEx.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    sttsSerial = "off"

    for (x, y, w, h) in rostos:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        sorriso = sorrisoEx.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)

        for (sx, sy, sw, sh) in sorriso:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            sttsSerial = "on"
    
    
    if(aux!=sttsSerial):
        print(sttsSerial)
        aux=sttsSerial
        serialCom.write(sttsSerial.encode())

    cv2.imshow("Detecao de sorrisos", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
