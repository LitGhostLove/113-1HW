# N10170015_HW5.py
import cv2
import numpy as np

src = cv2.imread("HW5.jpg")
cv2.imshow("src",src)                               # 顯示原始影像

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,60,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_SIMPLE)  
dst1 = cv2.drawContours(src,contours,-1,(0,0,255),5) # 繪製圖形輪廓
cv2.imshow("dst1",dst1)                            # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()


mask = np.ones(src.shape, np.uint8)
mask.fill(255)
dst = cv2.drawContours(mask,contours,-1,(0,0,0),-1) # 繪製圖形輪廓
dst2 = cv2.bitwise_or(src,mask)
cv2.imshow("mask",mask)
cv2.imshow("dst2",dst2)                 # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()


for c in contours:                                  # 繪製中心點迴圈
    M = cv2.moments(c)                              # 影像矩
    Cx = int(M["m10"] / M["m00"])                   # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])                   # 質心 y 座標
    cv2.circle(dst2,(Cx,Cy),5,(255,0,0),-1)          # 繪製中心點
cv2.imshow("dst3",dst2)                            # 顯示結果影像


dst4=dst2.copy()
box = cv2.minAreaRect(contours[0])                      # 建構最小矩形
print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)                             # 獲取頂點座標
points = np.intp(points)                                # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")
dst = cv2.drawContours(dst4,[points],0,(0,255,0),2)      # 繪製輪廓
cv2.imshow("dst4",dst4)


dst5=dst2.copy()
hull = cv2.convexHull(contours[0])                  # 獲得凸包頂點座標       
dst5 = cv2.polylines(dst5, [hull], True, (0,255,0),2) # 將凸包連線
cv2.imshow("dst5",dst5)
convex_area = cv2.contourArea(hull)                 # 凸包面積
print(f"凸包面積 = {convex_area}")

cv2.waitKey(0)
cv2.destroyAllWindows()
