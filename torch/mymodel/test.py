import torch
import torchvision.transforms
from dataUtils import *
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.load('10.pth').to(device=device)

img = Image.open(r'img_4.png').convert('RGB')

transfrom = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])
img = transfrom(img)
img = torch.reshape(img, [1, 3, 32, 32])
img = img.to(device)
out = model(img)
result = out.argmax(1)
print(test_data.classes[result])
# for i in range(10):
#     print(test_data.classes[i])
