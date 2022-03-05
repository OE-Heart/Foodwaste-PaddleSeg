import os
import numpy as np
from matplotlib import pyplot as plt
import cv2

output_path = "../output/analyze"

bgrColor = ("b", "g", "r")
# 统计窗口间隔 , 设置小了锯齿状较为明显 最小为1 最好可以被256整除
bin_win = 4
# 设定统计窗口bins的总数
bin_num = int(256 / bin_win)
# 控制画布的窗口x坐标的稀疏程度
xticks_win = 2

g = os.walk("../dataset/exceptional")

for path, dir_list, file_list in g:
    for file_name in file_list:
        if file_name[-5] != '右':
            continue
        img_path = os.path.join(path, file_name)
        img = cv2.imread(img_path, 1)

        if img is None:
            print("图片读入失败, 请检查图片路径及文件名")
            exit()

        fig, ax = plt.subplots()

        for cidx, color in enumerate(bgrColor):
            # cidx channel 序号
            # color r / g / b
            cHist = cv2.calcHist([img], [cidx], None, [bin_num], [0, 256])
            ax.plot(cHist, color=color)

        ax.set_xlim([0, bin_num])
        ax.set_ylim([0, 10000])
        ax.set_xticks(np.arange(0, bin_num, xticks_win))
        ax.set_xticklabels(list(range(0, 256, bin_win * xticks_win)), rotation=45)

        plt.savefig(os.path.join(output_path, file_name))