import torch
import torchvision.models

vgg16 = torch.load(r'vgg16me.pth')
print(vgg16)

vgg_dict = torch.load(r'vgg_dict.pth')
vgg16 = torchvision.models.vgg16()
vgg = vgg16.load_state_dict(torch.load('vgg_dict.pth'))
print(vgg)