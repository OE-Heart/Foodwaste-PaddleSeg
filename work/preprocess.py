import cv2
import os

top_bound = 100
buttom_bound = 660
left_bound = 195
right_bound = 755
data_norm_path = "../data/normal"
data_excep_path = "../data/exceptional"

g = os.walk("../origin_data/异常数据")

for path, dir_list, file_list in g:
    for file_name in file_list:
        img_path = os.path.join(path, file_name)
        img = cv2.imread(img_path, 1)

        cropped = img[top_bound:buttom_bound, left_bound:right_bound]
        if file_name[-5] == "右":
            # 遮盖水印
            cropped[540:560, 480:560] = [0, 0, 0]
            # 标准化
            cropped[cropped < 32] = 0
            cropped[(cropped >=32) & (cropped < 96)] = 64
            cropped[(cropped >= 96) & (cropped < 160)] = 128
            cropped[(cropped >= 160) & (cropped < 224)] = 192
            cropped[cropped >=224] = 255
        new_Path = os.path.join(data_excep_path, file_name)
        cv2.imwrite(new_Path, cropped)

g = os.walk("../origin_data/正常数据")

for path, dir_list, file_list in g:
    for file_name in file_list:
        if file_name[-5] != "右":
            img_path = os.path.join(path, file_name)
            img = cv2.imread(img_path, 1)

            cropped = img[top_bound:buttom_bound, left_bound:right_bound]
            new_Path = os.path.join(data_norm_path, file_name)
            cv2.imwrite(new_Path, cropped)
