import pyqrcodeng as pyqrcode 
import cv2

'''
qr = pyqrcode.create("polar bear")
qr.png('polar-bear.png', scale=5)
qr_pic = cv2.imread('polar-bear.png')
cv2.imshow('qr_pic', qr_pic)
cv2.waitKey(0)
'''

url = pyqrcode.create("www.robot_samurai.com")
url.png('robot-samurai.png', scale=25)
qr_pic = cv2.imread('robot-samurai.png')
cv2.imshow('qr_pic', qr_pic)
cv2.waitKey(0)