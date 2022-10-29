from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter(r'logs')
# for i in range(10000):
#     writer.add_scalar("y = x", i ^ 2, i)
# writer.close()
img_path = r'dataset/train/ants/0013035.jpg'
img_PIL = Image.open(img_path)
imgnp = np.array(img_PIL)
writer.add_image("picture", imgnp, 1, dataformats="HWC")
writer.close()
