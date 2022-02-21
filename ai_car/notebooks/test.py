import torch
import torchvision

CATEGORIES = ['apex']

device = torch.device('cuda')
model = torchvision.models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(512, 2 * len(CATEGORIES))
model = model.cuda().eval().half()
model.load_state_dict(torch.load('road_following_model_1.pth'))
from torch2trt import torch2trt
print("torch OK \n")
data = torch.zeros((1, 3, 224, 224)).cuda().half()

model_trt = torch2trt(model, [data], fp16_mode=True)

torch.save(model_trt.state_dict(), 'road_following_model_trt.pth')

import torch
from torch2trt import TRTModule

model_trt = TRTModule()
model_trt.load_state_dict(torch.load('road_following_model_trt.pth'))
print("model OK \n")
from jetracer.nvidia_racecar import NvidiaRacecar

car = NvidiaRacecar()
print("car OK \n")
from jetcam.csi_camera import CSICamera

camera = CSICamera(width=224, height=224, capture_fps=65)
print("camera OK \n")
from utils import preprocess
import numpy as np
import ipywidgets.widgets as widgets
concontroller = widgets.Controller(index=0)

STEERING_GAIN = -0.75
STEERING_BIAS = 0.00
car.throttle = -0.5

while True:
    image = camera.read()
    image = preprocess(image).half()
    output = model_trt(image).detach().cpu().numpy().flatten()
    x = float(output[0])
    print(output)
    car.steering =x 
