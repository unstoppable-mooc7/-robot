import numpy as np
import matplotlib.pyplot as plt

# 定义圆心、半径和圆弧角度
center = (0, 0)
radius = 1.0
angle = np.pi / 4  # 圆弧角度为45度

# 定义圆弧的边界点
theta = np.linspace(0, angle, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# 创建一个圆弧
arc = plt.figure(figsize=(5, 5))
plt.axes().set_aspect('equal')
plt.axes().plot(x, y, color='blue')
plt.axes().scatter(center[0], center[1], color='black')  # 圆心
plt.axes().set_xlim(-1.5, 1.5)
plt.axes().set_ylim(-1.5, 1.5)


# 检测点是否在圆弧内
def is_point_in_arc(point, center, radius, start_angle, end_angle):
    angle_to_point = np.arctan2(point[1] - center[1], point[0] - center[0])
    if angle_to_point < 0:
        angle_to_point += 2 * np.pi
    if start_angle > end_angle:
        return (angle_to_point > start_angle) or (angle_to_point < end_angle)
    else:
        return (angle_to_point > start_angle) and (angle_to_point < end_angle)


# 测试点
test_point = (np.cos(np.pi / 8), np.sin(np.pi / 8))
plt.axes().scatter(test_point[0], test_point[1], color='red')

# 检测结果
inside_arc = is_point_in_arc(test_point, center, radius, 0, angle)
plt.axes().text(test_point[0], test_point[1], 'Inside' if inside_arc else 'Outside', color='red')

plt.show()