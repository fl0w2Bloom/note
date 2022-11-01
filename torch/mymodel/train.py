import time

import torch.optim
from torch.utils.tensorboard import SummaryWriter

from dataUtils import *
from model import Model
import torch.nn as nn

# create new model
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model = Model().to(device=device)
epochs = 10
lr = 5e-2
loss_fn = nn.CrossEntropyLoss().to(device=device)
optim = torch.optim.SGD(model.parameters(), lr=lr)
total_train_step = 0

writer = SummaryWriter("logs")

for epoch in range(epochs + 1):
    model.train()
    start_time = time.time()
    print(f"-------开始第{epoch + 1}个周期训练(共{epochs}个周期)-------")
    for idx, (imgs, targets) in enumerate(train_dataloader):
        imgs = imgs.to(device)
        targets = targets.to(device)
        output = model(imgs)
        loss = loss_fn(output, targets)
        optim.zero_grad()
        loss.backward()
        optim.step()
        total_train_step += 1
        end_time = time.time()
        if total_train_step % 100 == 0:
            print(end_time - start_time)
            print(f'total_train_step:{total_train_step},loss: {loss.item()}')
            writer.add_scalar("train loss", loss.item(), total_train_step)
    if epoch % 10 == 0 and epoch != 0:
        torch.save(model, f'{epoch}.pth')

    model.eval()
    total_accuracy = 0.0
    with torch.no_grad():
        for imgs, targets in test_dataloader:
            imgs = imgs.to(device)
            targets = targets.to(device)
            output = model(imgs)
            loss = loss_fn(output, targets)
            accuracy = (output.argmax(1) == targets).sum()
            total_accuracy += accuracy.item()
    print(f'total_accuracy/test_data_size: {total_accuracy / test_data_size}')
writer.close()
