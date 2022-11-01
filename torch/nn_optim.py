import torch.nn as nn
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torchvision import transforms

datasets = CIFAR10(
    root=r'cifar',
    train=False,
    transform=transforms.ToTensor(),
    download=True,
)

dataloader = DataLoader(datasets, batch_size=64)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.seqls1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, padding=2, stride=1),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.seqls1(x)
        return x


model = Model()

# test code
# tensor = torch.ones([1, 3, 32, 32], dtype=torch.float)
# print(model(tensor).shape)

optim = torch.optim.SGD(model.parameters(), lr=0.05)
loss_fn = nn.CrossEntropyLoss()
for epoch in range(10):
    running_loss = 0.0
    for idx, (imgs, targets) in enumerate(dataloader):
        output = model(imgs)
        loss = loss_fn(output, targets)
        optim.zero_grad()
        loss.backward()
        optim.step()
        running_loss += loss
    print(running_loss)
