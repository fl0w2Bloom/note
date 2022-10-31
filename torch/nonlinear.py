import torch
from torch import nn
from torch.utils.tensorboard import SummaryWriter
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader

inputValue = torch.tensor([
    [1, -0.5],
    [-1, 3]
])

output = torch.reshape(inputValue, (-1, 1, 2, 2))
print(output.shape)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.relu1 = nn.ReLU()
        self.softmax = nn.Softmax()

    def forward(self, x):
        x = self.softmax(x)
        return x


model = Model()
out = model(output)
print(out)
writer = SummaryWriter(r"logs")
CIFAR10dataset = CIFAR10(
    root=r'cifar',
    train=False,
    transform=transforms.ToTensor(),
    download=True
)
dataloader = DataLoader(dataset=CIFAR10dataset, batch_size=64)

step = 0
for idx, (img, target) in enumerate(dataloader):
    writer.add_images("before", img, step)
    out = model(img)
    writer.add_images("after", out, step)
    step += 1
writer.close()
