import torch
from torch import nn
from torchvision import transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# create hyper-parameters
lr = 3e-2
epochs = 10
batch_size = 64

# get train and test CIFAR10 Dataset
train_data = CIFAR10(
    root=r'cifar',
    train=True,
    download=True,
    transform=transforms.ToTensor(),
)

test_data = CIFAR10(
    root=r'cifar',
    train=False,
    download=True,
    transform=transforms.ToTensor(),
)

# get train and test dataloader
trainDataLoader = DataLoader(train_data, batch_size=batch_size)
testDataLoader = DataLoader(test_data, batch_size=batch_size)

# get train and test dataset size
train_data_size = len(train_data)
test_data_size = len(test_data)
print(f'train_data_size: {train_data_size}')
print(f'test_data_size: {test_data_size}')


# build model
# The Model class inherits from the nn.Module class, which contains the basic functionality needed to create a neural
# network
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=1),
            nn.MaxPool2d(kernel_size=2),

        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(576, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        """
        The function takes in an image, passes it through the network to obtain the features (x), makes a prediction with
        the classifier, and returns the class scores

        :param x: input tensor
        :return: The output of the classifier
        """
        x = self.features(x)
        x = self.classifier(x)
        return x

# model ,data , loss function add .cuda
# test network code
# tensor = torch.ones([1, 3, 32, 32], dtype=torch.float)
# result = model(tensor)
# print(result.shape)
# create model
model = Model()
# print(model)

# create loss function
loss_fn = nn.CrossEntropyLoss()
# create optimizer
optim = torch.optim.SGD(model.parameters(), lr=lr)
# record train times
total_train_steps = 0
total_test_steps = 0
# tensorboard
writer = SummaryWriter(r'logs')

# train process
for epoch in range(epochs):
    print(f'---------第{epoch + 1}轮开始训练---------')
    running_loss = 0.0
    model.train()
    for idx, (imgs, targets) in enumerate(trainDataLoader):
        output = model(imgs)
        loss = loss_fn(output, targets)
        optim.zero_grad()
        loss.backward()
        optim.step()
        running_loss += loss.item()
        total_train_steps += 1
        if total_train_steps % 100 == 0:
            print(f'训练次数:{total_train_steps},误差: {loss.item()}')
            writer.add_scalar("train_loss", loss.item(), total_train_steps)
    # if epoch % 5 == 0:
    #     torch.save(model.state_dict(), f'model{epoch}.pth')
    print(running_loss)

    # test begin

    model.eval()
    total_test_loss = 0.0
    total_accuracy = 0.0
    with torch.no_grad():
        for idx, (imgs, targets) in enumerate(testDataLoader):
            output = model(imgs)
            loss = loss_fn(output, targets)
            total_test_loss += loss.item()
            accuracy = (output.argmax(1) == targets).sum()
            total_accuracy += accuracy.item()
    print(f'total_test_loss: {total_test_loss}')
    print(f'total_accuracy = {total_accuracy / test_data_size}')
    writer.add_scalar("test_loss", total_test_loss, total_test_steps)
    writer.add_scalar("accuracy", total_accuracy, total_test_steps)
    total_test_steps += 1
writer.close()
