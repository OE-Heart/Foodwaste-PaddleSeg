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
            
            # cropped[(cropped == [128, 128, 0]).all(axis=2)] = [128, 128, 64]
            # cropped[(cropped == [128, 64, 0]).all(axis=2)] = [128, 0, 64]
            # cropped[(cropped == [128, 64, 64]).all(axis=2)] = [128, 0, 64]
            # cropped[(cropped == [128, 128, 192]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [0, 128, 64]).all(axis=2)] = [0, 128, 128]
            # cropped[(cropped == [64, 128, 0]).all(axis=2)] = [0, 128, 0]
            # cropped[(cropped == [64, 128, 64]).all(axis=2)] = [128, 128, 64]
            # cropped[(cropped == [64, 128, 128]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [64, 192, 192]).all(axis=2)] = [0, 128, 192]
            # cropped[(cropped == [64, 128, 192]).all(axis=2)] = [0, 128, 192]
            # cropped[(cropped == [0, 64, 0]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [0, 64, 64]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [192, 128, 128]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [0, 0, 64]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [0, 64, 128]).all(axis=2)] = [0, 128, 128]
            # cropped[(cropped == [64, 64, 0]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [64, 0, 0]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [64, 64, 64]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [64, 0, 64]).all(axis=2)] = [0, 0, 0]
            # cropped[(cropped == [64, 64, 128]).all(axis=2)] = [64, 0, 128]
            # cropped[(cropped == [0, 64, 192]).all(axis=2)] = [0, 0, 192]
            # cropped[(cropped == [64, 0, 128]).all(axis=2)] = [0, 0 , 128]
            # cropped[(cropped == [64, 64, 192]).all(axis=2)] = [0, 0, 192]
            # cropped[(cropped == [192, 64, 64]).all(axis=2)] = [128, 0, 64]
            # cropped[(cropped == [64, 0, 192]).all(axis=2)] = [0, 0, 192]
            # cropped[(cropped == [192, 128, 0]).all(axis=2)] = [128, 128, 64]
            # cropped[(cropped == [192, 64, 0]).all(axis=2)] = [128, 0, 0]
            # cropped[(cropped == [192, 128, 64]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [192, 192, 192]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [192, 0, 0]).all(axis=2)] = [128, 0, 0]
            # cropped[(cropped == [192, 0, 64]).all(axis=2)] = [128, 0, 0]
            # cropped[(cropped == [0, 0, 255]).all(axis=2)] = [0, 0, 192]
            # cropped[(cropped == [128, 64, 128]).all(axis=2)] = [128, 128, 128]
            # cropped[(cropped == [128, 128, 64]).all(axis=2)] = [128, 128, 128]

            cropped[(cropped == [128, 128, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [128, 64, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [128, 64, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [128, 128, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 128, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 128, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 128, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 128, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 192, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 128, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 64, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 64, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 128, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 0, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 64, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 64, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 0, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 64, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 0, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 64, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 64, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 0, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 64, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 64, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [64, 0, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 128, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 64, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 128, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 192, 192]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 0, 0]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [192, 0, 64]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [0, 0, 255]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [128, 64, 128]).all(axis=2)] = [0, 0, 0]
            cropped[(cropped == [128, 128, 64]).all(axis=2)] = [0, 0, 0]

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
