import torch
import torchvision.transforms as transforms
import torch.nn.functional as F
import cv2
import PIL.Image
import numpy as np

#mean = torch.Tensor([0.485, 0.456, 0.406]).cuda()
#std = torch.Tensor([0.229, 0.224, 0.225]).cuda()

def preprocess(image):
    device = torch.device('cuda')
    image = PIL.Image.fromarray(image)
    transform = transforms.Compose([transform.Resize(32),transforms.ToTensor()])
    image = transform(image)
    #image.sub_(mean[:, None, None]).div_(std[:, None, None])
    
    return image[None, ...]