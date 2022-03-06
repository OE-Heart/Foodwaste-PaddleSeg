import os
import cv2

images_path = "../dataset/images"
labels_path = "../dataset/annotations"

train_file = open('../dataset/train_list.txt', 'w+')
val_file = open('../dataset/val_list.txt', 'w+')
test_file = open('../dataset/test_list.txt', 'w+')

g = os.walk("../data/exceptional")

cnt = 0

for path, dir_list, file_list in g:
    for file_name in file_list:
        if file_name[-5] == "左":
            continue

        img_path = os.path.join(path, file_name)

        if file_name[-5] == "中":
            img = cv2.imread(img_path, 1)
            file_name = file_name.replace(file_name[-5], "", 1)
            new_Path = os.path.join(images_path, file_name)

            if (cnt % 10 == 4):
                val_file.write("images/"+file_name+" labels/"+file_name+'\n')
            elif (cnt % 10 == 9):
                test_file.write("images/"+file_name+" labels/"+file_name+'\n')
            else:
                train_file.write("images/"+file_name+" labels/"+file_name+'\n')

            cnt += 1
        
        if file_name[-5] == "右":
            img = cv2.imread(img_path, 0)
            img[img == 14] = 1
            img[img == 33] = 2
            img[img == 38] = 3
            img[img == 52] = 4
            img[img == 57] = 5
            img[img == 75] = 6
            img[img == 113] = 7
            img[img == 128] = 8
            img[img == 132] = 9
            file_name = file_name.replace(file_name[-5], "", 1)
            new_Path = os.path.join(labels_path, file_name)

        cv2.imwrite(new_Path, img)

train_file.close()
val_file.close()
test_file.close()