import cv2
import numpy as np

# 读取图像
image = cv2.imread('img1.jpg', 0)

# 应用高斯滤波消除噪声
gray = cv2.GaussianBlur(image, (9, 9), 2)

# 应用霍夫变换检测圆
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# 确保至少发现了一个圆
if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # 绘制圆弧
        # cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 圆弧
        # cv2.circle(image, (i[0], i[1]), 2, (0, 128, 128), 3)  # 圆心
        cv2.ellipse(image, center=(i[0], i[1]), axes=(i[2], i[2]), angle=0, startAngle=90, endAngle=180,
                    color=(0, 0, 225), thickness=3)

# 显示结果
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
