import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.datasets import CIFAR10
from   torch.utils.tensorboard import SummaryWriter

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2)
        self.maxpool1 = nn.MaxPool2d(kernel_size=2)
        # self.conv2 = nn.Conv2d(32, 32, 5, padding=2, stride=1)
        self.conv2 = nn.LazyConv2d(32, 5, padding=2)
        self.maxpool2 = nn.MaxPool2d(2)
        self.conv3 = nn.Conv2d(32, 64, 5, padding=2)
        self.maxpool3 = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        # self.linear1 = nn.Linear(1024, 64)
        self.linear1 = nn.LazyLinear(64)
        self.linear2 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.conv3(x)
        x = self.maxpool3(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.linear2(x)
        return x


model = Model()
print(model)
inputs = torch.ones([64, 3, 32, 32])
out = model(inputs)
writer = SummaryWriter(r"logs")
writer.add_graph(model,inputs)
writer.close()
print(out.shape)
