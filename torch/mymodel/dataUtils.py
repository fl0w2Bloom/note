from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader

__ALL__ = ["train_data", "test_data", "train_dataloader", "test_dataloader", "batch_size", "test_data_size",
           "train_data_size"]
batch_size = 128

train_data = CIFAR10(
    root=r'cifar',
    train=True,
    transform=transforms.ToTensor(),
    download=True,
)

test_data = CIFAR10(
    root=r'cifar',
    train=False,
    transform=transforms.ToTensor(),
    download=True
)
test_data_size = len(test_data)
train_data_size = len(train_data)
train_dataloader = DataLoader(train_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)
