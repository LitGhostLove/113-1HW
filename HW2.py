# N10170015_HW2.py
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
white = (255,255,255)
red   = (  0,  0,255)

def cv2_Chinese_Text(img,text,left,top,textColor,fontSize):
    '''建立中文字輸出'''
# 影像轉成PIL影像格式
    if (isinstance(img,np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)              #建立PIL繪圖物件
    fontText = ImageFont.truetype(          #建立字型 - 新細明體
                "C:\Windows\Fonts\mingliu.ttc",         #新細明體
                fontSize,                   # 字型大小
                encoding="utf-8")           # 编碼方式
    draw.text((left,top),text,textColor,font=fontText)  # 繪製中文字
#將PIL影像格式轉成OpenCV影像格式
    return cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

img = cv2.imread('lena.jpg')
cv2.imshow('lena', img)
cv2.rectangle(img,(100,100),(250,260),red)  # 繪製矩形 
img = cv2_Chinese_Text(img, "黃晉瑋", 215, 280, white, 30)
cv2.ellipse(img,(260,295),(55,25),0,0,360,white,3)
cv2.imshow("lena1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread('back.jpg')
cv2.imshow('back', img2)
alpha = 1
beta = 1
gamma = 1
dst = cv2.addWeighted(img,alpha,img2,beta,gamma)    # 加權和
cv2.imshow("lena+back",dst)                         # 顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows ()

cv2.imshow("lena+back",dst)
img_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)    # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)
thresh = 127                                        # 閾值
maxval = 255                                        # 定義像素最大值
# 自適應閥值計算方法為ADAPTIVE_THRESHEAN_C
dst_mean = cv2.adaptiveThreshold(img_gray,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,3,5)
# 自適應閥值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(img_gray,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY,3,5)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C",dst_mean)       # 顯示自適應閥值結果
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",dst_gauss)  # 顯示自適應閥值結果
cv2.waitKey(0)
cv2.destroyAllWindows()
