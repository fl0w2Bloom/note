import os

from PIL import Image
from torchvision import transforms
import cv2
import numpy as np
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
img_dir = r'dataset/train/ants'
img_list = os.listdir(img_dir)
img = os.path.join(img_dir, img_list[0])
imgPIL = Image.open(img)
transfrom = transforms.Compose([transforms.PILToTensor(),
                                transforms.Resize(300),
                                transforms.CenterCrop(200),
                                transforms.RandomErasing()
                                ])
img1 = transfrom(imgPIL)
img_tensor = transforms.ToTensor()(imgPIL)
print()
writer.add_image("new picture", img_tensor)
writer.close()
print(img1.shape),
print(type(transforms.ToTensor()(imgPIL)))  # call __call__ function.
array = np.array(img1)
mat = np.uint8(array)
mat = mat.transpose(1, 2, 0)
cv2.imshow("img", mat)
cv2.waitKey()
