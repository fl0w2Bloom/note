import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

CIFAR10dataset = CIFAR10(
    root=r'cifar',
    train=True,
    transform=transforms.ToTensor(),
    download=True,
)
dataloader = DataLoader(dataset=CIFAR10dataset, batch_size=64)


# writer = SummaryWriter(r'logs')
# step = 0
# for idx, (img, targets) in enumerate(dataloader):
#     # img [64,3,x,y]
#     # target [ x,x,x,x]
#     print(img[1].shape)
#     print(targets)
#     for i, v in enumerate(targets):
#         print(CIFAR10dataset.classes[v])
#         writer.add_image("q", img[i], i)
#         print(i)
#         if i == 6:
#             break
#     break
# writer.close()

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = nn.Linear(3072,10)

    def forward(self, x):
        x = self.linear1(x)
        return x


model = Model()
img, targets = next(iter(dataloader))
print(img.shape)
flatten = torch.flatten(img[0])
print(flatten.shape)
out = model(flatten)
print(out.shape)