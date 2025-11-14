"""
Modify the last layer to output 2 classes
"""
from step02_load_resnet_model import model
# Import module
# Import torch.nn to modify the fully connected (fc) layer
import torch.nn as nn

# Update the fully connected (fc) layer to output 2 classes
model.fc = nn.Linear(512, 2)  # 512 is the input size for ResNet18's fc layer


