import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ff = np.fromfile(r'park.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray find', gray)

faces = face_cascade.detectMultiScale(gray, 1.2,5)
for (x,y,w,h) in faces:
    face_img = img[y:y+h, x:x+w]
    face_img = cv2.resize(face_img, dsize=(0,0), fx=0.1, fy=0.1)
    face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = face_img
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('img1.jpg', img)