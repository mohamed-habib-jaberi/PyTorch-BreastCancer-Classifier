"""
Using pre-trained models from torchvision, load resnet18 with default Resnet18 weghts.

Set output layer to 2 classes.

Load our fine tuned model from a checkpoint.

Load the model parameters from the checkpoint. 
"""
# Import modules
import torch
import torch.nn as nn
from torchvision import models

# Load the model from torchvision models using default weights
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

# Set classes in output layer to 2
model.fc = nn.Linear(model.fc.in_features, 2)

# Load checkpoint
checkpoint = torch.load('resnet_checkpoint.tar', weights_only=True)

# Load the model parameters from the checkpoint
model.load_state_dict(checkpoint['model_state_dict'])
# Print the model
print(model)
