#N10170015_HW4
import cv2

src = cv2.imread("hand.jpg",cv2.IMREAD_GRAYSCALE)   # 黑白讀取
src = cv2.GaussianBlur(src,(3,3),0)             # 降低噪音
# Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst_sobel =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)    # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)        # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)        # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst_scharr =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)   # 影像融合
# Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F,ksize=3)    # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)          # 將負值轉正值
# Canny()函數
dst_canny = cv2.Canny(src, 50, 100)             # minVal=50, maxVal=100
# 輸出影像梯度
cv2.imshow("src", src)
cv2.imshow("Canny", dst_canny)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)
cv2.imshow("Laplacian", dst_lap)

cv2.waitKey(0)
cv2.destroyAllWindows()


src = cv2.imread("hand.jpg")           # 讀取影像
downDst1 = cv2.pyrDown(src)                 # 第 1 次向下採樣
downDst2 = cv2.pyrDown(downDst1)                # 第 2 次向下採樣
downDst3 = cv2.pyrDown(downDst2)                # 第 3 次向下採樣
print(f"src.shape = {src.shape}")
print(f"downDst1.shape = {downDst1.shape}")
print(f"downDst2.shape = {downDst2.shape}")
print(f"downDst3.shape = {downDst3.shape}")

cv2.imshow("src",src)
cv2.imshow("downDst1",downDst1)
cv2.imshow("downDst2",downDst2)
cv2.imshow("downDst3",downDst3)

cv2.waitKey(0)
cv2.destroyAllWindows()


upDst1 = cv2.pyrUp(downDst3)                   # 第 1 次向上採樣
upDst2 = cv2.pyrUp(upDst1)                  # 第 2 次向上採樣
upDst3 = cv2.pyrUp(upDst2)                  # 第 3 次向上採樣

print(f"downDst3.shape = {downDst3.shape}")
print(f"upDst1.shape = {upDst1.shape}")
print(f"upDst2.shape = {upDst2.shape}")
print(f"upDst3.shape = {upDst3.shape}")
cv2.imshow("downDst3",downDst3)
cv2.imshow("upDst1",upDst1)
cv2.imshow("upDst2",upDst2)
cv2.imshow("upDst3",upDst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

