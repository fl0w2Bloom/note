import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

CIFAR10Dataset = CIFAR10(
    root=r'cifar',
    train=False,
    transform=transforms.ToTensor(),
    download=True,
)
dataloader = DataLoader(dataset=CIFAR10Dataset, batch_size=64)

writer = SummaryWriter(r'logs')


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
        self.maxpool1 = nn.MaxPool2d(kernel_size=3, ceil_mode=True)
        self.avfpool = nn.AvgPool2d(3)

    def forward(self, x):
        # x = self.conv1(x)
        # x = self.maxpool1(x)
        x = self.maxpool1(x)
        return x


tensor1 = torch.tensor([
    [
        [1, 2, 0, 3, 1],
        [0, 1, 2, 3, 1],
        [1, 2, 1, 0, 0],
        [5, 2, 3, 1, 1],
        [2, 1, 0, 1, 1]
    ]
], dtype=torch.float)
model = Model()

m = nn.MaxPool2d(3, ceil_mode=True)
print(m(tensor1))
# step = 0
# for idx, (img, target) in enumerate(dataloader):
#     output = model(img)
#     # print(img.shape)
#     # print(output.shape)
#     # break
#     writer.add_images("input", img, step)
#     writer.add_images("output", output, step)
#     step += 1
from PIL import Image

img0 = Image.open(r'preview.jpg')
tensorImg = transforms.PILToTensor()(img0)
print(tensorImg.dtype)
tensorImg = torch.tensor(tensorImg.clone().detach(), dtype=torch.float32)
out = model(tensorImg)
writer.add_image("before", transforms.PILToTensor()(img0), 1)
writer.add_image("after ", out, 1)
writer.close()
