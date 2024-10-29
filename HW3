# N10170015_HW3.py
import cv2
import numpy as np
src = cv2.imread("HW3.jpg")                             # 讀取影像
cv2.imshow("Src",src)                                   # 顯示原始影像
dst = cv2.resize(src,None,fx=0.8,fy=1.5)                # 重設影像大小
cv2.imshow("Dst",dst)                                   # 顯示新的影像
dst1 = cv2.flip(dst,1)                                  # 水平翻轉
cv2.imshow("Dst1",dst1)                                 # 顯示水平影像Dst1
dst = cv2.GaussianBlur(dst1,(5,5),0,0)                  # 使用5x5的濾波核
cv2.imshow("Dst2",dst)                                  # 顯示水平影像dst2
cv2.waitKey(0)
cv2.destroyAllWindows ()
cv2.imshow("Dst1",dst1)                                 # 顯示水平影像Dst1
kernel = np.ones((5,5),np.uint8)                        # 建立5x5内核
dst = cv2.morphologyEx(dst1,cv2.MORPH_OPEN,kernel)      # open
cv2.imshow("after OPEN",dst)
dst = cv2.morphologyEx(dst1,cv2.MORPH_CLOSE,kernel)     # close
cv2.imshow("after CLOSE",dst)
dst = cv2.morphologyEx(dst1,cv2.MORPH_GRADIENT,kernel)  # gradient
cv2.imshow("after morpological gradient",dst)
dst = cv2.morphologyEx(dst1,cv2.MORPH_TOPHAT,kernel)    # tophat
cv2.imshow("after tophat",dst)
dst = cv2.morphologyEx(dst1,cv2.MORPH_BLACKHAT,kernel)  # blackhat
cv2.imshow("after blackhat",dst)
cv2.waitKey(0)
cv2.destroyAllWindows ()
