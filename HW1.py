# N10170015_HW1.py
import cv2

bgr = cv2.imread("lena.jpg")
cv2.imshow('lenaBgr', bgr)
blue, green, red = cv2.split(bgr)
cv2.imshow('lenaRed', red)
red[:,:] = 255
image1 = cv2.merge([blue,green,red])
cv2.imshow('lenaR255',image1)
cv2.imwrite('lena1.jpg',image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('lenaBgr', bgr)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
cv2.imshow('lenaHsv', hsv)
hue, saturation, value = cv2.split(hsv)
cv2.imshow('lenaHue', hue)
hue[:,:] = 255
hsv = cv2.merge([hue, saturation, value])
cv2.imshow('lenaH255Hsv',hsv)
image2 = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('lenaH255Bgr',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
