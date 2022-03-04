import cv2
import os

top_bound = 100
buttom_bound = 660
left_bound = 195
right_bound = 755
dataset_norm_path = "../dataset/normal"
dataset_excep_path = "../dataset/exceptional"

g = os.walk("../data/异常数据")

for path, dir_list, file_list in g:
    for file_name in file_list:
        img_path = os.path.join(path, file_name)
        img = cv2.imread(img_path, 1)

        cropped = img[top_bound:buttom_bound, left_bound:right_bound]
        if file_name[-5] == "右":
            # 遮盖水印
            cropped[540:560, 480:560] = [0, 0, 0]
        new_Path = os.path.join(dataset_excep_path, file_name)
        cv2.imwrite(new_Path, cropped)

g = os.walk("../data/正常数据")

for path, dir_list, file_list in g:
    for file_name in file_list:
        if file_name[-5] != "右":
            img_path = os.path.join(path, file_name)
            img = cv2.imread(img_path, 1)

            cropped = img[top_bound:buttom_bound, left_bound:right_bound]
            new_Path = os.path.join(dataset_norm_path, file_name)
            cv2.imwrite(new_Path, cropped)
