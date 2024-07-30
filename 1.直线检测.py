import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("img.jpg")
# 用matplotlib读取图片数据

plt.imshow(img)
plt.show()
print(img.shape)
# 展现图片，展现numpy.ndarray格式的数组

img_gray = np.sum(img, axis=2)
print(img_gray.shape)
# 将每个像素的RGB数据相加，得到灰度图

points_list = []
for i in range(100):
    for j in range(100):
        if img_gray[i][j] < 200:
            img_gray[i][j] = 1
            points_list.append((i, j))
        else:
            img_gray[i][j] = 0
            # 将灰度图数据进行0, 1的划分。方便后续处理
print(len(points_list))# 得到黑色线条的坐标点


def get_line_coef_length(p1, p2):
    # 计算两个点的斜率
    import numpy as np
    x1, y1 = p1
    x2, y2 = p2
    xe = x1 - x2
    ye = y1 - y2
    dist = np.sqrt(xe * xe + ye * ye)
    k = float(y2) - float(y1)
    if x2 - x1 == 0:
        # 当斜率无穷大时，返回180。
        return dist, 180, y1
    k = k / (float(x2) - float(x1))
    k_theta = int(np.arctan(k) / 3.14 * 180.0 + 90.0)
    # 角度的取值范围[-90,90]，k_b_matrix下标从0开始，[-90,90]映射到了[0,180]
    b = y1 - k * x1
    # 线段长度，角度
    return dist, k_theta, b


def get_line_list(point_list):
    # 霍夫直线变换的思路，将斜率和截距投影到霍夫空间进行累加计算
    k_dist_list = np.zeros(200)
    k_b_matrix = np.zeros((200, 200))
    # 声明一个矩阵
    N = len(point_list)
    for i in range(0, N):
        p1 = point_list[i]
        for j in range(i + 1, N):
            p2 = point_list[j]
            dist, k, b = get_line_coef_length(p1, p2)
            # 计算两个p1, p2所在直线的斜率k和截距b
            if np.abs(b) <= 90:
                k_b_matrix[k, int(b + 90)] += 1
                # 遇到斜率k，截距为int(b+90),在矩阵相应位置加1
            if dist > k_dist_list[k]:
                k_dist_list[k] = dist
    return k_dist_list, k_b_matrix



k_dist_list, k_b_matrix = get_line_list(points_list)
print(k_dist_list)
print("*"*10)
print(k_b_matrix)