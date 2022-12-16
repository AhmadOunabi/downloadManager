from platform import release
import cv2
import tkinter as tk
tk.Tk()



cam=cv2.VideoCapture(0)
cv2.namedWindow("Kamera")

while True:
    ret,frame=cam.read()
    cv2.imshow('Kamera',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
    
cam.release()
cv2.destroyAllWindows()
