import cv2
import numpy as np

# 读取图像
image = cv2.imread('img1.jpg')

# 转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用Canny算子进行边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 应用Hough变换检测直线
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)


def dist(x1, y1, x2, y2):
    mm = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return int(mm ** 0.5)


print("直线的条数:", len(lines))
print("直线的位置", end=":")
length = []
# 绘制直线
for line in lines:
    x1, y1, x2, y2 = line[0]
    print("(%d, %d), (%d, %d)" % (x1, y1, x2, y2), end="\n\t\t")
    length.append(dist(x1, y1, x2, y2))
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
print()
print("直线的长度：", *length)

# 显示结果
cv2.imshow('Lines Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
