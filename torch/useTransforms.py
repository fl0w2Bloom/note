from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(r"logs")
img_path = r'preview.jpg'
img = Image.open(img_path)
print(img.size)
print(type(img))
trans = transforms.Compose([
    transforms.ToTensor(),
])

tensorImg = trans(img)
writer.add_image("full", tensorImg)

trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
imgNorm = trans_norm(tensorImg)

writer.add_image("norm", imgNorm)

img_randomErase = transforms.RandomVerticalFlip(0.7)
img = img_randomErase(tensorImg)
writer.add_image("random qwe ", img)

transGauss = transforms.GaussianBlur(3)
imgGauss = transGauss(tensorImg)
writer.add_image("Gauss", imgGauss)

transJitter = transforms.ColorJitter(1, 1, 1)
imgJitter = transJitter(tensorImg)
writer.add_image("Jitter", imgJitter)
import random

var = lambda: random.random()
for i in range(10):
    img = transforms.ColorJitter(i*0.5, i*0.5, i*0.5)(tensorImg)
    writer.add_image('Jitter', img, i)
writer.close()
