"""
Load the resnet18 model with pre-trained weights.

Use the DEFAULT class weights.
"""
# import module
from torchvision import models

# Load the ResNet18 model with pre-trained weights
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
