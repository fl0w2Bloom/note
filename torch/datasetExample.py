from torchvision import datasets
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from torch.utils.data import DataLoader

train_dataset = datasets.MNIST(
    root='mnist',
    train=True,
    transform=transforms.ToTensor(),
    download=True)
test_data = datasets.MNIST(root='mnist',
                           train=False,
                           transform=transforms.ToTensor(),
                           download=True)
writer = SummaryWriter("logs")
trainDataLoader = DataLoader(train_dataset, 12, shuffle=True, num_workers=4)
testDataLoader = DataLoader(test_data, batch_size=12, num_workers=4)
writer.close()
