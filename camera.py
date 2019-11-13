import time

import cv2

pic_num = 30
root = ("../face_pic/")
bool_break = 0
#웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

#얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i = 0
while(True):
    # frame 별로 capture 한다
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    frame_c = frame.copy()
    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x-40,y-40),(x+w+40,y+h+40),(255,0,0),2)
        # cropping & save
        face = frame_c[y-30:y+h+30,x-30:x+w+30]
        cv2.imwrite(root+str(i)+".jpg",face)
        i += 1
        time.sleep(0.5)
        if i == pic_num:
            bool_break = 1
            break        
    cv2.imshow('frame',frame)
    if bool_break == 1:
        break
    
    if cv2.waitKey(100) & 0xFF == ord('q'):               
        break
    
cap.release()
cv2.destroyAllWindows()
