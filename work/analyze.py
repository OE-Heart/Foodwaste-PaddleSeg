import os
import numpy as np
from matplotlib import pyplot as plt
import cv2

path = "../dataset/exceptional/1061645右.png"

# 读入图片
img = cv2.imread(path, 1)
if img is None:
    print("图片读入失败, 请检查图片路径及文件名")
    exit()

# 创建画布
fig, ax = plt.subplots()

# Matplotlib预设的颜色字符
bgrColor = ("b", "g", "r")

# 统计窗口间隔 , 设置小了锯齿状较为明显 最小为1 最好可以被256整除
bin_win = 4
# 设定统计窗口bins的总数
bin_num = int(256 / bin_win)
# 控制画布的窗口x坐标的稀疏程度. 最密集就设定xticks_win=1
xticks_win = 2

for cidx, color in enumerate(bgrColor):
    # cidx channel 序号
    # color r / g / b
    cHist = cv2.calcHist([img], [cidx], None, [bin_num], [0, 256])
    # 绘制折线图
    ax.plot(cHist, color=color)


# 设定画布的范围
ax.set_xlim([0, bin_num])
ax.set_ylim([0, 10000])
# 设定x轴方向标注的位置
ax.set_xticks(np.arange(0, bin_num, xticks_win))
# 设定x轴方向标注的内容
ax.set_xticklabels(list(range(0, 256, bin_win * xticks_win)), rotation=45)

plt.savefig("fig")
