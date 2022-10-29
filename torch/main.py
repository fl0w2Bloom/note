import os
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
from torch.utils.data import Dataset


class ABDataSet(Dataset):
    def __init__(self, root_dir, imgs_dir, labels_dir):
        self.root_dir = root_dir
        self._img_dir = imgs_dir
        self._labels_dir = labels_dir
        self.img_dir = os.path.join(self.root_dir, self._img_dir)
        self.labels_dir = os.path.join(self.root_dir, self._labels_dir)
        self.img_list = os.listdir(self.img_dir)
        self.labels_list = os.listdir(self.labels_dir)

    def __getitem__(self, item):
        img_item = self.img_list[item]
        img = os.path.join(self.img_dir, img_item)
        # print(img_item.rsplit('.')[0])
        # print(os.path.splitext(img_item)[0])
        # 寻找img——item 同名文件
        for i in self.labels_list:
            if str(i).rsplit('.')[0] == os.path.splitext(img_item)[0]:
                # 读取文件内容作为label
                with open(os.path.join(self.labels_dir, i)) as f:
                    label = f.readline()
                    return img, label

    def __len__(self):
        return len(self.img_list)


if __name__ == '__main__':
    root_dir = r'dataset2/train'
    ants_img_dir = r'ants_image'
    ants_labels_dir = r'ants_label'
    bees_img_dir = r'bees_image'
    bees_labels_dir = r'bees_label'

    ant_data = ABDataSet(root_dir, ants_img_dir, ants_labels_dir)
    bee_data = ABDataSet(root_dir, bees_img_dir, bees_labels_dir)

    print(ant_data[0])
    data = ant_data + bee_data
    print(len(data))
    # Image.open(data[123][0]).show()
    # Image.open(data[124][0]).show()

    write = SummaryWriter(r'logs')
    for idx, i in enumerate(data):
        write.add_image(os.path.splitext(i[0])[0], np.array(Image.open(i[0])), idx, dataformats="HWC")
    write.close()
    # print(str(list1[0]).rsplit('.')[0])
    # print(os.path.splitext(list1[0])[0])
