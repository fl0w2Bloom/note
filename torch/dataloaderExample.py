import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

train_data = torchvision.datasets.MNIST(
    root=r'mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),
    download=True
)

trainDataLoader = DataLoader(dataset=train_data, batch_size=4, shuffle=True)
print(train_data[0][0].shape)
print(train_data[0][1])
writer = SummaryWriter(r"logs")
for idx, (img, target) in enumerate(trainDataLoader):
    for id1, i in enumerate(img):
        writer.add_image(f'{idx}', i, id1)
    if idx == 8:
        break

writer.add_image("twet", train_data[0][0], train_data[0][1])
writer.close()
