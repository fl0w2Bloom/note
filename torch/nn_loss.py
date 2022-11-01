import torch
import torchvision.datasets
from torch import nn
from torch.nn import L1Loss, MSELoss, CrossEntropyLoss
from torch.utils.data import DataLoader

inputs = torch.tensor([1, 2, 3], dtype=torch.float32)
targets = torch.tensor([1, 2, 5], dtype=torch.float32)
result = L1Loss(reduction="sum")(inputs, targets)
print(result)

mesLoss = MSELoss()
result = mesLoss(inputs, targets)
print(result)
print("{:.4f}".format(4 / 3))
crossEntropy = CrossEntropyLoss()
result = crossEntropy(inputs, targets)
print(result)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.seqs1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.seqs1(x)
        return x


data = torchvision.datasets.CIFAR10(
    root=r'cifar',
    train=False,
    download=True,
    transform=torchvision.transforms.ToTensor()
)
dataloader = DataLoader(data, batch_size=32)
tensor_test = torch.ones([1, 3, 32, 32], dtype=torch.float32)
print(tensor_test.shape)
model = Model()
loss = torch.nn.CrossEntropyLoss()
print(model(tensor_test).shape)
for idx, (img, targets) in enumerate(dataloader):
    output = model(img)
    print(output.shape)
    print(len(targets))
    print(img.shape)
    result = loss(output, targets)
    result.backward()
    print(result)

