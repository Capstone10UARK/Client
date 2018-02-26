import cv2
cap = cv2.VideoCapture("C:/Users/snyde/Documents/Capstone/videos/VFI_NoArrows.avi")
count = 0

while count < cap.get(cv2.CAP_PROP_FRAME_COUNT):
    ret,frame = cap.read()
    frame = frame[0:0+725, 188:188+465]
    cv2.imwrite("C:/Users/snyde/Documents/Capstone/frameOutput/frames/frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
